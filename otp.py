import random
import smtplib
from validate_email import validate_email
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('300x300')


entry = Entry(root,fg='#FF4517',bg='#FFF9C2',bd=1)
entry.place(x=120,y=50,width=350,height=20)


label = Label(root,text='Enter Your Mail')
label.place(x=15,y=50)

otp_num = random.randint(1000,10000)

def vali():
    
     #genrate a 4-digit otp number
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()  # for security...
    server.login('mithaimadhuri3421@gmail.com',password='kkumptfmirwsbwlw')  #login with 2 step verification
    msg = 'Hello user,Your OTP is '+str(otp_num)
    server.sendmail('saipraneeth918@gmail.com',entry.get(),msg)
    server.quit()
    messagebox.showinfo('','otp sent sucessfully')

#verified OTP
def result():
    messagebox.showinfo('','otp verified')
    
        


btn = Button(root,text="Send OTP",bd=0,bg='#1061E6',command=vali)
btn.place(x=199,y=120)

entry2 = Entry(root)
entry2.place(x=120,y=190,width=350,height=20)

label2 = Label(root,text='Enter Your OTP')
label2.place(x=15,y=190)

btn2= Button(root,text="Submit",bg='#B3B3FF',command=result)
btn2.place(x=199,y=260)





root.mainloop()