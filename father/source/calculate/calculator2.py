import tkinter

window = tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False, False)

b1 = tkinter.Button(window, text="(0, 0)", borderwidth=2, relief="solid", highlightbackground="red", highlightcolor="green")
b2 = tkinter.Button(window, text="(0, 1)", borderwidth=2, relief="solid", highlightbackground="blue", highlightcolor="yellow")
b3 = tkinter.Button(window, text="(0, 2)", borderwidth=2, relief="solid", highlightbackground="pink", highlightcolor="purple")

b4 = tkinter.Button(window, text="(1, 0)", borderwidth=2, relief="solid", highlightbackground="orange", highlightcolor="gray")
b5 = tkinter.Button(window, text="(1, 1)", borderwidth=2, relief="solid", highlightbackground="green", highlightcolor="black")
b6 = tkinter.Button(window, text="(1, 3)", borderwidth=2, relief="solid", highlightbackground="cyan", highlightcolor="white")

b7 = tkinter.Button(window, text="(2, 1)", borderwidth=2, relief="solid", highlightbackground="brown", highlightcolor="gray")
b8 = tkinter.Button(window, text="(2, 2)", borderwidth=2, relief="solid", highlightbackground="gray", highlightcolor="blue")
b9 = tkinter.Button(window, text="(2, 4)", borderwidth=2, relief="solid", highlightbackground="black", highlightcolor="green")

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0, rowspan=2)
b5.grid(row=1, column=1, columnspan=6)
b6.grid(row=1, column=3)

b7.grid(row=2, column=1)
b8.grid(row=2, column=2)
b9.grid(row=2, column=99)

window.mainloop()
