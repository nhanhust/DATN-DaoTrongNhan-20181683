import os
from PIL import Image

def resize_images(folder_path, new_width, new_height):
    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            # Open the image
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)

            # Resize the image
            resized_image = image.resize((new_width, new_height))

            # Save the resized image, overwrite the original file
            resized_image.save(image_path)

            # Close the image
            image.close()

# Example usage
folder_path = input("duong dan thu muc anh: ").strip()
# folder_path = "/path/to/folder"  # Replace with the path to your folder
new_width = 800  # Replace with the desired width
new_height = 600  # Replace with the desired height

resize_images(folder_path, new_width, new_height)
