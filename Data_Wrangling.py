import os
import requests

# Base URL for downloading the files
base_url = "https://www.ncei.noaa.gov/pub/data/daily-grids/v1-0-0/averages"

# Variables for which we want to download data
variables = ["prcp", "tmin", "tmax", "tavg"]

# Define the years and the months
start_year = 1990
end_year = 2024

# Base folder to store downloaded files
output_base_dir = "/Users/deepthipavurala/Documents/4th_Sem/Dataset/nClimGrid"

# Loop through each year
for year in range(start_year, end_year + 1):
    # Set the range of months, limit to 9 if the year is 2024
    months = range(1, 10) if year == 2024 else range(1, 13)

    # Loop through each variable (prcp, tmin, tmax, tavg)
    for var in variables:
        # Create the folder structure: year/variable/
        year_var_dir = os.path.join(output_base_dir, str(year), var)
        os.makedirs(year_var_dir, exist_ok=True)

        # Loop through each month
        for month in months:
            # Format the month as a two-digit number (e.g., 01 for January)
            month_str = f"{month:02d}"

            # Construct the file name
            file_name = f"{var}-{year}{month_str}-cty-scaled.csv"

            # Construct the full URL for downloading the file
            file_url = f"{base_url}/{year}/{file_name}"

            # Construct the local file path where the file will be saved
            local_file_path = os.path.join(year_var_dir, file_name)

            # Download the file
            print(f"Downloading {file_url}...")
            response = requests.get(file_url)

            # Check if the download was successful
            if response.status_code == 200:
                # Save the file
                with open(local_file_path, "wb") as file:
                    file.write(response.content)
                print(f"Saved to {local_file_path}")
            else:
                print(f"Failed to download {file_url} (Status code: {response.status_code})")
