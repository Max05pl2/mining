# **vn-to-anki**

This software is designed to assist Japanese learners who utilize visual novels. It automates the process of extracting Japanese text from visual novel screenshots, processing it, and preparing it for import into Anki flashcards.

## **How it works:**

Image Optimization: Screenshots are preprocessed to enhance text clarity.
OCR: Google Cloud Vision API is used to extract text from the optimized images.
Output: Extracted text is saved in a .txt file, ready for Anki import.

## **Output:**
<img src="https://t.vndb.org/sf/99/137699.jpg" width="400">

```
image;text
```
```
<img src='408776.jpg'>;那有多「なんで私なのよ・・・・・ 葛がいるじゃない?」
```

## **Prerequisites:**

- Google Cloud Platform account: To use the Google Cloud Vision API.
- Service account credentials: A JSON file containing your service account credentials.

**PLEASE NOTE: The Cloud Vision API is not free. However, you can use it to process up to 1000 images per month at no cost.**

Packages:
- pillow
- google-cloud-vision

## **Usage:**

Run the script for the first time to create the necessary folders.

1. Place your screeshots in the "screenshots" folder.
2. Run the script

Output will be in sentences.txt
