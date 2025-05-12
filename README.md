# FAO Data Analysis Project

This project extracts, transforms, and analyzes agricultural and environmental data from the FAOSTAT database. It focuses on maize production and pesticide usage across selected countries and outputs the results into a structured Excel workbook.

## Overview

The pipeline performs the following steps:
- Extracts maize and pesticide data from FAOSTAT for Brazil, China, India, United States of America, and Russian Federation.
- Filters the last 5 years of available data.
- Averages relevant indicators over those years.
- Saves both raw and processed data to a single Excel file with separate sheets.

## Project Structure

Blonk/
├── main.py                 # Main script to orchestrate the ETL process  
├── extract.py              # Contains function to extract data from FAOSTAT  
├── transform.py            # Contains function to average data over years  
├── load.py                 # Contains function to write dataframes to Excel  
├── requirements.txt        # Project dependencies  
├── .gitignore              # Git exclusions  
└── README.md               # Project documentation

## Usage

Run the pipeline with:  
python main.py

This will create an Excel file (`assessment.xlsx`) containing:
- All_maize_data  
- Averaged_maize_data  
- All_pesticide_data  
- Averaged_pesticide_data

## Testing

Tests can be added using pytest. To run them:  
pytest
