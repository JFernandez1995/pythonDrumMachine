from playsound import playsound
import tkinter as tk

def sound1():
    playsound('/insert/path/to/.mp3file')

#define multiple sounds to assign to each pad


root = tk.Tk()
frame = tk.Frame(root)
frame.pack(side = tk.TOP)

bottomframe = tk.Frame(root)
bottomframe.pack( side = tk.TOP )

bottomframe2 = tk.Frame(root)
bottomframe2.pack( side = tk.TOP )


button1 = tk.Button(frame, 
                   text="Pad 1", 
                   fg="blue",
                   command=sound1,
                   height = 5, width = 10)
button1.pack(side=tk.LEFT)

button2 = tk.Button(frame,
                   text="Pad 2",
                    fg="blue",
                   command=sound1,
                   height = 5, width = 10)
button2.pack(side=tk.LEFT)

button3 = tk.Button(frame,
                   text="Pad 3",
                    fg="blue",
                   command=sound1,
                   height = 5, width = 10)
button3.pack(side=tk.LEFT)

button4 = tk.Button(bottomframe,
                   text="Pad 4",
                    fg="blue",
                   command=sound1,
                   height = 5, width = 10)
button4.pack(side=tk.LEFT)


button5 = tk.Button(bottomframe,
                   text="Pad 5",
                    fg="blue",
                   command=sound1,
                   height = 5, width = 10)
button5.pack(side=tk.LEFT)

button6 = tk.Button(bottomframe,
                   text="Pad 6",
                    fg="blue",
                   command=sound1,
                   height = 5, width = 10)
button6.pack(side=tk.LEFT)


button7 = tk.Button(bottomframe2,
                   text="Pad 7",
                    fg="blue",
                   command=sound1,
                   height = 5, width = 10)
button7.pack(side=tk.LEFT)


button8 = tk.Button(bottomframe2,
                   text="Pad 8",
                    fg="blue",
                   command=sound1,
                   height = 5, width = 10)
button8.pack(side=tk.LEFT)


button9 = tk.Button(bottomframe2,
                   text="Pad 9",
                    fg="blue",
                   command=sound1,
                   height = 5, width = 10)
button9.pack(side=tk.LEFT)

root.mainloop()