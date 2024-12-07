# Virginia Climate Indicators

We developed a user-friendly climate data dashboard tailored for practitioners in Virginia to support climate adaptation and resilience planning. The Virginia Climate Data Dashboard addresses the information challenges faced by municipal planners by offering a centralized platform to access and analyze historical and projected climate data. This tool equips planners with actionable insights to make informed decisions on climate adaptation and mitigation strategies.

The climate dashboard, built using data from NOAA’s National Centers for Environmental Information (NCEI), provides actionable insights into key climate indicators such as temperature, precipitation, and humidity from January 1990 to September 2024. Designed for flexibility, it allows users to filter by date range, season, and county, delivering customized visualizations that automatically update to support diverse planning needs. Key features include trends in maximum and minimum temperatures, annual precipitation totals, and extreme heat days, along with color-coded maps that highlight statistically significant patterns. 

Findings indicate that 2024 is on track to become the wettest year on record, surpassing 2018, while warming trends show a northward progression of extreme heat challenges. Notably, 2020 was Virginia’s second hottest year, but the highest number of extreme heat days occurred in 2010, especially in southern and central regions. By visualizing historical climate trends, the dashboard empowers urban planners, policymakers, and environmental organizations to assess vulnerabilities and develop resilience strategies. 

Future updates may incorporate predictive models, findings about vector borne diseases(disease resul ng from mosquito and ck bites) and additional indicators to further strengthen Virginia’s response to evolving climate risks.


Problem Context:
**Domain of problem:** Environmental Science, Public Health, Urban Planning

**IMPORTANCE OF THE PROBLEM:**
- Poor access to climate data hinders municipal planning, risking public health and environmental resilience.
- Ineffective use of climate data can lead to increased vulnerability to climate events
- Potential negative impacts on public health, and economic losses due to inadequate preparation and response strategies

Problem Statement: 
- Municipal planners in Virginia face significant challenges in accessing, interpreting, and utilizing climate data for local needs. 
- The data is often scattered across various sources, lacks county-specific detail, and is presented in complex formats. 
- This hinders planners' ability to make well-informed decisions, potentially compromising climate adaptation efforts, public health initiatives, and economic resilience in the face of changing environmental conditions

![image](https://github.com/user-attachments/assets/6c8c6937-3019-4d0b-bc94-a8ebdddf7068)


  
**SOLUTION PROPOSED:**
Our team proposed a strategic approach to ensure the successful development of the Virginia Climate Data Dashboard:  

1. **Building a Strong Foundation with Climate Data:**  
   We prioritized gaining a comprehensive understanding of climate data from diverse sources, formats, and analytical techniques. This in-depth knowledge guided us in selecting the most relevant data sources and types for collection, enabling efficient data cleaning and processing for the dashboard.  

2. **Streamlining Data Accessibility:**  
   Our approach simplifies the data acquisition process by consolidating information into a single platform, eliminating the need for planners to search across multiple sources.  

3. **Leveraging Clear and Interactive Visualizations:**  
   By implementing intuitive visual representations of historical climate data, we help users quickly grasp critical insights, empowering them to make informed, data-driven decisions.  

This solution equips municipal planners with the tools needed to effectively assess climate risks, strategize adaptation measures, and communicate their findings to communities with clarity and confidence.

# Architecture
![Architecture (2)](https://github.com/user-attachments/assets/c8c4d77b-1a07-4d88-aa16-b5e489a67c32)  

• Data extraction from NCEI source    
• Storage and management in local drive   
• Processing and preparation on PC    
• Dashboard creation in Tableau     
• End user access and interaction    

**Potential Analytic/Algorithm Name: Historical Climate Trend Analysis**

Datasets: 
Weather station records from NOAA
Focusing on temperature and precipitation extremes
Processed climate data, county-level geographical data.

Computer Resources Required: CPU with sufficient RAM for data processing; cloud resources for scalability..etc.

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

# Data Readiness Steps for Dashboard
![Data Analysis](https://github.com/user-attachments/assets/7463ca17-ea87-4951-b307-e33de6db079c)

The finalized dataset used for building the Tableau dashboard is too large to store directly in the repository. The dataset is available for download from [this S3 URL](https://gmu-cec-sagemaker-daen690-dw.s3.us-east-1.amazonaws.com/combined_va_data.csv)

## Workflow Summary for the Virginia Climate Data Dashboard  

1. **Data Collection and Extraction:**  
   - Climate data for Virginia counties was systematically collected from NOAA's NCEI, focusing on minimum, maximum, and average temperatures, along with precipitation data.  

2. **Data Cleaning and Preprocessing:**  
   - Missing values were removed, formatting issues were resolved, date formats were standardized, and unit conversions were completed to ensure consistency and usability.  

3. **Data Integration and Aggregation:**  
   - Temperature and precipitation datasets were merged, county-level data was combined into unified time series, and temporal and spatial alignment was achieved for comprehensive analysis.  

4. **Statistical Analysis:**  
   - Key analyses included calculating historical averages, assessing variability, identifying trends, validating significance using p-values, detecting extreme events, and analyzing seasonal patterns.  

5. **Visualization Development:**  
   - A range of visualizations was created, including time series plots, spatial heatmaps, county-level comparisons, seasonal patterns, and interactive charts for user exploration.  

6. **Final Dataset Preparation:**  
   - The workflow resulted in a clean, validated dataset optimized for Tableau dashboard implementation, designed for easy updates, and tailored to meet the needs of municipal planners for effective decision-making.
  

# Tableau Dashboard
[Virginia Climate Indicators](https://public.tableau.com/views/VirginiaClimateIndicators-2/VirginiaClimateIndicators?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)

**A snapshot of Whole State**: 

![Whole State](https://github.com/user-attachments/assets/b448b42f-8984-4b9d-8a02-305b994260c8)


### Key findings 

This highlights significant statewide warming, with average monthly temperatures increasing by 2.53°F. Minimum temperatures have risen faster at 3.29°F compared to maximum temperatures at 2.36°F, reflecting a narrowing temperature range. The frequency of extreme heat days, defined as days exceeding 90°F, has steadily increased, primarily in southern and central Virginia, with these patterns now spreading northward. Seasonal analyses reveal significant warming during summer and winter months, potentially impacting ecosystems, agriculture, energy consumption, and public health.  

Precipitation trends indicate a statewide increase of 7.65 inches; however, regional variability paints a more complex picture. Twelve counties, including Fairfax, Prince William, Manassas, and Manassas Park, face declining precipitation, raising concerns about drought and water scarcity. Meanwhile, other areas report intensified precipitation events, increasing flood risks and complicating stormwater management efforts. These trends underscore the growing urgency of addressing climate challenges, from heat-related health risks to managing water resources effectively. The data emphasizes the need for tailored adaptation and mitigation strategies to build climate resilience across Virginia’s diverse regions.

To conclude, by combining robust statistical analysis with interactive visualizations, the dashboard empowers policymakers and planners with actionable insights to address Virginia's evolving climate challenges effectively.

# Team Members
Deepthi Pavurala, Ashritha Gugire, Bhargava Devarakonda, Rishik Reddy Ragi, Adithya Karkata
