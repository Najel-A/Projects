from tkinter import *
import math


def convert():
    weight = int(weight_entry.get())
    height = int(height_entry.get())

    BMI = (703 * weight) / math.pow(height, 2)

    result = Tk()
    result.title("Results")
    result.geometry("375x150")
    result.config(bg="skyblue")

    chart = ""
    reply = ""
    if BMI < 18.5:
        chart = "Underweight"
        reply = ", perhaps you should eat a little more."

    elif BMI >= 18.5 and BMI <= 24.9:
        chart = "Normal Weight"
        reply = ", maintain your diet."

    elif BMI > 24.9 and BMI <= 29.9:
        chart = "Overweight"
        reply = ", cut back on the carbohydrates."

    else:
        chart = "Obesity"
        reply = ", maybe you should hit the gym."

    result_title = Label(result, text="Your Results", bg="green", font="times 24 bold")
    result_title.grid(row=1, column=1)

    height_entered = Label(result, text="Your height is: " + str(height) + " inches.")
    height_entered.grid(row=2, column=1)

    weight_entered = Label(result, text="Your weight is: " + str(weight) + "pounds.")
    weight_entered.grid(row=3, column=1)

    BMI_conversion = Label(result, text="Your BMI is: " + str("{:.1f}".format(BMI)), font="times 18 underline")
    BMI_conversion.grid(row=4, column=1)

    chart_label = Label(result, text="You are " + chart + reply, font="times 14 bold")
    chart_label.grid(row=5, column=1)

    result.mainloop()

if __name__ == '__main__':

    window = Tk()
    window.title("BMI Calculator")
    window.geometry("390x250")
    window.config(bg="lightgray")

    title = Label(window, text="BMI Conversion Calculator", bg="blue", font="times 32 bold")
    title.grid(row=1, column=1)

    weight = Label(window, text="Enter weight in pounds:", bg="red", font="times 22 bold")
    weight.grid(row=2, column=1)

    weight_entry = Entry(window)
    weight_entry.grid(row=3, column=1)

    height = Label(window, text="Enter height in inches:", bg="red", font="times 22 bold")
    height.grid(row=4, column=1)

    height_entry = Entry(window)
    height_entry.grid(row=5, column=1)

    show = Button(window, text="Get Results", bg="red", font="times 22 bold", command=convert)
    show.grid(row=6, column=1)

    Exit = Button(window, text="Exit", fg="blue", bg="red", command=exit, font="times 18 bold")
    Exit.grid(row=7, column=1)

    window.mainloop()
