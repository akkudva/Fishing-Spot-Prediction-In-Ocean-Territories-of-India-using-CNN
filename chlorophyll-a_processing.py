import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import os


# Load netcdf file
input_folder = r"D:\datasets\fishing dataset\chl-dataset\nc6"
output_folder = r"D:\datasets\fishing dataset\chl-dataset\dataset"


if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# Select chlorophyll concentration data and convert to ug/L
min_chol = 1
max_chol=5
n_levels=20
level = np.arange(1, 6)


for filename in os.listdir(input_folder):
    if filename.endswith('.nc'):
        # open the .nc file
        ds = xr.open_dataset(os.path.join(input_folder, filename))
        chol = ds['chlor_a']
        lon = ds['lon']
        lat = ds['lat']
        levels = np.linspace(min_chol, max_chol, n_levels)
        fig, ax = plt.subplots(figsize=(10, 8))
        contour = ax.contourf(lon, lat, chol, levels=level, cmap='viridis')
        ax.contour(lon, lat, chol, levels=level, colors='green')
        ax.axis('off')

        output_filename = os.path.join(output_folder, filename.replace('.nc', '.png'))
        dpi = 256 / fig.get_size_inches()[1]  # calculate DPI based on height of figure
        fig.savefig(output_filename, dpi=300, bbox_inches='tight')
        
        # close the plot and the .nc file
        plt.close(fig)
        ds.close()