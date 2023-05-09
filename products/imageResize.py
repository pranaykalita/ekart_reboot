from PIL import Image

def resize_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    ratio = 1

    if img.height > 500 or img.width > 500:
        ratio = min(500 / width, 500 / height)
    elif img.height < 500 or img.width < 500:
        ratio = 1

    new_width = round(width * ratio)
    new_height = round(height * ratio)

    # resize the image
    img = img.resize((new_width, new_height), Image.ANTIALIAS)

    # create a new image with the target size, centered on a black background
    background = Image.new('RGBA', (500, 500), (0, 0, 0, 255))
    x = (500 - new_width) // 2
    y = (500 - new_height) // 2
    background.paste(img, (x, y))

    return img
