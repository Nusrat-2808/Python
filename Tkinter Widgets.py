from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title('image')
root.geometry(500*500)
upload=Image.open("balcony.png")
image=ImageTk.PhotoImage(upload)
label=Label(root,image=image,height=450,width=400)
label.place(x=50,y=0)
label2=Label(root,text="This is how you add image in Tkinter Window")
label2.place(x=40,y=460)
root.mainloop()