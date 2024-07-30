from tools import edit, ocr, savetofile
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from pathlib import Path

# Create the Root Frame
root = tk.Tk()
root.title("Visual Novel OCR")
root.resizable(False, False)
root.geometry('450x200')

# Top Label
label = tk.Label(root, text = 'Select the necessary files and press "Start".')
label.pack(fill="x", padx=5, pady=5)

# Function to insert text into a text box
def insert_textbox(text_box, text):
    text_box.config(state=tk.NORMAL) 
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, text)
    text_box.config(state=tk.DISABLED) 

# Function that opens the window to select a file
def select_file(text_box):
    filetypes = (('JSON files', '*.json'),('All files', '*.*'))
    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    insert_textbox(text_box, filename)

# Function that opens the window to select a directory
def select_directory(text_box):
    directory = filedialog.askdirectory(
        title='Open directory',
        initialdir='/',)
    insert_textbox(text_box, directory)

# Function to create a frame with a label, text box and a browse button
def create_innerframe(text, cmd):
  frame = ttk.Frame(root)
  frame.pack()
  label = tk.Label(frame, text=text)
  label.pack(side='left')
  text_box = tk.Text(frame, height=1, width=30, state="disabled")
  text_box.pack(side='left')
  button = ttk.Button(frame, text='Browse', command=lambda: cmd(text_box))
  button.pack(expand=True)
  return text_box

# Create 3 inner labels for each files necessery to select
credentialsbox = create_innerframe("Cloud Vision API JSON:", select_file)
imagesbox = create_innerframe("Select image directory:", select_directory)
outputbox = create_innerframe("Select output location:", select_directory)

# Lower Label that shows how many images have been processed
progresslabel = tk.Label(root, text = '')
progresslabel.pack()

# Function to start the OCR script
def start_ocr():
    filesdone = 0

    # Get the paths from the text-boxes
    outputfolder = outputbox.get("1.0", "end-1c")
    imagesfolder = imagesbox.get("1.0", "end-1c")
    credentialsfile = credentialsbox.get("1.0", "end-1c")
    tempfolder = imagesfolder + '/temp/'

    if os.path.exists(outputfolder) == False: 
        print("Error: Invalid output folder!")
        return False
    if os.path.exists(imagesfolder) == False:
        print("Error: Invalid images folder!")
        return False
    if os.path.isfile(credentialsfile) == False:
        print("Error: Invalid credentials file!")
        return False

    # Make the temp folder
    os.makedirs(tempfolder, exist_ok=True) 
    # Create the output txt
    with open(outputfolder + '/outputsentences.txt', 'w') as fp:
        pass

    paths = sorted(Path(imagesfolder).iterdir(), key=os.path.getmtime)
    file_names = [os.path.basename(path) for path in paths]

    for imagename in file_names:
        try:
            edit.edit_image(imagename, imagesfolder + '/' + imagename, tempfolder)
            text = ocr.ocr(imagesfolder + '/' + imagename, credentialsfile)
            savetofile.save_to_file(outputfolder + "/outputsentences.txt", text + "\n")
            os.remove(tempfolder + imagename)
            filesdone = filesdone + 1
            progresslabel.config(text = "Files processed: " + str(filesdone))
        except:
            print("This is not an image.")

# Lower start button
button = ttk.Button(root, text='Start', command=start_ocr)
button.pack(expand=True)

root.mainloop()