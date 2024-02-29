from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from face_recognition import Face_recognition


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #First Image
        img1=Image.open("/Users/gavesh_aggarwal/Desktop/Python_project/pillow_venv/Images/1.jpg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #Second Image
        img2=Image.open("/Users/gavesh_aggarwal/Desktop/Python_project/pillow_venv/Images/2.jpg")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #Third Image
        img3=Image.open("/Users/gavesh_aggarwal/Desktop/Python_project/pillow_venv/Images/3.jpg")
        img3=img3.resize((500,130))
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #Background Image
        img4=Image.open("/Users/gavesh_aggarwal/Desktop/Python_project/pillow_venv/Images/bgimg.jpg")
        img4=img4.resize((1530,710))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Student Button
        img5=Image.open("/Users/gavesh_aggarwal/Desktop/Python_project/pillow_venv/Images/student.jpg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand",font=("times new roman",20,"bold"),bg="orange",fg="blue")
        b1_1.place(x=200,y=300,width=220,height=40)

        #Detect Face Button
        img6=Image.open("/Users/gavesh_aggarwal/Desktop/Python_project/pillow_venv/Images/face_detector.jpg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand",command=self.face_data,font=("times new roman",20,"bold"),bg="purple",fg="blue")
        b1_1.place(x=500,y=300,width=220,height=40)

        #Attendance Button
        img7=Image.open("/Users/gavesh_aggarwal/Desktop/Python_project/pillow_venv/Images/attendance.jpg")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand")
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand",font=("times new roman",20,"bold"),bg="purple",fg="blue")
        b1_1.place(x=800,y=300,width=220,height=40)

        #Help Button
        img8=Image.open("/Users/gavesh_aggarwal/Desktop/Python_project/pillow_venv/Images/helpdesk.jpg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand")
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand",font=("times new roman",20,"bold"),bg="purple",fg="blue")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #Train Button
        img9=Image.open("/Users/gavesh_aggarwal/Desktop/Python_project/pillow_venv/Images/train_data.jpg")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand")
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand",font=("times new roman",20,"bold"),bg="purple",fg="blue")
        b1_1.place(x=200,y=580,width=220,height=40)

        #Photo Button
        img10=Image.open("/Users/gavesh_aggarwal/Desktop/Python_project/pillow_venv/Images/photos.jpg")
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand")
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand",font=("times new roman",20,"bold"),bg="purple",fg="blue")
        b1_1.place(x=500,y=580,width=220,height=40)

        #Developer Button
        img11=Image.open("/Users/gavesh_aggarwal/Desktop/Python_project/pillow_venv/Images/developer.jpg")
        img11=img11.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand")
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand",font=("times new roman",20,"bold"),bg="purple",fg="blue")
        b1_1.place(x=800,y=580,width=220,height=40)

        #Exit Button
        img12=Image.open("/Users/gavesh_aggarwal/Desktop/Python_project/pillow_venv/Images/exit.jpg")
        img12=img12.resize((220,220))
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,cursor="hand")
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand",font=("times new roman",20,"bold"),bg="purple",fg="blue")
        b1_1.place(x=1100,y=580,width=220,height=40)

        ############################## Function Buttons ##############################

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)



if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
