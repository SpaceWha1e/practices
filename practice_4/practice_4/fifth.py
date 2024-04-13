from tkinter import *


def button_click(number):
    myEntry.insert(len(myEntry.get()), number)


def button_clear():
    myEntry.delete(0, last=END)


def button_add():
    global f_num
    global math
    f_num = int(myEntry.get())
    print(f_num)
    math = '+'
    button_clear()


def button_multiply():
    global f_num
    global math
    f_num = int(myEntry.get())
    math = '*'
    button_clear()


def button_subtract():
    global f_num
    global math
    f_num = int(myEntry.get())
    math = '-'
    button_clear()


def button_divide():
    global f_num
    global math
    f_num = int(myEntry.get())
    math = '/'
    button_clear()


def button_equal():
    global f_num
    global math
    s_num = int(myEntry.get())
    button_clear()

    if math == '+':
        myEntry.insert(0, str(f_num + s_num))
    elif math == '*':
        myEntry.insert(0, str(f_num * s_num))
    elif math == '-':
        myEntry.insert(0, str(f_num - s_num))
    elif math == '/':
        myEntry.insert(0, str(f_num / s_num))

    print(f_num, s_num, math)


f_num = 0
math = ''

root = Tk()
w = root.winfo_screenwidth() // 2 - 150
h = root.winfo_screenheight() // 2 - 215
root.geometry(f'300x430+{w}+{h}')
root.title("Калькулятор")

frame = Frame(borderwidth=2, relief=SOLID, padx=8, pady=8)

# ----------------------------поле-ввода-----------------------------

myEntry = Entry(frame, width=40, borderwidth=5)
myEntry.grid(row=1, columnspan=3, pady=15)

# ------------------------------кнопки-------------------------------
button0 = Button(frame, width=10, height=3, text="0", command=lambda: button_click(0))
button1 = Button(frame, width=10, height=3, text="1", command=lambda: button_click(1))
button2 = Button(frame, width=10, height=3, text="2", command=lambda: button_click(2))
button3 = Button(frame, width=10, height=3, text="3", command=lambda: button_click(3))
button4 = Button(frame, width=10, height=3, text="4", command=lambda: button_click(4))
button5 = Button(frame, width=10, height=3, text="5", command=lambda: button_click(5))
button6 = Button(frame, width=10, height=3, text="6", command=lambda: button_click(6))
button7 = Button(frame, width=10, height=3, text="7", command=lambda: button_click(7))
button8 = Button(frame, width=10, height=3, text="8", command=lambda: button_click(8))
button9 = Button(frame, width=10, height=3, text="9", command=lambda: button_click(9))

buttonClear = Button(frame, width=22, height=3, text="Очистить", command=button_clear)
buttonAdd = Button(frame, width=10, height=3, text="+", command=button_add)
buttonMult = Button(frame, width=10, height=3, text="*", command=button_multiply)
buttonSub = Button(frame, width=10, height=3, text="-", command=button_subtract)
buttonDvd = Button(frame, width=10, height=3, text="/", command=button_divide)
buttonEq = Button(frame, width=22, height=3, text="=", command=button_equal)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
button0.grid(row=5, column=0)
buttonClear.grid(row=5, column=1, columnspan=2)
buttonAdd.grid(row=6, column=0)
buttonEq.grid(row=6, column=1, columnspan=2)
buttonSub.grid(row=7, column=0)
buttonMult.grid(row=7, column=1)
buttonDvd.grid(row=7, column=2)

frame.pack(anchor=CENTER, expand=1)

root.mainloop()
