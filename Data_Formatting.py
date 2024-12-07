import os
import pandas as pd
from calendar import monthrange
from scipy import stats  # Importing scipy for statistical significance calculation


# Function to check for leap year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Base folder where the files are saved
base_folder = "/Users/deepthipavurala/Documents/4th_Sem/Dataset/nClimGrid"

# Climate Indicators
variables = ["prcp", "tmin", "tmax", "tavg"]
columns = ['Type', 'Code', 'State_County', 'Year', 'Month', 'Variable'] + [f"Day_{i}" for i in range(1, 32)]

# Current year and month
from datetime import datetime

# Get the current date
current_date = datetime.now()

# Extract the current year and month
current_year = current_date.year
current_month = current_date.month


# Step 1: Preprocess and directly combine data
def combine_data_directly():
    combined_data = []

    for year in range(1990, current_year + 1):
        print(f"Processing year: {year}")

        year_data = None

        for var in variables:
            folder_path = os.path.join(base_folder, str(year), var)
            if not os.path.exists(folder_path):
                continue

            var_data = []

            for file_name in os.listdir(folder_path):
                if file_name.endswith(".csv"):
                    file_path = os.path.join(folder_path, file_name)

                    # Load the CSV without headers
                    df = pd.read_csv(file_path, header=None, names=columns)
                    df[['State', 'County']] = df['State_County'].str.split(': ', expand=True)

                    new_rows = []
                    for idx, row in df.iterrows():
                        year = row['Year']
                        month = row['Month']

                        if year == current_year and month > current_month:
                            continue

                        num_days = monthrange(int(year), int(month))[1]

                        for day in range(1, num_days + 1):
                            date_str = f"{year:04d}-{month:02d}-{day:02d}"
                            daily_value = row[f"Day_{day}"]

                            # Prepare row for new DataFrame
                            new_row = {
                                'Date': date_str,
                                'State': row['State'],
                                'County': row['County'],
                                var: daily_value
                            }
                            new_rows.append(new_row)

                    var_df = pd.DataFrame(new_rows)
                    var_data.append(var_df)

            if var_data:
                var_data_df = pd.concat(var_data, ignore_index=True)

                # Merge with the existing year's data (on 'Date', 'State', 'County')
                if year_data is None:
                    year_data = var_data_df
                else:
                    year_data = pd.merge(year_data, var_data_df, on=['Date', 'State', 'County'], how='outer')

        # Add the year's combined data to the main list
        if year_data is not None:
            combined_data.append(year_data)

    # Step 2: Combine all years, filter for VA, rename columns
    if combined_data:
        all_data = pd.concat(combined_data, ignore_index=True)
        va_data = all_data[all_data['State'] == 'VA']

        # Rename columns to final names for easier reference later
        va_data = va_data.rename(columns={
            'tmin': 'Minimum Temperature (°F)',
            'tmax': 'Maximum Temperature (°F)',
            'tavg': 'Average Temperature (°F)',
            'prcp': 'Precipitation (inches)'
        })

        # Step 3: Clean data by removing placeholder values
        va_data = va_data[(va_data['Precipitation (inches)'] != -999.99) &
                          (va_data['Minimum Temperature (°F)'] != -999.99) &
                          (va_data['Maximum Temperature (°F)'] != -999.99) &
                          (va_data['Average Temperature (°F)'] != -999.99)]

        # Step 4: Convert Celsius to Fahrenheit and mm to inches for cleaned data
        va_data['Minimum Temperature (°F)'] = va_data['Minimum Temperature (°F)'] * 9/5 + 32
        va_data['Maximum Temperature (°F)'] = va_data['Maximum Temperature (°F)'] * 9/5 + 32
        va_data['Average Temperature (°F)'] = va_data['Average Temperature (°F)'] * 9/5 + 32
        va_data['Precipitation (inches)'] = va_data['Precipitation (inches)'] / 25.4  # Convert mm to inches

        # Convert Date column to datetime format and extract Year and Month if not already present
        va_data['Date'] = pd.to_datetime(va_data['Date'])
        if 'Year' not in va_data.columns or 'Month' not in va_data.columns:
            va_data['Year'] = va_data['Date'].dt.year
            va_data['Month'] = va_data['Date'].dt.month

        # Ensure no NaNs are present before statistical significance calculation
        va_data.dropna(subset=['Average Temperature (°F)', 'Precipitation (inches)'], inplace=True)

        va_data['Date'] = pd.to_datetime(va_data['Date'], errors='coerce')

        # Initialize new columns for slope, p-value, and significance
        va_data['Temp Slope'] = None
        va_data['Temp P-Value'] = None
        va_data['Significant Temp Trend'] = None
        va_data['Precip Slope'] = None
        va_data['Precip P-Value'] = None
        va_data['Significant Precip Trend'] = None

        # Calculate trends for each county
        for county, group in va_data.groupby('County'):
            # Sort by date to ensure time series is ordered
            group = group.sort_values(by='Date')

            # Get time values (e.g., year) and the variable of interest
            time_values = group['Date'].dt.year
            avg_temp = group['Average Temperature (°F)']
            precip = group['Precipitation (inches)']

            # Calculate trend (slope, p-value) for Average Temperature
            slope_temp, intercept_temp, r_value_temp, p_value_temp, std_err_temp = stats.linregress(time_values,
                                                                                                    avg_temp)

            # Calculate trend (slope, p-value) for Precipitation
            slope_precip, intercept_precip, r_value_precip, p_value_precip, std_err_precip = stats.linregress(
                time_values, precip)

            # Check if trends are statistically significant (p-value < 0.05)
            significant_temp_trend = p_value_temp < 0.05
            significant_precip_trend = p_value_precip < 0.05

            # Assign values back to the original DataFrame for this county
            va_data.loc[va_data['County'] == county, 'Temp Slope'] = slope_temp
            va_data.loc[va_data['County'] == county, 'Temp P-Value'] = p_value_temp
            va_data.loc[va_data['County'] == county, 'Significant Temp Trend'] = significant_temp_trend
            va_data.loc[va_data['County'] == county, 'Precip Slope'] = slope_precip
            va_data.loc[va_data['County'] == county, 'Precip P-Value'] = p_value_precip
            va_data.loc[va_data['County'] == county, 'Significant Precip Trend'] = significant_precip_trend

        # Save the combined VA data to a new CSV file
        output_file = os.path.join(base_folder, "combined_va_data.csv")
        va_data.to_csv(output_file, index=False)
        print(f"Combined VA data saved to {output_file}")
    else:
        print("No data found across the years.")


# Run the function
if __name__ == "__main__":
    combine_data_directly()

