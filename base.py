from tkinter import *  

root = Tk()
root.geometry("300x100+800+10")
#root.title("sami")

lab = Label(text="texte", bg='red', fg='blue')
lab.pack()

but = Button(text= 'fermer', command=root.destroy)
but.pack()





root.mainloop()
