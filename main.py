import tkinter
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import math

window=tkinter.Tk()
window.title("My App")
window.config(width=600, height=600,bg="#7FC7D9",padx=20,pady=20)

title=tkinter.Label(text="Watermarker App",font=("Arial",25,"bold"),bg="#7FC7D9",fg="white",padx=15,pady=15)
title.grid(row=0,column=0)

btn3=None
def upload():
    file_types=[("All Files","*.*"),("Jpeg Files","*.jpg"),("Gif Files","*.gif")]
    file_path=filedialog.askopenfilename(multiple=False, filetypes=file_types)

    img=Image.open(file_path)
    img.resize((300,300))
    filename=file_path.split('/')[::-1][0]

    file_name=tkinter.Label(text=filename,font=("Arial",12,"italic"),fg="black",bg="#7FC7D9", padx=5, pady=5)
    file_name.grid(row=2,column=0)

    uploaded_img = ImageTk.PhotoImage(img)
    panel=tkinter.Label(image=uploaded_img,bg="white", borderwidth=5)
    panel.image=uploaded_img #display an image
    #panel["image"]=uploaded_img  #must be included if your uploading multiple files.
    panel.grid(row=3, column=0)

    def save():
        global btn3
        img = Image.open(file_path)
        watermark_img = img.copy()
        draw = ImageDraw.Draw(watermark_img)

        img_width, img_height = watermark_img.size
        img_x = math.floor(img_width / 2)
        img_y = math.floor(img_height / 2)

        if img_x > img_y:
            fontsize = img_y
        elif img_y > img_x:
            fontsize = img_x
        else:
            fontsize = img_x

        watermark_font = ImageFont.truetype("BAUHS93.TTF", int(fontsize / 6))
        draw.text((img_x, img_y), text="[watermark]", fill="#FAF9F6", font=watermark_font, anchor="ms")
        saved_img = filedialog.asksaveasfile(filetypes=file_types, defaultextension=".jpg")
        watermark_img.save(saved_img)
        messagebox.showinfo(title="Success", message="Your image has been successfully saved.")
        btn3.config(state="disabled")

    def add_watermark():
        global btn3
        img=Image.open(file_path)
        img.resize((300,300))
        display_img=img.copy()
        draw=ImageDraw.Draw(display_img)

        width,height=display_img.size
        #math.floor() and int() have the same output, a whole number disregarding the decimals.
        x=math.floor(width/2)
        y=math.floor(height/2)

        if x>y:
            font_size=y
        elif y>x:
            font_size=x
        else:
            font_size=x

        font=ImageFont.truetype("BAUHS93.TTF",int(font_size/6))

        draw.text((x,y),text="[watermark]",fill="#FAF9F6",font=font,anchor="ms")
        photo = ImageTk.PhotoImage(display_img)
        panel.config(image=photo)
        panel.image=photo
        btn2.grid_forget()

        btn3 = tkinter.Button(text="Download Image", padx=5, pady=5, command=save)
        btn3.grid(row=5, column=0, padx=10, pady=10)

    btn2=tkinter.Button(text="Add Watermark",padx=5,pady=5,command=add_watermark)
    btn2.grid(row=4,column=0,padx=10, pady=10)
    btn1.grid_forget()

btn1=tkinter.Button(text="Upload Image",padx=5,pady=5,command=upload)
btn1.grid(row=1,column=0)

window.mainloop()