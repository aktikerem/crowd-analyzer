import supervision as sv
from ultralytics import YOLO
import cv2 as cv
import tkinter as tk
from PIL import Image, ImageTk
import ttkbootstrap as ttk
import numpy as np
import re

confval = 0.1
value1 = 320
root = ttk.Window(themename= 'vapor')
root.title("CAP Crowd Analyzer")
root.resizable(width=False, height=False)
#patern to cut the xywh part from the yolo output 
pattern = r'xyxy=array\((.*?)\, dtype=float32\)'
#k is for counting while drawing circles not optimal but its just works
k = 0
capture = cv.VideoCapture(0)
model = YOLO('model.pt')


label = tk.Label(root)
label.pack(side="left")

def getxyxy(detectionstring):
    match = re.search(pattern, detectionstring)
    if match:
     desired_substring = match.group(1)
     modified_substring = eval(str(desired_substring[1:-1]))
     return modified_substring
    else:
     print("No match found.")



# def to update the Tkinter window with each video frame
# also looks realy messy
def update():
    k = 0
    ret, frame = capture.read()
    if ret:
        result = model(frame,imgsz=(value1),max_det=-1,conf=confval)[0]
        detections = sv.Detections.from_ultralytics(result)
        if checkbox_var.get() == 1:
         for i in detections:
           xyxy = getxyxy(str(detections[k]))
           #find center of the bounding box

           cx = (xyxy[0] + xyxy[2])/2
           cy = (xyxy[1] + xyxy[3])/2
           cv.circle(frame, (round(cx),round(cy)), 3 , (0,0,255), thickness=-1)
           k += 1
        
        k = 0
        if checkbox_var2.get() == 1:
         cv.putText(frame, f'total person count : {str(len(detections))}' , (2,25), cv.FONT_HERSHEY_TRIPLEX, 1.0, (192, 64, 110), 2)
        # Convert the OpenCV BGR image to RGB
        rgb_image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        # Convert the RGB image to a Tkinter PhotoImage
        img = Image.fromarray(rgb_image)
        imgtk = ImageTk.PhotoImage(image=img)

        # Update the label with the new PhotoImage
        label.imgtk = imgtk
        label.configure(image=imgtk)

    # Call the update function after certain time it also makes the window move laggy
    root.after(2, update)


# def that converts slider two output into float so we can use it also asigns global var things 
def sliders_callback(value):
    global value1
    global value2
    global confval
    value1 = slider1_var.get()
    value2 = slider2_var.get()
    confval = (value2 / 100) 

input_frame = ttk.Frame(master=root,height=550)
sliders_frame = ttk.Frame(input_frame)
buttons_frame = ttk.Frame(input_frame)

# sliders for controlling parameters 
slider1_var = tk.IntVar()
slider1 = tk.Scale(sliders_frame, from_=320, to=1280, orient="horizontal", label="input img size", length=400, variable=slider1_var, command=sliders_callback)
slider1.pack(side="top",pady=5)

slider2_var = tk.IntVar()
slider2 = tk.Scale(sliders_frame, from_=1, to=100, orient="horizontal", label="confidance treshold", length=400, variable=slider2_var, command=sliders_callback)
slider2.pack(side="top",pady=5)

# checkboxs for controling parameters
checkbox_var = tk.IntVar()
checkbox = tk.Checkbutton(buttons_frame, text="draw circles", variable=checkbox_var)
checkbox.pack(side="left")

checkbox_var2 = tk.IntVar()
checkbox2 = tk.Checkbutton(buttons_frame, text="show count", variable=checkbox_var2)
checkbox2.pack(side="left",padx=10)


#some adjustments so interface looks a bit better
sliders_frame.pack(pady=15)
buttons_frame.pack(side='left',pady=5)
input_frame.pack(padx=10)


# Call the update function to start displaying the video
update()

# Run the Tkinter event loop
root.mainloop()

# Release the video capture object when the Tkinter window is closed
capture.release()