from PIL import Image
import pathlib
import os
import sys
OUTPUT_QUALITY = 100

def open_image(image_path: str) -> Image:
    """Open an image file and return a PIL Image object"""
    try:
        return Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return None

def overlay_image(png_image: Image, jpg_image: Image) -> Image:
    """Overlay a PNG image onto a JPG image"""
    jpg_width, jpg_height = jpg_image.size
    png_width, png_height = png_image.size

    '''Poner la marca de agua a la mitad'''
    """x = (jpg_width - png_width) //2
    y = (jpg_height - png_height) //2"""
    '''Ponerla abajo a la derecha'''

    x = (jpg_width - png_width)
    y = (jpg_height - png_height)

    jpg_image.paste(png_image, (x, y), png_image)
    return jpg_image

def save_image(image: Image, output_path: str) -> None:
    """Save an image to a file"""
    try:
        image.save(output_path, quality=OUTPUT_QUALITY)
    except Exception as e:
        print(f"Error saving image: {e}")

def load_images(jpg_image_folder: str) -> list[Image]:
    """Load all JPG images from a folder"""
    jpg_image_paths = list(pathlib.Path(jpg_image_folder).glob("*.jpg"))
    jpg_images = [open_image(str(path)) for path in jpg_image_paths]
    return jpg_images

def overlay_images(png_image_path: str, jpg_image_folder: str, output_folder: str) -> None:
    """Overlay a PNG image onto multiple JPG images from a folder and save the output"""
    png_image = open_image(png_image_path)
    if png_image is None:
        return

    output_folder_path = pathlib.Path(output_folder)
    output_folder_path.mkdir(parents=True, exist_ok=True)

    jpg_images = load_images(jpg_image_folder)

    for jpg_image in jpg_images:
        if jpg_image is None:
            continue

        output_image = overlay_image(png_image, jpg_image)
        output_path = output_folder_path / jpg_image.filename
        save_image(output_image, str(output_path))


png_image_path = 'water.png'
jpg_image_folder = 'photos'
output_folder = 'output'

overlay_images(png_image_path, jpg_image_folder, output_folder)