#Padaryti galerijos programą. T.y. paleista programa turi du mygtukus, pirmyn ir atgal. Spaudant mygtukus galima išvysti paveiksliukus iš dabartinės direktorijos.
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image


def forward(img_no):

	# GLobal variable so that we can have
	# access and change the variable
	# whenever needed
	global label
	global button_forward
	global button_back
	global button_exit
	label.grid_forget()

	# This is for clearing the screen so that
	# our next image can pop up
	label = Label(image=List_images[img_no-1])

	# as the list starts from 0 so we are
	# subtracting one
	label.grid(row=1, column=0, columnspan=3)
	button_for = Button(root, text="forward",
						command=lambda: forward(img_no+1))

	# img_no+1 as we want the next image to pop up
	if img_no == 4:
		button_forward = Button(root, text="Forward",
								state=DISABLED)

	# img_no-1 as we want previous image when we click
	# back button
	button_back = Button(root, text="Back",
						command=lambda: back(img_no-1))

	# Placing the button in new grid
	button_back.grid(row=5, column=0)
	button_exit.grid(row=5, column=1)
	button_for.grid(row=5, column=2)


def back(img_no):

	# We will have global variable to access these
	# variable and change whenever needed
	global label
	global button_forward
	global button_back
	global button_exit
	label.grid_forget()

	# for clearing the image for new image to pop up
	label = Label(image=List_images[img_no - 1])
	label.grid(row=1, column=0, columnspan=3)
	button_forward = Button(root, text="forward",
							command=lambda: forward(img_no + 1))
	button_back = Button(root, text="Back",
						command=lambda: back(img_no - 1))
	print(img_no)

	# whenever the first image will be there we will
	# have the back button disabled
	if img_no == 1:
		button_back = Button(root, Text="Back", state=DISABLED)

	label.grid(row=1, column=0, columnspan=3)
	button_back.grid(row=5, column=0)
	button_exit.grid(row=5, column=1)
	button_for.grid(row=5, column=2)


root = Tk()
root.title("Galerija")
root.geometry("1800x700")

image_1 = ImageTk.PhotoImage(Image.open("gallery/pic_1.jpg"))
image_2 = ImageTk.PhotoImage(Image.open("gallery/pic_2.jpg"))
image_3 = ImageTk.PhotoImage(Image.open("gallery/pic_3.jpg"))
image_4 = ImageTk.PhotoImage(Image.open("gallery/pic_4.jpg"))

List_images = [image_no_1, image_no_2, image_no_3, image_no_4]

label = Label(image=image_no_1)
label.grid(row=1, column=0, columnspan=3)

# We will have three button back ,forward and exit
button_back = Button(root, text="Back", command=back,
					state=DISABLED)

# root.quit for closing the app
button_exit = Button(root, text="Exit",
					command=root.quit)

button_forward = Button(root, text="Forward",
						command=lambda: forward(1))

# grid function is for placing the buttons in the frame
button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
button_forward.grid(row=5, column=2)

root.mainloop()
