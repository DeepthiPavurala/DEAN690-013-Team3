import os
import pandas as pd
from calendar import monthrange


# Function to check for leap year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Base folder where the files are saved
base_folder = "/Users/deepthipavurala/Documents/4th_Sem/Dataset/nClimGrid"

# Climate Indicators
variables = ["prcp", "tmin", "tmax", "tavg"]
columns = ['Type', 'Code', 'State_County', 'Year', 'Month', 'Variable'] + [f"Day_{i}" for i in range(1, 32)]

# Current year and month
current_year = 2024
current_month = 9


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

    # Step 2: Filter for VA and save
    if combined_data:
        all_data = pd.concat(combined_data, ignore_index=True)
        va_data = all_data[all_data['State'] == 'VA']

        # Save the combined VA data to a new CSV file
        output_file = os.path.join(base_folder, "combined_va_data.csv")
        va_data.to_csv(output_file, index=False)
        print(f"Combined VA data saved to {output_file}")
    else:
        print("No data found across the years.")


# Run the function
if __name__ == "__main__":
    combine_data_directly()
