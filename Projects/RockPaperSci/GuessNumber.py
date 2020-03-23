from tkinter import *
import random

answer = random.randint(1, 21)


def showResult():
    fetch_guess = int(guess_field.get())
    if fetch_guess == answer:
        result = Tk()
        result.title("Your Number")
        result.geometry("250x250")
        result.config(background="green")

        user_guess = Label(result, text="Your guess was: " + str(guess_field.get()), bg="black", fg="white",
                           font="times 12 bold")
        user_guess.grid(row=1, column=1)

        result_title = Label(result, text="You were correct!", bg="white",
                             font="times 12 bold")
        result_title.grid(row=2, column=1)

        play_again = Button(result, text="Play Again?", bg="white", fg="red", font="times 12 bold",command=reset)
        play_again.grid(row=3, column=1)

        Exit_result = Button(result, text="Exit", fg="blue", bg="red", command=exit)
        Exit_result.grid(row=4, column=1)

    else:
        result = Tk()
        result.title("Your Number")
        result.geometry("250x250")
        result.config(background="red")

        user_guess = Label(result, text="Your guess was: " + str(guess_field.get()), bg="black", fg="white",
                           font="times 12 bold")
        user_guess.grid(row=1, column=1)

        result_title = Label(result, text="The correct number is: " + str(answer), bg="white",
                             font="times 12 bold")
        result_title.grid(row=2, column=1)

        play_again = Button(result, text="Play Again?", bg="white", fg="red", font="times 12 bold",command=reset)
        play_again.grid(row=3, column=1)

        Exit_result = Button(result, text="Exit", fg="blue", bg="red", command=exit)
        Exit_result.grid(row=4, column=1)

def reset():
    window = Tk()
    window.title("Guess the number")
    window.geometry("250x250")
    window.config(background="black")

    title = Label(window, text="Guess the number!", bg="dark gray", font="times 12 bold")
    title.grid(row=1, column=1)

    entry = Label(window, text="Enter a number between 1-20", bg="lightgreen", font="times 12 bold")
    entry.grid(row=2, column=1)

    guess_field = Entry(window)
    guess_field.grid(row=3, column=1)

    show = Button(window, text="Show Answer", bg="red", font="times 12 bold", command=showResult)
    show.grid(row=4, column=1)

    Exit = Button(window, text="Exit", fg="blue", bg="red", command=exit)
    Exit.grid(row=5, column=1)




if __name__ == '__main__':
    window = Tk()
    window.title("Guess the number")
    window.geometry("250x250")
    window.config(background="black")

    title = Label(window, text="Guess the number!", bg="dark gray", font="times 12 bold")
    title.grid(row=1, column=1)

    entry = Label(window, text="Enter a number between 1-20", bg="lightgreen", font="times 12 bold")
    entry.grid(row=2, column=1)

    guess_field = Entry(window)
    guess_field.grid(row=3, column=1)

    show = Button(window, text="Show Answer", bg="red", font="times 12 bold", command=showResult)
    show.grid(row=4, column=1)

    Exit = Button(window, text="Exit", fg="blue", bg="red", command=exit)
    Exit.grid(row=5, column=1)

    window.mainloop()
