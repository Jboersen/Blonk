"""
Data transformation module for processing and aggregating FAOSTAT datasets.
"""

import pandas as pd

def average_over_years(df):
    """
       Computes the average 'Value' over all years in the provided DataFrame.

       Parameters:
           df (pd.DataFrame): FAOSTAT data containing at least the columns:
                              'Area', 'Item', 'Element', 'Year', 'Value'.

       Returns:
           pd.DataFrame: A DataFrame grouped by 'Area', 'Item', and 'Element',
                         with the mean of 'Value' over all years.
   """

    df['Year'] = pd.to_numeric(df['Year'], errors='raise')
    df['Value'] = pd.to_numeric(df['Value'], errors='raise')

    # Compute average over the years
    avg_df = (
        df.groupby(['Area', 'Item', 'Element'], as_index=False)
          .agg({'Value': 'mean'})
    )

    return avg_df