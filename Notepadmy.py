from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os


root=Tk()
root.geometry("500x500")
root.title("keshab ka menu")

def newbar():
	global file
	root.title("My Notepad Keshab")
	file = None
	t.delete(1.0,END)
	
	
	
def openbar():
	global file
	file=askopenfilename(defaultextension="*.txt",filetypes=[("All Files" ,"*.*"),("Text Documents","*.txt")])
	if file=="":
		file=None
	else:
		root.title(os.path.basename(file)+"-Notepad keshab")
		t.delete(1.0,END)
		f=open(file,"r")
		t.insert(1.0,f.read())
		f.close()
	
	

def saveasbar():
	global file
	if file ==None:
		file=asksaveasfilename(initialfile='Untitle.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
		if file=="":
			file=None
		else:
			f=open(file,'w')
			f.write(t.get(1.0,END))
			f.close
	
	
	


def exitbar():
	root.destroy()





def copybar():
	t.event_generate(("<<Copy>>"))	
def pastebar():
	t.event_generate(("<<Paste>>"))
def cutbar():
	t.event_generate(("<<Cut>>"))

#if __name__ == '__main__':
#	file()
	
# Main mainu bar

m=Menu(root)
m1=Menu(m)
m1.add_command(label="New",command=newbar)
m1.add_command(label="open",command=openbar)
m1.add_command(label="save",command=saveasbar)
m1.add_command(label="Exit",command=exitbar)
#m1.add_separator()
root.config(menu=m)

m.add_cascade(label="File",menu=m1)


#  Edit menu bar

m1=Menu(m)
m1.add_command(label="copy",command=copybar)
m1.add_command(label="paste",command=pastebar)
m1.add_command(label="cut",command=cutbar)

#m1.add_separator()
root.config(menu=m)

scrollbar=Scrollbar(root)

m.add_cascade(label="Edit",menu=m1)
t=Text(root,width='40',height='31',wrap=WORD,yscrollcommand=scrollbar.set)
scrollbar.config(command=t.yview)
scrollbar.pack(side=RIGHT,fill=Y)
t.pack()
root.mainloop()