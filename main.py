from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import playsound
import threading
import time

def start_sound():
	while True:
		playsound.playsound('audio/oof.mp3')
		time.sleep(0.1)

def sound_thread():
	t = threading.Thread(target=start_sound)
	t.setDaemon(True)
	t.start()


# Initialize screen
root = Tk()

# Make the title
root.title('FBI Login Prompt')

# Make the window size
root.geometry('600x400')

# Make it unresizable
root.resizable(0,0)

# Set the icon
root.iconbitmap('icons/topsecreticon.ico')

# Set the window to default tkinter bgcolor
default_bg = '#%02x%02x%02x' % (240, 240, 237) # RGB Color
root.configure(bg=default_bg)


# Open the topsecret_1 image
top1_img = Image.open('pictures/topsecret_1.png')
top1_img = top1_img.resize((200,200), Image.ANTIALIAS)
top1_img = ImageTk.PhotoImage(top1_img)

# Create the topsecret_1 label and add it onto the screen
top1_label = Label(root, image=top1_img)
top1_label.pack()




# Open the topsecret_2 image
top2_img = Image.open('pictures/topsecret_2.png')
top2_img = top2_img.resize((100,100), Image.ANTIALIAS)
top2_img = ImageTk.PhotoImage(top2_img)

# Create the topsecret_2 label and add it onto the screen
top2_label = Label(root, image=top2_img)
top2_label.place(x=20, y=30)


# Open the topsecret_3 image
top3_img = Image.open('pictures/topsecret_3.png')
top3_img = top3_img.resize((100,100), Image.ANTIALIAS)
top3_img = ImageTk.PhotoImage(top3_img)

# Create the topsecret_3 label and add it onto the screen
top3_label = Label(root, image=top3_img)
top3_label.place(x=475, y=30)

# Create the username label
username_label = Label(root, text='USERNAME:', fg='red', font=(None, 20))
username_label.place(x=50, y=240)


# Create the password label
password_label = Label(root, text='PASSWORD:', fg='blue', font=(None, 20))
password_label.place(x=50, y=290)


# Create the username entry
username_entry = Entry(root, width=20, font=(None, 20), fg='purple')
username_entry.place(x=230, y=240)

# Create the password entry
password_entry = Entry(root, width=20, font=(None, 20), fg='yellow', show='*')
password_entry.place(x=230, y=290)


def click():
	global johndoe_img
	messagebox.showwarning('Warning', 'Be carefal you are about to delete system32')

	def flashing_virus():
		while True:
			try:
				lb = Label(top, text='VIRUS DETECTED!!', font=(None, 30), fg='red')
				lb.pack()
				time.sleep(1)
				lb.pack_forget()
				time.sleep(1)
			except:
				return


	def flashing_thread():
		t = threading.Thread(target=flashing_virus)
		t.setDaemon(True)
		t.start()

	# Create a new window and keep on playing oof.mp3
	top = Toplevel(root)
	top.title('OOF')
	top.iconbitmap('icons/roblox.ico')
	top.geometry('400x450')
	top.resizable(0,0)

	# Add the johndoe image
	johndoe_img = Image.open('pictures/johndoe.png')
	johndoe_img = johndoe_img.resize((400, 400), Image.ANTIALIAS)
	johndoe_img = ImageTk.PhotoImage(johndoe_img)

	# Create the johndoe label
	johndoe_label = Label(top, image=johndoe_img)

	# Add that onto the second screen
	johndoe_label.pack()

	# Add a flashing VIRUS DETECTED
	flashing_thread()

	# Start the sound thread
	sound_thread()


# Continue button
continue_button = Button(root, text='CONTINUE', bg='black', fg='white', padx=210, command=click)
continue_button.place(x=50, y=350)



# Run the mainloop
root.mainloop()
