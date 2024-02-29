from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import subprocess

class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st Image
        img1 = Image.open("/Users/gavesh_aggarwal/Desktop/Python_project/pillow_venv/Images/face_page_2.jpg")
        img1 = img1.resize((650, 700))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # 2nd Image
        img2 = Image.open("/Users/gavesh_aggarwal/Desktop/Python_project/pillow_venv/Images/face_page_1.jpg")
        img2 = img2.resize((950, 700))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand", font=("times new roman", 25, "bold"),bg="green", fg="red", command=self.run_face_recognition)
        b1_1.place(x=350, y=612, width=250, height=50)

    def run_face_recognition(self):
        try:
            # Load the cascade
            face_cascade = cv2.CascadeClassifier('/Users/gavesh_aggarwal/Desktop/Python_project/pillow_venv/Scripts/haarcascade_frontalface_default.xml')

            # To capture video from webcam.
            cap = cv2.VideoCapture(0)

            while True:
                # Read the frame
                _, img = cap.read()

                # Convert to grayscale
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # Detect the faces
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)

                # Draw the rectangle around each face
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

                # Display
                cv2.imshow('img', img)

                # Stop if escape key is pressed
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    break

            # Release the VideoCapture object
            cap.release()
            cv2.destroyAllWindows()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")



if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
