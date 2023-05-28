import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import os

# set the path to the folder containing the .nc files
input_folder = r"D:\datasets\fishing dataset\temp-dataset\nc\nc4"

# set the path to the folder where the images will be saved
output_folder = r"D:\datasets\fishing dataset\temp-dataset\dataset"

# set the minimum and maximum chlorophyll-a concentration values for the plot
level = (np.arange(24, 30.5, 0.5)).tolist()
max_temp = 24
min_temp= 30
# set the number of levels for the plot
n_levels = 20


# create the directory to save the images, if it doesn't already exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop over all the .nc files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.nc'):
        # open the .nc file
        ds = xr.open_dataset(os.path.join(input_folder, filename))

        # extract the chlorophyll-a concentration data
        temp = ds['sst']

        # extract the longitude and latitude coordinates
        lon = ds['lon']
        lat = ds['lat']

        # create a continuous contour plot of the chlorophyll-a concentration data
        levels = np.linspace(min_temp, max_temp, n_levels)
        fig, ax = plt.subplots(figsize=(10, 8))
        contour = ax.contourf(lon, lat, temp, levels=n_levels, cmap='viridis')
        ax.contour(lon, lat, temp, levels=level, colors='red')
        ax.axis('off')
        

        # save the plot as a PNG file in the output folder with the same name as the input file
        output_filename = os.path.join(output_folder, filename.replace('.nc', '.png'))
        fig.savefig(output_filename, dpi=300, bbox_inches='tight')
        
        # close the plot and the .nc file
        plt.close(fig)
        ds.close()