from captcha.image import ImageCaptcha
import string,random
import tkinter as tk
from tkinter import CENTER
from PIL import Image, ImageTk

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

random_string()
print(captcha_text)

root = tk.Tk()
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

captchaLbl = tk.Label(root)
img = ImageTk.PhotoImage(Image.open(path))
captchaLbl.config(height="45px",width="130px",image=img)
captchaLbl.grid(row=4,column=1,pady=8,columnspan=4)

entryLbl = tk.Label(root,text="Enter the captcha text shown above: ",font=("Arial",13))
entryLbl.grid(row=5,column=1,columnspan=3,pady=8,padx=25)

captchaTxt = tk.Entry(root)
userCaptcha = tk.StringVar()
captchaTxt.config(font=("Arial",14),width=12,textvariable=userCaptcha)
captchaTxt.grid(row=5,column=4,pady=8)

root.mainloop()