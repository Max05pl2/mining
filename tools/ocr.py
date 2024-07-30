from google.cloud import vision
import os

def ocr(path, credentials):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    
    response = client.document_text_detection(
    image=image,
    image_context={"language_hints": ["ja"]}, 
    ) 
    texts = response.text_annotations
        
    if response.error.message:
        raise Exception('{}\nFor more info on error messages, check: https://cloud.google.com/apis/design/errors'.format(response.error.message))

    try:
        text = (texts[0].description).replace('\n', '')
        text1 = text.replace('▼', '')
        return (text1)
    except:
        return ("No Text found!")
