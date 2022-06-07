import tkinter as tk
from tkinter import CENTER, END, StringVar, messagebox
from turtle import screensize, width
from PIL import Image, ImageTk
from captcha.image import ImageCaptcha
import string,random
import os
from matplotlib.pyplot import text

from sqlalchemy import null

def random_string():
    # hash length
    N = 6
    s = string.ascii_uppercase + string.ascii_lowercase + string.digits
    # generate a random string of length 5
    global captcha_text
    captcha_text = ''.join(random.choices(s, k=N))
    image = ImageCaptcha(width = 180, height = 60)
    data = image.generate(captcha_text)
    global path
    path = './' + captcha_text+ '.png'
    image.write(captcha_text, path)

root = tk.Tk()
userCaptcha = StringVar()
captchaLbl = tk.Label(root)
captchaTxt = tk.Entry(root)

def submit():
    
    if userCaptcha.get()=="":
        messagebox.showwarning("","Enter the captcha")
    elif userCaptcha.get()==captcha_text:
        messagebox.showinfo("Success","Captcha verified successfully!")
        captchaTxt.config(text="")
        captchaTxt.delete(0,END)
        regenerate()
    else:
        messagebox.showerror("","Enter the correct captcha")
        
def regenerate():
    os.remove(path)
    random_string()
    print(captcha_text)
    img = ImageTk.PhotoImage(Image.open(path))
    captchaLbl.config(image=img,height="45px",width="130px")
    captchaLbl.image= img
            
random_string()
print(captcha_text)


root.title("CAPTCHA Generation")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
app_width = 480
app_height= 420
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.configure(background = '#ffd9db')

introLbl = tk.Label(root,text="Welcome to the captcha generator",font=("Arial",15))
introLbl.grid(row=2,column=1,pady=28,padx=90,columnspan=4,rowspan=2);
introLbl.config(anchor=CENTER)

img = ImageTk.PhotoImage(Image.open(path))
captchaLbl.config(height="45px",width="130px",image=img)
captchaLbl.grid(row=4,column=1,pady=8,columnspan=4)

entryLbl = tk.Label(root,text="Enter the captcha text shown above: ",font=("Arial",13))
entryLbl.grid(row=5,column=1,columnspan=3,pady=8,padx=25)

captchaTxt.config(font=("Arial",14),width=12,textvariable=userCaptcha)
captchaTxt.grid(row=5,column=4,pady=8)

submitBtn = tk.Button(root,text="Submit",command=submit,font=("Arial",13))
submitBtn.grid(row=7,column=2,pady=8)


resetBtn = tk.Button(root,text="Regenerate",command=regenerate,font=("Arial",13))
resetBtn.grid(row=7,column=3,pady=8,padx=10)

def on_closing():
    os.remove(path)
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
