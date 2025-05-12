import faostat
from extract import extract_from_faostat
from transform import average_over_years
from load import write_dfs_to_excel

"""
Main script to extract, transform, and export FAOSTAT data to Excel.

Steps:
1. Extract maize and pesticide data for a defined set of countries and years.
2. Compute 5-year averages.
3. Save both raw and averaged datasets to an Excel workbook.
"""

def main():
    # Define the first search conditions
    database = 'QCL'
    countries = ["Brazil", "China", "India", "United States of America", "Russian Federation"]
    item_codes = ['56']
    element_codes = ['2312', '2413', '2510']
    nYears = 5
    years = sorted(faostat.get_par('QCL', 'years'))[-nYears:]

    # Extract the data from the FAO database
    maize_df = extract_from_faostat(database, countries, item_codes, element_codes, years)

    # Make an average over the data of all years in the current set (currently 5 years selected)
    maize_df_averaged = average_over_years(maize_df)

    # Define the second search conditions
    database = 'RP'
    countries = ["Brazil", "China", "India", "United States of America", "Russian Federation"]
    item_codes = ['1357']
    element_codes = ['5159']
    nYears = 5
    years = sorted(faostat.get_par('RP', 'years'))[-nYears:]

    # Extract the data from the FAO database
    pesticide_df = extract_from_faostat(database, countries, item_codes, element_codes, years)

    # Make an average over the data of all years in the current set (currently 5 years selected)
    pesticide_df_averaged = average_over_years(pesticide_df)

    df_dict = {
        'All_maize_data' : maize_df,
        'Averaged_maize_data' : maize_df_averaged,
        'All_pesticide_data' : pesticide_df,
        'Averaged_pesticide_data' : pesticide_df_averaged
    }

    write_dfs_to_excel(df_dict, path='output/assessment.xlsx')

if __name__ == '__main__':
    main()