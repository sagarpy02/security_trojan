from cgi import test
from tkinter import *
import cv2
import smtplib
import imghdr
from email.message import EmailMessage
from tkinter import messagebox

userid = 'sagar'
password = '123'

def getvals():
    username =uservalue.get()
    pas =passvalue.get()
    print(type(username))
    print(type(pas))
    if(username =='sagar' and pas=='123'):
            messagebox.showinfo("Succesfully Loged In", "Congratulation You are login Succesfully")
    else:
        messagebox.showerror('Wrong Password of username', 'You entered a wrong Password or Username please try again later!')
        videoCaptureObject = cv2.VideoCapture(0)
        result = True
        while(result):
            ret,frame = videoCaptureObject.read()
            cv2.imwrite("suspect.jpg",frame)
            result = False
        videoCaptureObject.release()
        cv2.destroyAllWindows()
        EMAIL_ADDRESS = 'sagarthorattrojan@gmail.com'
        EMAIL_PASSWORD = 'Kevin$123'

        contacts = ['sagarthorat01700@gmail.com', 'vaishnavidhole2000@gmail.com ','nanavarea77@gmail.com','adityadkashid@coep.sveri.ac.in']

        msg = EmailMessage()
        msg['Subject'] = 'Sycurity Alert!'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = contacts
        msg.set_content('Hello Sir/Madam, Someone trying to login to your account here is that person look out and punish him/her')

        with open('suspect.jpg','rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
        msg.add_alternative(file_data,maintype='image',subtype=file_type,filename=file_name)


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
root = Tk()
root.geometry("1200x988")

user = Label(root, text="Username" ,font=("Poppins bold",25),padx=50)
password = Label(root, text="Password",font=("Poppins bold",25),padx=50)
user.grid()
password.grid(row=1)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvals ,font=("Poppins bold",25)).grid()

root.mainloop()