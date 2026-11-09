from PIL import Image, ImageOps, ImageDraw
import math

def main():
    lego_colors = {
        "White": (242, 243, 242),
        "Black": (27, 42, 52),
        "Red": (196, 40, 28),
        "Blue": (13, 105, 172),
        "Yellow": (245, 205, 47),
        "Green": (40, 127, 71),
        "Orange": (218, 133, 65),
        "Light Gray": (160, 165, 169),
        "Dark Gray": (99, 95, 98),
        "Brown": (88, 57, 39),
        "Tan": (228, 205, 158),
        "Pink": (255, 152, 195),
        "Purple": (129, 0, 123),
        "Light Blue": (180, 210, 227),
    }
    
     
    # image = "LEGO_Pictures/mj-dunk.jpeg"
    print("== Choose an image by typing A, B, C, or D ==")
    image1 = "A"
    image2 = "B"
    image3 = "C"
    image4 = "D"
    image = " "
    choice = input("Image: ").upper()
    if choice == image1:
        image = "LEGO_Pictures/mj-dunk.jpeg"
    elif choice == image2:
        image = "LEGO_Pictures/river-brayden-garret.jpg"
    elif choice == image3:
        image = "LEGO_Pictures/dog.jpg"
    elif choice == image4:
        image = "LEGO_Pictures/lake-powell.jpg"
    

    resized_image = load_image_from_file(image, 100)

    lego_matrix = create_lego_matrix(resized_image, lego_colors, 100)

    lego_image = create_lego_image(lego_matrix, lego_colors, 50)

    lego_image.show()

    count_legos = count_lego_colors(lego_matrix)

    display_color_totals(count_legos)

    total_legos = count_blocks(count_legos)

    print(f"Total number of LEGO blocks needed: {total_legos}")

    #Milestone requirements:
        #pixel_rgb = resized_image.getpixel((10, 10))
   
        # print(pixel_rgb)

        # print(color_distance(pixel_rgb, lego_colors["White"]))
        # print(find_lego_color(pixel_rgb, lego_colors))

def display_color_totals(count_legos):
    print("Parts List:")
    for color, count in count_legos.items():
        print(f"-{color}: {count}")

def count_lego_colors(lego_matrix):
    count = {}
    for row in lego_matrix:
        for color_name in row:
            if color_name in count:
                count[color_name] += 1
            else:
                count[color_name] = 1
    return count

def count_blocks(lego_count_dict):
    total = 0
    for count in lego_count_dict.values():
        total = total + count

    return total
        


def create_lego_matrix(resized_image, lego_colors, size):
    lego_matrix = [] 
    for row_index in range(size):
        row = []
        for column_index in range(size):
            pixel_rgb = resized_image.getpixel((column_index, row_index))
            color_name = find_lego_color(pixel_rgb, lego_colors)
            row.append(color_name)
        lego_matrix.append(row)
    return lego_matrix


def color_distance(rgb1, rgb2):

    distance = math.sqrt(((rgb2[0] - rgb1[0])**2) + ((rgb2[1] - rgb1[1])**2) + ((rgb2[2] - rgb1[2])**2))

    return round(distance, 3)

def find_lego_color(rgb, colors):
    closest_name = None
    smallest_distance = float("inf")
    for name, lego_rgb in colors.items():
        distance = color_distance(rgb, lego_rgb)

        if distance < smallest_distance:
            closest_name = name
            smallest_distance = distance

    return closest_name


def load_image_from_file(image_path, desired_width_and_height=100):
    """
    Loads an image from a file, resizes it, and returns it as a PIL Image object.

    Params:
        image_path: The path to the image file to load.
        desired_width_and_height: The desired width and height of the image (default is 100).
    """
    image = Image.open(image_path)
    resized_image = ImageOps.fit(image, (desired_width_and_height, desired_width_and_height), method=Image.Resampling.BOX)
    return resized_image


def create_lego_image(lego_matrix, colors, block_size_pixels=50):
    """
    Create a new PIL Image object representing the LEGO design.
    Each LEGO block is represented as a square with a circle (stud) in the center.
    The width and height of the image are determined by the number of blocks in the design and the size of each block.

    Params:
        lego_matrix: A 2D list of color names representing the LEGO design.
        colors: A dictionary mapping color names to RGB tuples.
        block_size_pixels (optional): The size of each LEGO block in pixels.
    Returns:
        A new PIL Image object representing the LEGO mosaic.
    """
    LEGO_BRICK_BORDER_COLOR = (0, 0, 0)  # Dark color for the LEGO brick borders
    OUTLINE_WIDTH = 3  # Width of the outline for the LEGO blocks

    # Determine the dimensions of the LEGO design
    height = len(lego_matrix)
    width = len(lego_matrix[0]) if height > 0 else 0

    # Determine the dimensions of the output image based on the number of blocks and the size of each block
    image_width = width * block_size_pixels
    image_height = height * block_size_pixels

    lego_image = Image.new("RGB", (image_width, image_height))
    image_draw_obj = ImageDraw.Draw(lego_image)

    for block_y in range(height):
        for block_x in range(width):
            # Get the color of the current LEGO block
            color_name = lego_matrix[block_y][block_x]

            # Get the RGB tuple for the LEGO block color from the colors dictionary
            lego_rgb_tuple = colors[color_name]

            draw_lego_block(image_draw_obj, block_x, block_y, block_size_pixels, lego_rgb_tuple)

    return lego_image

def draw_lego_block(image_draw_obj, block_x, block_y, block_size_pixels, color_rgb_tuple):
    """
    Draw a single LEGO block at the specified position in the scaled image.

    Params:
        image_draw_obj: A PIL ImageDraw object used to draw on the image.
        block_x: The x-coordinate of the block in the LEGO design.
        block_y: The y-coordinate of the block in the LEGO design.
        block_size_pixels: The size of each LEGO block in pixels.
        color_rgb_tuple: The RGB color tuple for the LEGO block.
    """
    LEGO_BRICK_BORDER_COLOR = (0, 0, 0)  # Dark color for the LEGO brick borders
    OUTLINE_WIDTH = 3  # Width of the outline for the LEGO blocks

    # Top-left corner of the block in the scaled image
    left = block_x * block_size_pixels
    top = block_y * block_size_pixels
    right = left + block_size_pixels - 1
    bottom = top + block_size_pixels - 1

    # Square of the LEGO block color
    image_draw_obj.rectangle([left, top, right, bottom], fill=color_rgb_tuple, outline=LEGO_BRICK_BORDER_COLOR, width=OUTLINE_WIDTH)

    # Circle (stud) centered in the square
    center_x = left + block_size_pixels / 2
    center_y = top + block_size_pixels / 2
    radius = block_size_pixels / 4

    # Add a small lower-right shadow behind the stud. This makes the
    # circle look raised while keeping the mosaic's pixel-art style.
    stud_shadow = tuple(max(channel - 45, 0) for channel in color_rgb_tuple)
    image_draw_obj.ellipse(
        [center_x - radius + 2, center_y - radius + 2,
         center_x + radius + 2, center_y + radius + 2],
        fill=stud_shadow)

    # The lighter fill and thin outline suggest the top surface of
    # the raised LEGO stud.
    stud_highlight = tuple(min(channel + 25, 255) for channel in color_rgb_tuple)
    stud_box = [center_x - radius, center_y - radius,
                center_x + radius, center_y + radius]
    
    image_draw_obj.ellipse(
        stud_box,
        fill=stud_highlight,
        outline=LEGO_BRICK_BORDER_COLOR,
        width=OUTLINE_WIDTH)

    # A short highlight on the upper-left edge reinforces the light
    image_draw_obj.arc(stud_box, start=180, end=270, fill=(255, 255, 255), width=2)





# TO DO - 
# Create LEGO Matrix to put extracted pixels from find_lego_color()
# Use draw_LEGO_block() using matrix
# Save as PNG
# Count list of colors using a for loop and store them in a dictionary
# Get two other photos from friends and make them mosaics



main()