from tkinter import *
from tkinter import messagebox, filedialog, ttk
import camera
import datetime

now = datetime.datetime.now()
today = str(now)

def takePhotos():
	n = numberE.get()
	camera.make_dataset(n)

def takeGroupies():
	camera.take_groupie()

def register_btn():
	global numberE
	root = Tk()
	root.title('Student Face Registration')
	root.geometry('300x100+500+250')
	ins = Label(root, text='Enter Registration Number')
	ins.grid(sticky=W)

	number = Label(root, text='Username')
	number.grid(row=1, sticky=W)

	numberE = Entry(root)
	numberE.grid(row=1, column=1)
	numberE.focus()

	loginB = Button(root, text='Take Photos', command=takePhotos)
	loginB.grid(columnspan=2)
	root.mainloop()

def callback():
	global filepath
	filepath = filedialog.askopenfilename()

def submit():
	branch = var.get()
	code = var1.get()
	branch_code = branch+code
	print(branch_code+today+".jpg")


def attendance_btn():
	global root
	global var
	global var1
	root = Tk()
	root.title('Upload details')
	root.geometry('300x200+500+250')

	branch_name = Label(root, text='Select Branch')
	subject_code = Label(root, text='Select Subject')
	photo_name = Label(root, text='Select Photo')
	branch_name.grid(row=0, sticky=W)
	subject_code.grid(row=1, sticky=W)
	photo_name.grid(row=2, sticky=W)

	var = StringVar(root)
	var.set("CS") # initial value
	option1 = OptionMenu(root, var, "CS", "IT", "EC", "EE")
	option1.grid(row =0,column=1,sticky = W)

	var1 = StringVar(root)
	var1.set("601") # initial value
	option2 = OptionMenu(root, var1, "601", "602", "603")
	option2.grid(row =1, column=1,sticky = W)

	submitB = Button(root, text='Take Class Photograph', command=submit)
	submitB.grid(row=3, column=1,sticky=W)

	root.mainloop()

def home():
	root = Tk()
	root.title('Smart Attendance System')
	root.geometry("500x500")
	

	reg = Button(root,text='Registration',command=register_btn)
	att = Button(root,text='Take Attendance',command=attendance_btn)
	reg.pack()
	reg.place(relx=0.5, rely=0.5,height=30, width=100,anchor=CENTER)
	att.pack()
	att.place(relx=0.5, rely=0.3,height=30, width=100,anchor=CENTER)
	root.mainloop()

home()

