from pdf2image import convert_from_path 
from tkinter import *
from tkinter import messagebox 
import pdfsplitter

from tkinter import filedialog
from tkinter import *

def browse_input():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global input_pdf_path
    filename = filedialog.askopenfilename()
    input_pdf_path.set(filename)
    print(filename)

def browse_output():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global output_folder_path
    filename = filedialog.askdirectory()
    output_folder_path.set(filename)
    print(filename)

def pdf2img(): 
    try: 
        images = convert_from_path(str(e2.get())) 
        for img in images: 
            img.save('new_folder\output.jpg', 'JPEG') 
  
    except  : 
        Result = "NO pdf found"
        messagebox.showinfo("Result", Result) 
  
    else: 
        Result = "success"
        messagebox.showinfo("Result", Result) 
  
  
  
def runner():
    # print(output_folder_path.get())
    # print(input_pdf_path.get())
    pdfsplitter.split_pdf(input_pdf_path.get(), output_folder_path.get())



root = Tk()

# // Select input folder path
input_pdf_path = StringVar()
Label(root, text="Consolidated PDF (each pg has multiple images sep. by white border):").grid(row=0, column=0, sticky=W)  

input_pdf_label = Label(master=root,textvariable=input_pdf_path)
input_pdf_label.grid(row=0, column=1)
input_browse_button = Button(text="Browse", command=browse_input)
input_browse_button.grid(row=0, column=2)


# // Select output
output_folder_path = StringVar()
Label(root, text="Output images to: ").grid(row=1, column=0, sticky=W)

output_folder_label = Label(master=root,textvariable=output_folder_path)
output_folder_label.grid(row=1, column=1)
output_browse_button = Button(text="Browse", command=browse_output)
output_browse_button.grid(row=1, column=2)


# // Autocrop button
autocrop_button = Button(text="Autocrop", command=runner)
autocrop_button.grid(row=3, column=1)

mainloop()






# master = Tk() 


# # // Convert to image
# Label(master, text="Main PDF Location").grid(row=1, sticky=W)  
  
# e2 = Entry(master) 
# e2.grid(row=1, column=1) 
  
# # b = Button(master, text="2. Convert folder to images", command=pdf2img) 
# b = Button(master, text="2. Convert folder to images", command=test) 

# b.grid(row=1, column=2,columnspan=2, rowspan=2,padx=5, pady=5) 

# mainloop()