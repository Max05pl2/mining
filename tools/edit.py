from PIL import Image, ImageChops, ImageEnhance

def edit_image(imagename, imageloc, tempfolder): 
    # MOVE IMAGE TO TEMP FOLDER

    img = Image.open(imageloc)
    img.save(tempfolder + imagename, 'JPEG')

    # CROP IMAGE
    width, height = img.size
    img.crop((0, height/1.5, width, height)).save(tempfolder + imagename, 'JPEG')

    # MONOCHROME
    img = Image.open(tempfolder + imagename)
    img = img.convert('L').save(tempfolder + imagename, 'JPEG')

    # BRIGHTNESS
    img = Image.open(tempfolder + imagename)
    im3 = ImageEnhance.Brightness(img) 
    im3.enhance(0.3).save(tempfolder + imagename, 'JPEG')

    # CONTRAST
    img = Image.open(tempfolder + imagename)
    im3 = ImageEnhance.Contrast(img) 
    im3.enhance(10).save(tempfolder + imagename, 'JPEG')

    # BRIGHTNESS
    img = Image.open(tempfolder + imagename)
    im3 = ImageEnhance.Brightness(img) 
    im3.enhance(0.5).save(tempfolder + imagename, 'JPEG')

    # INVERT
    img = Image.open(tempfolder + imagename)
    img = ImageChops.invert(img).save(tempfolder + imagename, 'JPEG')