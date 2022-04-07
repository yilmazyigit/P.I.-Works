from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("1300x560")
window.resizable(width=False, height=False)


frame2 = Frame(window, width = 1300, height = 50, relief = SUNKEN)
frame2.pack(side = TOP, expand = True, fill = BOTH)
frame3 = Frame(window, width = 1300, height = 510, relief = SUNKEN)
frame3.pack(side = TOP, expand = True, fill = BOTH)

frame4 = Frame(frame3, width = 650, height = 510, relief = FLAT)
frame4.pack(side = RIGHT, expand = True, fill = BOTH)
frame5 = Frame(frame3, width = 650, height = 510, relief = SUNKEN)
frame5.pack(side = LEFT, expand = True, fill = BOTH)

newUser = Button(frame2, text = "+ New User", background="blue")
newUser.place(x = 10, y = 10)

checkbutton1 = IntVar()
hideButton = Checkbutton(frame2, text = "Hide Disabled User",
                         variable=checkbutton1,
                         onvalue=1,
                         offvalue=0)
hideButton.place(x =100, y=10)

saveButton = Button(frame2, text = "Save User", background="blue", state=DISABLED).place(x=1200, y =10)



class Table:
    def __init__(self,frame5):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(frame5, width=15, fg='blue',
                               font=('Arial',12,'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

lst = [('ID','User Name','E-mail',"Enabled"),
       (1,'Admin User','admin@piworks.net','true'),
       (2,'Test User','testuser@piworks.net','true')]

total_rows = len(lst)
total_columns = len(lst[0])
t = Table(frame5)



lbl = Label(frame4, text="New User", font=('Arial',15,'bold'))
lbl.place(x = 20,y = 20)

a = Label(frame4 ,text = "Username: ").place(x = 20, y = 70)
b = Label(frame4 ,text = "Display Name:").place(x = 20, y = 120)
c = Label(frame4 ,text = "Phone:").place(x = 20, y = 170)
d = Label(frame4 ,text = "Email:").place(x = 20, y = 220)
e = Label(frame4 ,text = "User Roles:").place(x = 20, y = 270)
a1 = Entry(frame4).place(x = 150, y = 70)
b1 = Entry(frame4).place(x = 150, y = 120)
c1 = Entry(frame4).place(x = 150, y = 170)
d1 = Entry(frame4).place(x = 150, y = 220)
e1 = Entry(frame4).place(x = 150, y = 270)
#
checkbutton2 = IntVar()
enabledButton = Checkbutton(frame4, text = "Enabled",
                         variable=checkbutton2,
                         onvalue=1,
                         offvalue=0)
enabledButton.place(x =20, y=320)

l1 = Label(frame4, text="Guest\n Admin \n SuperAdmin", borderwidth=2, relief="groove").place(x=625,y = 460)


window.mainloop()