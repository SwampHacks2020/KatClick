import argparse
import io
import os
import json

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw, ImageOps

#Resolution to scale Instagram images: 1080 x 1080

def get_crop_hint(path):
    """Detect crop hints on a single image and return the first result."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    #Getting bounds from localizedObjectAnnotations
    image = vision.types.Image(content=content)
    objects = client.object_localization(image=image).localized_object_annotations

    #Check if image contains a cat
    isCat = False
    for object_ in objects:
        if object_.name == 'Cat':
            isCat = True
            vertices = object_.bounding_poly.normalized_vertices

    #If image doesn't contain a cat, return False
    if isCat is False:
        return False

    #Get resolution of image
    im = Image.open(path)
    width, height = im.size

    #Change normalized vertices to regular coordinates
    for vertex in vertices:
        vertex.x = vertex.x * width
        vertex.y = vertex.y * height

    return vertices

def crop_to_hint(path):
    """Crop the image using the hints in the vector list."""
    #Get normalized vertices
    vects = get_crop_hint(path)
    if vects is False:
        print('Invalid image')
        return

    #Crop image based on vertices 
    im = Image.open(path)
    im2 = im.crop([vects[0].x, vects[0].y,
                  vects[2].x - 1, vects[2].y - 1])
    
    return im2

def draw_hint(path):
    #Get coordinates of cropped image or return false
    vects = get_crop_hint(path)
    if vects is False:
        print('Invalid image')
        return

    #Crop original image and upscale to 1080 x 1080
    im2 = crop_to_hint(path)
    size = (256, 256)
    im3 = ImageOps.fit(im2, size, Image.ANTIALIAS)

    #Creating new naming convention
    filename = os.path.basename(path)
    filename = filename.replace(".jpg", "_CROP.jpg")
    print("images/" + filename)
    im3.save("images/" + filename, 'JPEG')
    print('Image edit successful')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='The image you\'d like to crop.')
    args = parser.parse_args()

    draw_hint(args.path)