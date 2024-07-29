from tools import edit, ocr, savetofile
import os
from pathlib import Path


os.makedirs('./temp', exist_ok=True) 
os.makedirs('./screenshots', exist_ok=True) 

paths = sorted(Path("./screenshots").iterdir(), key=os.path.getmtime)
file_names = [os.path.basename(path) for path in paths]

if os.path.isfile("./credentials.json"):
    print("Cloud Vision API Credentials found.")
else:
    print('ERROR: Cloud Vision API credentials not found. This software requires a Google Cloud Platform project with the Cloud Vision API enabled and a service account key file (JSON format) to function correctly. Please obtain the necessary credentials and place the JSON file, named "credentials.json" in the same directory this Python file is located in. Without valid credentials, the software will be unable to perform any image analysis tasks.')
    exit()

for imagename in file_names:
    # crop the image and make it black and white for better OCR recognition.
    edit.edit_image(imagename)

    # OCR the image 
    text = ocr.ocr('./temp/' + imagename)

    imagepath = "<img src='" + imagename +"'>"
    formated = imagepath + ";" + text + "\n"

    # Save the formated text to the txt file
    savetofile.save_to_file("./sentences.txt", formated)

    # Delete the file in the temp folder
    os.remove("./temp/" + imagename)