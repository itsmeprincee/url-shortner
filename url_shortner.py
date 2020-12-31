from tkinter import *
import pyshorteners
import pyperclip
def get_url():
    global n,generated_frame,url
    gett_url = n.get()
    shortener = pyshorteners.Shortener()
    x = shortener.tinyurl.short(gett_url)
    url.set(x)
    generated_frame.pack()
def copy_url():
    global url
    pyperclip.copy(url.get())
def master_gadgets():
    global generated_frame,n,url
    #main heading that describes the window..
    url_shortner_label = Label(master,font=("Helvetica",18,"bold"),fg="black",bg="white",pady=10,text="URL Shortner")
    url_shortner_label.pack()
    #creating another frame to take input from the user to short the url....
    normal_frame = Frame(master,bg='white')
    normal_frame.pack()
    n=StringVar()
    n.set("copy your link here")
    normal_entry=Entry(normal_frame,textvariable=n,font=("times new roman",15,"italic"),width=50,bg="ghostwhite")
    normal_entry.grid(row=0,column=0,columnspan=3,pady=10)
    command_button = Button(normal_frame,text="Generate Url",bd=0,bg='#61afef',padx=5,pady=5,font=("times new roman",11,"bold"),activebackground="#9a63ae",command=get_url)
    command_button.grid(row=1,column=1,pady=10)
    #creating another frame to display the generated url..
    generated_frame = Frame(master,bg="white")
    url=StringVar()
    generated_entry = Entry(generated_frame,textvariable=url,font=("times new roman",15,"italic"),width=40,bg="ghostwhite")
    generated_entry.grid(row=0,column=0,columnspan=2,pady=10,padx=5)
    copy_button = Button(generated_frame,text="Copy url",bd=0,bg="#61afef",font=("Helvetica",10,"bold"),width=10,activebackground="#9a63ae",command=copy_url)
    copy_button.grid(row=0,column=2)
master = Tk()
master.geometry("600x300")
master.resizable(False,False)
master.title("URl Shortner")
master.config(bg="white")
master_gadgets()
master.mainloop()
