"""Module for generating Binary Cards resource."""

import os.path
from PIL import Image, ImageDraw, ImageFont


def resource_image(task, resource_manager):
    """Create a image for Binary Cards resource.

    Args:
        task: Dicitionary of requested document options.
        resource_manager: File loader for external resources.

    Returns:
        A list of Pillow image objects.
    """
    BASE_IMAGE_PATH = "img/resources/binary-cards/"
    IMAGE_SIZE_X = 2480
    IMAGE_SIZE_Y = 3508
    IMAGE_DATA = [
        ("binary-cards-1-dot.png", 1),
        ("binary-cards-2-dots.png", 2),
        ("binary-cards-4-dots.png", 4),
        ("binary-cards-8-dots.png", 8),
        ("binary-cards-16-dots.png", 16),
        ("binary-cards-32-dots.png", 32),
        ("binary-cards-64-dots.png", 64),
        ("binary-cards-128-dots.png", 128),
    ]

    # Retrieve parameters
    display_numbers = task["display_numbers"]
    black_back = task["black_back"]

    if display_numbers:
        font_path = "fonts/PatrickHand-Regular.ttf"
        local_font_path = resource_manager.get_path(font_path)
        font = ImageFont.truetype(local_font_path, 600)
        BASE_COORD_X = IMAGE_SIZE_X / 2
        BASE_COORD_Y = IMAGE_SIZE_Y - 100
        IMAGE_SIZE_Y = IMAGE_SIZE_Y + 300

    images = []

    for (image_path, number) in IMAGE_DATA:
        data = resource_manager.load(os.path.join(BASE_IMAGE_PATH, image_path))
        image = Image.open(data)
        if display_numbers:
            background = Image.new("RGB", (IMAGE_SIZE_X, IMAGE_SIZE_Y), "#FFF")
            background.paste(image, mask=image)
            draw = ImageDraw.Draw(background)
            text = str(number)
            text_width, text_height = draw.textsize(text, font=font)
            coord_x = BASE_COORD_X - (text_width / 2)
            coord_y = BASE_COORD_Y - (text_height / 2)
            draw.text(
                (coord_x, coord_y),
                text,
                font=font,
                fill="#000"
            )
            image = background
        images.append(image)

        if black_back:
            black_card = Image.new("1", (IMAGE_SIZE_X, IMAGE_SIZE_Y))
            images.append(black_card)

    return images


def subtitle(task):
    """Return the subtitle string of the resource.

    Used after the resource name in the filename, and
    also on the resource image.

    Args:
        task: Dicitionary of requested document.

    Returns:
        text for subtitle (string)
    """
    if task["display_numbers"]:
        display_numbers_text = "with numbers"
    else:
        display_numbers_text = "without numbers"

    if task["black_back"]:
        black_back_text = "with black back"
    else:
        black_back_text = "without black back"

    text = "{} - {} - {}".format(
        display_numbers_text,
        black_back_text,
        task["paper_size"]
    )
    return text


def valid_options():
    """Provide dictionary of all valid parameters.

    This excludes the header text parameter.

    Returns:
        All valid options (dict).
    """
    return {
        "display_numbers": [True, False],
        "black_back": [True, False],
        "paper_size": ["a4", "letter"],
    }
