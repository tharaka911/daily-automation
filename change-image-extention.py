from PIL import Image
import os

# Input and output folder paths
input_folder = "C:/Users/lakshan/Desktop/eshop-images/"
output_folder = "C:/Users/lakshan/Desktop/ok/"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# List all files in the input folder
files = os.listdir(input_folder)

# Iterate through the files
for file in files:
    # Check if the file has a supported image extension (e.g., jpg, jpeg, gif, bmp, etc.)
    if file.lower().endswith((".jpg",".webp", ".jpeg", ".gif", ".bmp", ".tiff", ".ico")):
        try:
            # Open the image file
            image = Image.open(os.path.join(input_folder, file))
            
            # Convert and save it as PNG in the output folder
            output_file = os.path.splitext(file)[0] + ".png"
            image.save(os.path.join(output_folder, output_file), "PNG")
            
            print(f"Converted: {file} -> {output_file}")
        except Exception as e:
            print(f"Failed to convert {file}: {str(e)}")

print("Conversion complete.")
