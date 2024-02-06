# Preamble
import zipfile
from PIL import Image
import numpy as np
import io
import os

# Change_directory folder
os.chdir('D:/Dokumenter/DTU/3_år/MatModel/Project1')
  
def zip_to_numpy(zip_file_path):
    # Open the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Get the list of file names in the zip file
        file_names = zip_ref.namelist()

        # Initialize an empty list to store image data
        image_data_list = []

        # Iterate through each file in the zip file
        for file_name in file_names:
            # Check if the file is a PNG file
            if file_name.lower().endswith('.png'):
                # Read the PNG file from the zip file
                with zip_ref.open(file_name) as file:
                    # Open the PNG file using PIL
                    img = Image.open(file)

                    # Convert the PIL image to a numpy array
                    img_array = np.array(img)

                    # Append the numpy array to the list
                    image_data_list.append(img_array)

    if not image_data_list:
        print("No PNG files found in the zip file.")
        return None

    # Convert the list of image data to a single numpy array
    image_data_array = np.stack(image_data_list)

    return image_data_array

# Change Directory of the zip file
zip_file_path = r'D:\Dokumenter\DTU\3_år\MatModel\Project1\toyProblem_F22.zip'
result_array = zip_to_numpy(zip_file_path)

#########################
# Problem 1
#########################

import matplotlib.pyplot as plt 

for i in range(len(result_array)): 
    plt.cla() 
    plt.title('Slå Johan! \n\n Window {}'.format(i), fontweight ="bold") 
    plt.imshow(result_array[i]) 
    plt.pause(0.01) 


#########################
# Problem 3
#########################

# Functio to convert pixels into vectors

def convert_pixels_to_coordinates(image):
    height, width, _ = image.shape

    coordinates = []
    for y in range(height):
        for x in range(width):
            coordinates.append((x, y))

    return np.array(coordinates)

 
# Loop over each picture in the array to get an array of coordinates.
for idx, picture in enumerate(result_array):
    coordinates = convert_pixels_to_coordinates(picture)
    print(f"Coordinates for Picture {idx + 1}:\n{coordinates}\n")


# Random A- Matrix, bcs I did not do Part 2. Please insert right matrix later
# Matrix dimensions [256, 2], just like eq (2). From the notes.

MatrixA = np.random.random((256, 2))

# Transpose the matrix (If you need, I need in this case)
A_transposed = np.transpose(MatrixA)

# Solve the least squares problem Ax = b
x, residuals, rank, s = np.linalg.lstsq(A_transposed, coordinates, rcond=None)

print("Least Squares Solution (x):")
print(x)
print("\nResiduals:")
print(residuals)
