from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
from PIL import ImageTk, Image, ImageOps, ImageFilter
import matplotlib.pyplot as plt 

image = False
original_image = False
    



#GUI

#initialize the main window 
window = Tk() 
window.title('IPwithGUI') 
window.geometry("800x550")
window.configure(bg='white')
window.resizable(False, False)

#canvas to open the image
canvas = Canvas(window, width=500, height=330, bg="white")
canvas.place(x = 180, y = 20)



# logical functions
def addImageToCanvas(image):
        imgtk = ImageTk.PhotoImage(image)
        canvas.image = imgtk
        canvas.create_image(0, 0, image = imgtk, anchor=NW)


def uploadImage():
    
    global image
    global original_image
    image_path = filedialog.askopenfilename(
            title = "Choose an image",
            filetypes=[("image files", ('.png', '.jpg'))]
            )
    if image_path:
        image = Image.open(image_path).convert("RGB")
        image = image.resize((500, 400), Image.ANTIALIAS)
        original_image = image
        addImageToCanvas(image)


def toBinary():
    global image
    if image:
        image = image.convert('1')
        addImageToCanvas(image)  

def toGray():
    global image
    if image:
        image = image.convert('LA')
        addImageToCanvas(image)


def reset():
    global image
    global original_image

    if image:
        image = original_image
        addImageToCanvas(image)



def histogram():
    global image
    
    if image:
        data = image.convert("LA").histogram()
        plt.bar(range(len(data)), data , color = 'blue',width = .4)
        plt.xlabel("Colors")
        plt.ylabel("Frequency")
        plt.title("Image Histogram")
        plt.show()
    

def edge_detection():
    global image
    if image:
        image = image.convert("L")
        image = image.filter(ImageFilter.FIND_EDGES)
        addImageToCanvas(image)

def complementImage():
    global image

    if image:
        image = ImageOps.invert(image)
        addImageToCanvas(image)


def rotateClock():
    global image

    if image:
        image = image.rotate(-45)
        addImageToCanvas(image)

def rotateAntiClock():
    global image

    if image:
        image = image.rotate(45)
        addImageToCanvas(image)

# basic operation label
bo_label = Label(window, width = 19, height = 5, anchor=CENTER,bg="white", text="Basic Operation").place(x = 0, y = 0)

# upload image button
upload_image_btn = Button(window, text="Upload Image", height=2, width=12,bg="#326fa8", command=uploadImage).place(x = 20, y= 100)

#to gray button 
to_gray_btn = Button(window, text="RGB to Gray", height=2, width=12,bg="#326fa8", command=toGray).place(x = 20, y= 160)


#to binary button
to_binray_btn = Button(window, text="Convert to Binary", height=2, width=12,bg="#326fa8", command=toBinary).place(x = 20, y= 220)

#reset button
reset_btn = Button(window, text="RESET", height=2, width=12,bg="#326fa8", command=reset).place(x = 20, y= 280)

#Advanced Operation Label
ao_label = Label(window, width = 19, height = 5,bg="white", anchor=CENTER, text="Advanced Operation").place(x = 20, y = 400)

#Histogram button
histogram_btn = Button(window, text="Histogram", height=2, width=12,bg="#326fa8", command=histogram).place(x = 200, y= 400)

#Complement image
complement_btn = Button(window, text="Complement Image", height=2, width=15,bg="#326fa8", command=complementImage).place(x = 350, y= 400)

#edge detection
edge_btn = Button(window, text="Edge Detection", height=2, width=14,bg="#326fa8", command=edge_detection).place(x = 520, y= 400)

#rotate clockwise
histogram_btn = Button(window, text="Rotate Clockwise", height=2, width=14,bg="#326fa8", command=rotateClock).place(x = 280, y= 460)


#rotate Anti-clockwise
histogram_btn = Button(window, text="Rotate Anti-Clockwise", height=2, width=16,bg="#326fa8",command=rotateAntiClock).place(x = 450, y= 460)


window.mainloop()







    






