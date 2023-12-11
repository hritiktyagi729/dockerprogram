import os
import sys
import time
import pytesseract
from PIL import Image

def perform_ocr(image_path):
    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(Image.open(image_path))

    # Print the OCR result
    print(text)

def ocr_folder(folder_path):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Calculate the time for OCR
    start_time = time.time()

    # Process each image in the folder
    for file_name in file_list:
        # Get the full path of the image file
        image_path = os.path.join(folder_path, file_name)
        
        # Print the image name before OCR
        print(f"Processing image: {file_name}")

        # Perform OCR on the image
        perform_ocr(image_path)

    # Calculate and print the total time taken for OCR
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken for OCR: {total_time:.2f} seconds")

if __name__ == "__main__":
    # Check if a folder path argument is provided
    #if len(sys.argv) != 2:
    #    print("Usage: python ocr_script.py <folder_path>")
    #    sys.exit(1)

    # Get the folder path from the command-line argument
    #folder_path = sys.argv[1]
    folder_path = input("Enter the folder path:")

    # Call the OCR function with the provided folder path
    ocr_folder(folder_path)

