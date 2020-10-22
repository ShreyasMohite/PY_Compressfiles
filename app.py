from tkinter import *
import tkinter.filedialog
import os
import tkinter.messagebox
import shutil
import threading



class Zipsfiles:
    def __init__(self,root):
        self.root=root
        self.root.title("Zip File Extracter")
        self.root.geometry("500x400")
        self.root.iconbitmap("logo931.ico")
        self.root.resizable(0,0)


        filepath=StringVar()
        save=StringVar()
        password=StringVar()

#===========================================================#

        
        def clear():
            filepath.set("")
            save.set("")
            password.set("")
            lab_successful.config(text="")

        def findfile():
            a = tkinter.filedialog.askopenfilename(title = "Select file",filetypes = (("Zips","*.zip"),("all files","*.*"))) 
            filepath.set(a)

        def savefile():
            a=tkinter.filedialog.askdirectory(title="choose folder")
            filepath.set(a)




        def zips():
            try:     
                shutil.make_archive(filepath.get()+"/"+save.get(),'zip',filepath.get())
                  
            except Exception as e:
                print(e)
        
        def thread_zip():
            t=threading.Thread(target=zips)
            t.start()



#===========================================================#
        mainframe=Frame(self.root,width=500,height=400,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=493,height=300,relief="ridge",bd=3,bg="#312244")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=493,height=93,relief="ridge",bd=3,bg="#354f52")
        secondframe.place(x=0,y=300)

#=============================================================#
        but_extract=Button(secondframe,width=14,text="Zips",font=('times new roman',12),cursor="hand2",command=thread_zip)
        but_extract.place(x=20,y=30)

        but_extract_password=Button(secondframe,width=14,text="Zips-Password",font=('times new roman',12),cursor="hand2")
        but_extract_password.place(x=175,y=30)
        
        but_clear=Button(secondframe,width=14,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=330,y=30)
#==================================================================#

        but_find_savefile=Button(firstframe,width=14,text="Save to Folder",font=('times new roman',12),cursor="hand2",command=savefile)
        but_find_savefile.place(x=175,y=30)

        ent_file=Entry(firstframe,width=50,font=('times new roman',12),relief="ridge",bd=3,textvariable=filepath)
        ent_file.place(x=40,y=70)

        lab_saveas=Label(firstframe,text="Enter Save as:",font=('times new roman',12),bg="#312244",fg="white")
        lab_saveas.place(x=70,y=130)

        ent_file=Entry(firstframe,width=24,font=('times new roman',12),relief="ridge",bd=3,textvariable=save)
        ent_file.place(x=200,y=130)

        lab_password=Label(firstframe,text="Enter Password",font=('times new roman',12),bg="#312244",fg="white")
        lab_password.place(x=70,y=230)

        ent_file=Entry(firstframe,width=24,font=('times new roman',12),relief="ridge",bd=3,textvariable=password)
        ent_file.place(x=200,y=230)

        lab_successful=Label(firstframe,text="",font=('times new roman',12),bg="#312244",fg="white")
        lab_successful.place(x=200,y=265)




     
if __name__ == "__main__":
    root=Tk()
    app=Zipsfiles(root)
    root.mainloop()
