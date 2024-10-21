# Virginia Climate Indicators

The Virginia Climate Data Dashboard aims to bridge the information gap faced by municipal planners in the state. By providing a centralized platform for accessing and analyzing historical and projected climate data, the dashboard empowers planners to make informed decisions regarding climate adaptation and mitigation.

The dashboard leverages advanced data visualization techniques to present climate indicators, such as temperature, precipitation, and humidity, in a clear and actionable manner. This enables planners to identify climate risks, assess vulnerabilities, and develop effective strategies to protect their communities from the impacts of climate change.


Problem Context:
**Domain of problem:** Environmental Science, Public Health, Urban Planning

**Importance of problem:**
- Poor access to climate data hinders municipal planning, risking public health and environmental resilience.
- Ineffective use of climate data can lead to increased vulnerability to climate events
- Potential negative impacts on public health, and economic losses due to inadequate preparation and response strategies

Problem Statement: 
- Municipal planners in Virginia face significant challenges in accessing, interpreting, and utilizing climate data for local needs. 
- The data is often scattered across various sources, lacks county-specific detail, and is presented in complex formats. 
- This hinders planners' ability to make well-informed decisions, potentially compromising climate adaptation efforts, public health initiatives, and economic resilience in the face of changing environmental conditions

**Potential Analytic/Algorithm Name: Historical Climate Trend Analysis**

Datasets: 
Weather station records from NOAA
Focusing on temperature and precipitation extremes
Processed climate data, county-level geographical data.

Computer Resources Required: CPU with sufficient RAM for data processing; cloud resources for scalability..etc.

Training:  If using machine learning models for projections 

Optimization: 
Feature selection for relevant climate indicators
Efficient data processing techniques for large datasets
Efficient rendering techniques for interactive visualizations

Testing: Validation against historical extreme weather records.

# Files

**Data_Wrangling.py:**<br>
Automates downloading of climate data from NOAA's nClimGrid repository.<br>
Iterates over years, months, and variables (precipitation, Tmin, Tmax, Tavg).<br>
Saves data locally in a structured format, organized by year and variable.<br>

**Data_Formatting.py:**<br>
Processes and combines daily climate data from multiple CSV files.<br>
Creates unified Date column and splits state/county information.<br>
Filters data for Virginia and outputs a combined CSV for further analysis.<br>

# Data Flow

<img width="1306" alt="Architecture" src="https://github.com/user-attachments/assets/a1f6fb34-304b-4a94-839c-a919ee89dc52">



# Team Members
Deepthi Pavurala, Ashritha Gugire, Bhargava Devarakonda, Rishi Reddy Ragi, Adithya Karkata
