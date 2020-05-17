import pygame
import dot
import random


# Initializes Pygame
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 40)
notefont = pygame.font.SysFont('Arial', 30)
screenWidth = 825
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
running = True
timer = pygame.time.Clock()
effect = pygame.mixer.Sound('beep-07.wav')  # set up the sound cliip

# Colors
colorKey = {
    "Healthy": (0, 0, 255),  # Blue
    "Immune": (0, 255, 0),  # Green
    "Sick": (255, 0, 0),  # Red
    "Infected": (255, 150, 0),  # Orange
    "Dead": (0, 0, 0)  # Black
}
# Create Sprites
all_sprites_list = pygame.sprite.Group()

dotList = []

infection_origin = random.randint(5, 100)
for i in range(100):
    if i < 5:
        start = (random.randint(0, 499), random.randint(0, 499))
        # end = (start[0],start[1])
        end = (random.randint(0, 499), random.randint(0, 499))
        state = "Immune"
        size = 5
        dotObj = dot.Dot(start, end, state, size, True, False)
        dotList.append(dotObj)
        all_sprites_list.add(dotObj)
    elif i == infection_origin:
        start = (random.randint(0, 499), random.randint(0, 499))
        end = (random.randint(0, 499), random.randint(0, 499))
        state = "Infected"
        size = 5
        dotObj = dot.Dot(start, end, state, size, True, False)
        dotList.append(dotObj)
        all_sprites_list.add(dotObj)
    else:
        start = (random.randint(0, 499), random.randint(0, 499))
        end = (random.randint(0, 499), random.randint(0, 499))
        state = "Healthy"
        size = 5
        dotObj = dot.Dot(start, end, state, size, True, False)
        dotList.append(dotObj)
        all_sprites_list.add(dotObj)

frame = 5
day = 0
counter = 0

healthy_list = []
immune_list = []
sick_list = []
infected_list = []
dead_list = []

healthy_counter = 0
immune_counter = 0
sick_counter = 0
infected_counter = 0
dead_counter = 0

# Pygame Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Sets a white background
    screen.fill((255, 255, 255))
    # Calculates time and days
    seconds = pygame.time.get_ticks() / 1000
    counter += timer.get_time() // 20
    day = seconds // 1
    if day > 0:
        day -= 1

    # Draw Sprites
    # Maybe an idea? Keep this in thought?
    for i in all_sprites_list:
        pygame.draw.circle(screen, i.color, i.current, i.size)
        i.Back()
        all_sprites_list.remove(i)
        hit_list = pygame.sprite.spritecollide(i, all_sprites_list, False, pygame.sprite.collide_circle_ratio(-1))
        all_sprites_list.add(i)

        if i.state == "Healthy" and i not in healthy_list:
            healthy_list.append(i)
            healthy_counter = len(healthy_list)
        if i.state == "Immune" and i not in immune_list:
            immune_list.append(i)
            immune_counter = len(immune_list)
        if i.state == "Sick" and i not in sick_list:
            sick_list.append(i)
            sick_counter = len(sick_list)
        if i.state == "Infected" and i not in infected_list:
            infected_list.append(i)
            infected_counter = len(infected_list)
        if i.state == "Dead" and i not in dead_list:
            dead_list.append(i)
            dead_counter = len(dead_list)

        for j in hit_list:
            # Collision Avoidance works to a certain extent
            # i.avoid()
            # j.avoid2()
            if i.isInfected() is True:
                j.hasInfection()
                j.update()
            elif j.isInfected() is True:
                i.hasInfection()
                i.update()

        # Checks to see if it will become sick
        if i.state == "Infected":
            # Create a timer to see if Infected becomes sick? Works but could be better
            i.time += 1
            if i.time == 150:
                i.updateState("Sick")
                if i.SD6 == True:
                    i.stop()
                else:
                    # If SD6 is False resets time clock but keeps moving
                    i.time_reset()
        # If sick for long enough see if it will recover
        if i.state == "Sick":
            i.time += 1
            if i.time == 150:
                i.recover()

        # Draws histogram on the right of screen
        pygame.draw.rect(screen, (155, 120, 150), (500, 0, 200, 500))
        pygame.draw.rect(screen, (0, 0, 255), (700, 500, 25, -len(healthy_list) * 5))
        pygame.draw.rect(screen, (0, 255, 0), (725, 500, 25, -len(immune_list) * 5))
        pygame.draw.rect(screen, (255, 0, 0), (750, 500, 25, -len(sick_list) * 5))
        pygame.draw.rect(screen, (255, 150, 0), (775, 500, 25, -len(infected_list) * 5))
        pygame.draw.rect(screen, (0, 0, 0), (800, 500, 25, -len(dead_list) * 5))

        for i in healthy_list:
            if i.state != "Healthy":
                healthy_list.remove(i)
                healthy_counter = len(healthy_list)
        for i in immune_list:
            immune_counter = len(immune_list)
        for i in sick_list:
            if i.state != "Sick":
                sick_list.remove(i)
                sick_counter = len(sick_list)
        for i in infected_list:
            if i.state != "Infected":
                infected_list.remove(i)
                infected_counter = len(infected_list)
        for i in dead_list:
            dead_counter = len(dead_list)

        day_text = str("Day: " + str(int(day)))
        day_surface = myfont.render(day_text, False, (255, 255, 255))
        screen.blit(day_surface, (550, 10))

        healthy_text = str("Healthy: " + str(healthy_counter))
        healthy_surface = myfont.render(healthy_text, False, (0, 0, 255))
        screen.blit(healthy_surface, (505, 50))

        immune_text = str("Immune: " + str(immune_counter))
        immune_surface = myfont.render(immune_text, False, (0, 255, 0))
        screen.blit(immune_surface, (505, 90))

        sick_text = str("Sick: " + str(sick_counter))
        sick_surface = myfont.render(sick_text, False, (255, 0, 0))
        screen.blit(sick_surface, (505, 130))

        infected_text = str("Infected: " + str(infected_counter))
        infected_surface = myfont.render(infected_text, False, (255, 150, 0))
        screen.blit(infected_surface, (505, 170))

        dead_text = str("Dead: " + str(dead_counter))
        dead_surface = myfont.render(dead_text, False, (0, 0, 0))
        screen.blit(dead_surface, (505, 210))

        remember_text = str("REMEMBER!")
        remember_surface = myfont.render(remember_text, False, (255, 105, 180))
        screen.blit(remember_surface, (520, 250))

        fact_text = str("Stay Indoors!")
        fact_surface = notefont.render(fact_text, False, (0, 0, 0))
        screen.blit(fact_surface, (540, 290))

        fact2_text = str("AND")
        fact2_surface = notefont.render(fact2_text, False, (0, 0, 0))
        screen.blit(fact2_surface, (575, 330))

        fact3_text = str("Wear a mask")
        fact3_surface = notefont.render(fact3_text, False, (0, 0, 0))
        screen.blit(fact3_surface, (535, 370))

        fact4_text = str("when outside!")
        fact4_surface = notefont.render(fact4_text, False, (0, 0, 0))
        screen.blit(fact4_surface, (535, 410))

    all_sprites_list.update(screen)

    # Flips the display
    pygame.display.flip()
    timer.tick(20)

pygame.QUIT()

