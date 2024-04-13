from PIL import ImageTk, Image
from tkinter import Tk, Label, Button


def back():
    global imageList
    global label, label_info
    global current
    global button_back

    current -= 1
    current %= len(imageList)
    label.configure(image=imageList[current])
    label_info.configure(text="Image" + str(current + 1) + "/" + str(len(imageList)))

    if current == 0:
        button_back.configure(state="disabled")
    else:
        button_back.configure(state="active")

    if current == len(imageList) - 1:
        button_forward.configure(state="disabled")
    else:
        button_forward.configure(state="active")


def forward():
    global imageList
    global label, label_info
    global current
    global button_back

    current += 1
    current %= len(imageList)
    label.configure(image=imageList[current])
    label_info.configure(text="Image" + str(current + 1) + "/" + str(len(imageList)))

    if current == 0:
        button_back.configure(state="disabled")
    else:
        button_back.configure(state="active")

    if current == len(imageList) - 1:
        button_forward.configure(state="disabled")
    else:
        button_forward.configure(state="active")

root = Tk()
w = root.winfo_screenwidth() // 2 - 200
h = root.winfo_screenheight() // 2 - 200
root.geometry(f'400x400+{w}+{h}')
root.title("Альбом")

imageList = [ImageTk.PhotoImage((Image.open("images/test.png")).resize((200, 200))),
             ImageTk.PhotoImage((Image.open("images/test2.png")).resize((200, 200)))]

current = 0

label = Label(root, height=200, width=200, image=imageList[current])
label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<", command=back, state="disabled")
button_back.grid(row=1, column=0)

buttonEx = Button(root, text="Exit", command=lambda: root.quit())
buttonEx.grid(row=1, column=1)

button_forward = Button(root, text=">>", command=forward)
button_forward.grid(row=1, column=2)

label_info = Label(root, width=30, text="Image"+str(current + 1)+"/"+str(len(imageList)), justify="left", borderwidth=1, relief="sunken", anchor="e")
label_info.grid(row=2, column=0, columnspan=3, pady=8)
root.mainloop()
