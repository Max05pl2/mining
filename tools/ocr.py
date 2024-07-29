from google.cloud import vision

import os
# Replace 'YOUR_SERVICE_ACCOUNT_KEY.json' with the actual path to your service account key.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./credentials.json"

from google.cloud import vision

def ocr(path):
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    context = vision.ImageContext(language_hints="ja")
    response = client.document_text_detection(image=image)
    
    response = client.document_text_detection(
    image=image,
    image_context={"language_hints": ["ja"]}, 
    ) 
    texts = response.text_annotations
        
    if response.error.message:
        raise Exception('{}\nFor more info on error messages, check: https://cloud.google.com/apis/design/errors'.format(response.error.message))

    text = (texts[0].description).replace('\n', '')
    text1 = text.replace('▼', '')
    return (text1)
