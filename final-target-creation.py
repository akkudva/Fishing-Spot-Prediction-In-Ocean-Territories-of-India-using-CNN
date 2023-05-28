import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
# Path to the two folders
folder1_path = r"D:\datasets\fishing dataset\temp-dataset\dataset-256"
folder2_path = r"D:\datasets\fishing dataset\chl-dataset\dataset-256"
output_folder = r"D:\datasets\fishing dataset\final-target\target_dataset"

# Iterate over the two folders simultaneously using the zip function
for file1, file2 in zip(sorted(os.listdir(folder1_path)), sorted(os.listdir(folder2_path))):
    # Load the two images
        
        filename = file1 + file2
        img1 = cv2.imread(os.path.join(folder1_path, file1))
        img2 = cv2.imread(os.path.join(folder2_path, file2))

# Convert the images to HSV color space
        img1_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
        img2_hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

# Define the lower and upper thresholds for red color
        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])
        lower_red2 = np.array([170, 50, 50])
        upper_red2 = np.array([180, 255, 255])

# Define the lower and upper thresholds for green color
        lower_green = np.array([36, 25, 25])
        upper_green = np.array([70, 255, 255])

# Create a mask for red color in image 1
        mask1_red = cv2.inRange(img1_hsv, lower_red, upper_red)
        mask1_red2 = cv2.inRange(img1_hsv, lower_red2, upper_red2)
        mask1_red = cv2.bitwise_or(mask1_red, mask1_red2)

# Create a mask for green color in image 2
        mask2_green = cv2.inRange(img2_hsv, lower_green, upper_green)

# Find the overlapping regions and highlight them in the second image
        overlap = cv2.bitwise_and(mask1_red, mask2_green)
        output = np.ones_like(img2)*255  # Initialize output image with white color
        output[np.where(overlap > 0)] = (0, 0, 0)  # Update overlapping regions with green color

# Display the output image using matplotlib
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.axis('off')
        
        
#save 
        output_filename = os.path.join(output_folder, filename +".png")
        plt.imsave(output_filename, output)
        
# close the plot and the .nc file
        plt.close(fig)