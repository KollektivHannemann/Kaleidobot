from PIL import Image, ImageDraw, ImageEnhance


def mirror(img):
    # load the image, create the mirrored image, and the result placeholder
    img    = Image.open('img.png')
    mirror = img.transpose(Image.FLIP_LEFT_RIGHT)
    sz     = max(img.size + mirror.size)
    result = Image.new(img.mode, (sz,sz))
    result.paste(img, (0,0)+img.size)
    
    # now paste the mirrored image, but with a triangular binary mask
    mask = Image.new('1', mirror.size)
    draw = ImageDraw.Draw(mask)
    draw.rectangle([0,0,(sz/2),sz], outline='white', fill='white')
    result.paste(mirror, (0,0)+mirror.size, mask)
    
    # clean up and save the result
    del mirror, mask, draw
    result.save('img.png')
    print("--- Mirroring horizontal")
    
    
    
    # load the image, create the mirrored image, and the result placeholder
    img2    = Image.open('img.png')
    mirror2 = img2.transpose(Image.FLIP_TOP_BOTTOM)
    sz2     = max(img2.size + mirror2.size)
    result2 = Image.new(img2.mode, (sz2,sz2))
    result2.paste(img2, (0,0)+img2.size)
    
    # now paste the mirrored image, but with a triangular binary mask
    mask2 = Image.new('1', mirror2.size)
    draw2 = ImageDraw.Draw(mask2)
    draw2.rectangle([0,(sz2/2),sz2 ,sz2], outline='white', fill='white')
    result2.paste(mirror2, (0,0)+mirror2.size, mask2)
    
    # clean up and save the result
    del mirror2, mask2, draw2
    result2.save('img.png')
    print("--- Mirroring vertical")
    
    
    
    # load the image, create the mirrored image, and the result placeholder
    img3    = Image.open('img.png')
    mirror3 = img3.transpose(Image.FLIP_LEFT_RIGHT)
    sz3     = max(img3.size + mirror3.size)
    result3 = Image.new(img3.mode, (sz3,sz3))
    result3.paste(img3, (0,0)+img3.size)
    
    # now paste the mirrored image, but with a triangular binary mask
    mask3 = Image.new('1', mirror3.size)
    draw3 = ImageDraw.Draw(mask3)
    draw3.rectangle([(sz3/2),0, sz3, sz3], outline='white', fill='white')
    result3.paste(mirror3, (0,0)+mirror3.size, mask3)
	
    
    # clean up and save the result
    del mirror3, mask3, draw3
    result3.save('img.png')
    print("--- Finishing mirroring")
    print("---")
	
	

def saturation(img):
	img = Image.open('img.png')
	satu = ImageEnhance.Color(img)
	img2 = satu.enhance(1.3)
	print("--- Upped the saturation")
	img2.save('img.png')