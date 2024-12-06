import os
import requests
from datetime import datetime

# Base URL for downloading the files
base_url = "https://www.ncei.noaa.gov/pub/data/daily-grids/v1-0-0/averages"

# Variables for which we want to download data
variables = ["prcp", "tmin", "tmax", "tavg"]

# Get the current date
current_date = datetime.now()

# Extract the current year and month
end_year = current_date.year
current_month = current_date.month

start_year = 1990


# Base folder to store downloaded files
output_base_dir = "/Users/deepthipavurala/Documents/4th_Sem/Dataset/nClimGrid"

# Loop through each year
for year in range(start_year, end_year + 1):
    months = range(1, current_month+1) if year == end_year else range(1, 13)

    for var in variables:
        year_var_dir = os.path.join(output_base_dir, str(year), var)
        os.makedirs(year_var_dir, exist_ok=True)

        for month in months:
            month_str = f"{month:02d}"

            file_name = f"{var}-{year}{month_str}-cty-scaled.csv"

            file_url = f"{base_url}/{year}/{file_name}"

            local_file_path = os.path.join(year_var_dir, file_name)

            print(f"Downloading {file_url}...")
            response = requests.get(file_url)

            if response.status_code == 200:
                # Save the file
                with open(local_file_path, "wb") as file:
                    file.write(response.content)
                print(f"Saved to {local_file_path}")
            else:
                print(f"Failed to download {file_url} (Status code: {response.status_code})")
