import tkinter

x = 0
def scroll():
    global x
    x = (x-1)%640

    canvas.delete("IMAGE")
    canvas.create_image(x-320,240,image=bgimage[0],tag="IMAGE")
    canvas.create_image(x+320,240,image=bgimage[1],tag="IMAGE")

    root.after(10,scroll)

img_num = 2

root  = tkinter.Tk()
root.title("Spectrum")
canvas = tkinter.Canvas(width=640,height=240)
canvas.pack()

imgname = ["spectrum1.png", "spectrum2.png"]

bgimage = []
for i in range (img_num):
    bgimage.append(tkinter.PhotoImage(file=imgname[i]))

scroll()    
root.mainloop()