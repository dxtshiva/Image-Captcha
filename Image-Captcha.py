# Necessary imports
import tkinter as tk
from tkinter import CENTER, END, messagebox
from PIL import Image, ImageTk
from captcha.image import ImageCaptcha
import string,random
import os

#Function to generate random length captcha
def random_string():
    
    # hash length
    N = random.choice([5,6,7])
    s = string.ascii_uppercase + string.ascii_lowercase + string.digits
    
    # generate a random string of length N
    global captcha_text
    captcha_text = ''.join(random.choices(s, k=N))
    
    # Generate image captcha from the captcha text
    image = ImageCaptcha(width = 180, height = 60)
    image.generate(captcha_text)
    
    # Store the image to directory to display in GUI
    global path
    path = './' + captcha_text+ '.png'
    image.write(captcha_text, path)

# Initializing the tkinter 
root = tk.Tk()
captchaLbl = tk.Label(root)
captchaTxt = tk.Entry(root)

# Function to check whether the entered captcha matches the genreated captcha
def submit():
    userCaptcha = captchaTxt.get().strip()
    if userCaptcha=="":
        messagebox.showwarning("","Enter the captcha")
    elif userCaptcha==captcha_text:
        messagebox.showinfo("Success","Captcha verified successfully!")
        captchaTxt.config(text="")
        captchaTxt.delete(0,END)
        regenerate()
    else:
        messagebox.showerror("","Enter the correct captcha")

# Function to generate a new captcha and display it on the label
def regenerate():
    os.remove(path)
    random_string()
    print(captcha_text)
    img = ImageTk.PhotoImage(Image.open(path))
    captchaLbl.config(image=img,height="48px",width="136px")
    captchaLbl.image= img

# Generating the initial captcha text and image
random_string()
print(captcha_text)

# Configuring the root container
root.title("Captcha Generation")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
app_width = 480
app_height= 420
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.configure(background = '#ffd9db')

# Adding the header label to GUI
introLbl = tk.Label(root,text="Welcome to the captcha generator",font=("Arial",15))
introLbl.grid(row=2,column=1,pady=28,padx=90,columnspan=4,rowspan=2);
introLbl.config(anchor=CENTER)

# Adding the captcha image to GUI
img = ImageTk.PhotoImage(Image.open(path))
captchaLbl.config(height="45px",width="130px",image=img)
captchaLbl.grid(row=4,column=1,pady=8,columnspan=4)

# Adding the label for user entry
entryLbl = tk.Label(root,text="Enter the captcha text shown above: ",font=("Arial",13))
entryLbl.grid(row=5,column=1,columnspan=3,pady=8,padx=25)

# Adding the text entry to take input from user
captchaTxt.config(font=("Arial",14),width=12)
captchaTxt.grid(row=5,column=4,pady=8)

# Adding the submit button to verify the captcha
submitBtn = tk.Button(root,text="Submit",command=submit,font=("Arial",13))
submitBtn.grid(row=7,column=2,pady=8)

# Adding the button to generate a new captcha
resetBtn = tk.Button(root,text="Regenerate",command=regenerate,font=("Arial",13))
resetBtn.grid(row=7,column=3,pady=8,padx=10)

# Defining an event to delete the last generated captcha 
def on_closing():
    os.remove(path)
    root.destroy()

# Running the tkinter
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()