from PIL import Image

from resizeimage import resizeimage

with open('mydata/raw.png', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [256, 256])
        cover.save('mydata/girl.png', image.format)


