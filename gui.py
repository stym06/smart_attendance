import MySQLdb
from tkinter import *
from tkinter import messagebox, filedialog, ttk

def checkLogin():
	u = nameE.get()
	p = pwordE.get()

	# messagebox.showinfo('Login', p)

	db = MySQLdb.connect('localhost', 'root','','attendance')
	cur = db.cursor()

	cur.execute("SELECT * FROM login where username='" + u + "'")

	flag=0

	for row in cur.fetchall():
		# messagebox.showinfo('Login', row)
		if row[2] == p:
			flag=1
			break

	if flag == 1:
		messagebox.showinfo('Login', 'Login Succesful')
		root.destroy()
		Upload()
	else:
		messagebox.showinfo('Login', 'Incorrect Username or Password')
		nameE.delete(0, END)
		pwordE.delete(0, END)


def loginscreen():
	global nameE
	global pwordE
	global root
	root = Tk()
	root.title('Login')
	root.geometry('300x100+500+250')
	ins = Label(root, text='Enter credentials')
	ins.grid(sticky=W)

	name = Label(root, text='Username')
	pword = Label(root, text='Password')
	name.grid(row=1, sticky=W)
	pword.grid(row=2, sticky=W)

	nameE = Entry(root)
	pwordE = Entry(root, show='*')
	nameE.grid(row=1, column=1)
	pwordE.grid(row=2, column=1)
	nameE.focus()

	loginB = Button(root, text='Login', command=checkLogin)
	loginB.grid(columnspan=2)
	root.mainloop()


def Upload():
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
	
	imageuploadbutton = Button(text="Upload", command= callback)
	imageuploadbutton.grid(row=2,column = 1, sticky=W)

	submitB = Button(root, text='Submit', command=submit)
	submitB.grid(row=3, column=1,sticky=W)

	showdata = Button(root, text='Show Attendence', command=destroy_upload)
	showdata.grid(row=4, column=1,sticky=W)

	logoutB = Button(root, text='Logout', command=logout)
	logoutB.grid(row=5, column=1,sticky=W)

	root.mainloop()

loginscreen()