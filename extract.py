"""
Data extraction module for retrieving structured data from the FAOSTAT API.
"""

import faostat
import pandas as pd

def extract_from_faostat(database, countries, item_codes, element_codes, years):
    """
        Extracts FAOSTAT data for given parameters.

        Parameters:
            database (str): FAOSTAT database code (e.g., 'QCL', 'RP').
            countries (list): List of country names (as strings).
            item_codes (list): List of item codes (as strings).
            element_codes (list): List of element codes (as strings).
            years (list): List of years (as strings or integers).

        Returns:
            pd.DataFrame: A DataFrame containing the raw FAOSTAT data.

        Raises:
            KeyError: If any country, item, element, or year is not found in the FAOSTAT metadata.
    """

    # Check if countries are in the country-list of the FAO
    country_dict = faostat.get_par(database , 'area')
    countryIds = []
    for country in countries:
        if country in country_dict:
            countryIds.append(country_dict[country])
        else:
            raise KeyError(f'country {country} is not in FAOSTAT database or spelled incorrectly')

    for item_code in item_codes:
        if item_code not in faostat.get_par(database, 'item').values():
            raise KeyError(f'item code {item_code} is not in FAOSTAT database')

    for element_code in element_codes:
        if element_code not in faostat.get_par(database, 'element').values():
            raise KeyError(f'element code {element_code} is not in FAOSTAT database')

    for year in years:
        if year not in faostat.get_par(database, 'year'):
            raise KeyError(f'year {year} is not in FAOSTAT database')

    parameters = {'area': countryIds,
                    'item': item_codes,
                    'element': element_codes,
                    'year': years}

    df = faostat.get_data_df(database, pars=parameters, strval=True, show_flags=True, null_values=False, show_notes=True)
    return df



