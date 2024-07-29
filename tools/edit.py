from PIL import Image, ImageChops, ImageEnhance

def edit_image(image): 
    # MOVE IMAGE TO TEMP FOLDER
    img = Image.open('./screenshots/' + image)
    img.save('./temp/' + image, 'JPEG')


    # CROP IMAGE
    width, height = img.size
    img.crop((0, height/1.5, width, height)).save('./temp/' + image, 'JPEG')

    # MONOCHROME
    img = Image.open('./temp/' + image)
    img = img.convert('L').save('./temp/' + image, 'JPEG')

    # BRIGHTNESS
    img = Image.open('./temp/' + image)
    im3 = ImageEnhance.Brightness(img) 
    im3.enhance(0.3).save('./temp/' + image, 'JPEG')

    # CONTRAST
    img = Image.open('./temp/' + image)
    im3 = ImageEnhance.Contrast(img) 
    im3.enhance(10).save('./temp/' + image, 'JPEG')

    # BRIGHTNESS
    img = Image.open('./temp/' + image)
    im3 = ImageEnhance.Brightness(img) 
    im3.enhance(0.5).save('./temp/' + image, 'JPEG')

    # INVERT
    img = Image.open('./temp/' + image)
    img = ImageChops.invert(img).save('./temp/' + image, 'JPEG')

    # SHARPNESS
    #img = Image.open('./temp/' + image)
    #im3 = ImageEnhance.Sharpness(img) 
    #im3.enhance(7).save('./temp/' + image, 'JPEG')