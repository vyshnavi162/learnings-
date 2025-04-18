from PIL import Image, ImageEnhance, ImageFilter

# Ask the user for the image path
image_path = input("Enter the path to your image file: ")

# Open the image
try:
    image = Image.open(image_path)
    print("Image loaded successfully!")
except FileNotFoundError:
    print("Error: File not found. Please check the file path and try again.")
    exit()

# Display the original image
image.show()

# Apply some edits
edited_image = image.filter(ImageFilter.CONTOUR)  # Add contour filter
enhancer = ImageEnhance.Brightness(edited_image)  
bright_image = enhancer.enhance(1.5)  # Brighten the image

# Save the edited images
edited_image.save("edited_image.jpg")
bright_image.save("bright_image.jpg")

print("Edited images have been saved as 'edited_image.jpg' and 'bright_image.jpg'.")
bright_image.show()


