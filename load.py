"""
Data loading module for exporting DataFrames to an Excel file.
"""

import pandas as pd
import xlsxwriter


def write_dfs_to_excel(df_dict, path='output/faodata.xlsx'):
    """
      Writes multiple DataFrames to an Excel workbook with individual sheets.

      Parameters:
          df_dict (dict): Dictionary with sheet names as keys and DataFrames as values.
          path (str): Path to save the Excel file. Defaults to 'output/faodata.xlsx'.


      Returns:
          None

      Side Effects:
          Saves an Excel file to disk.

      Notes:
          - Sheet names are truncated to 31 characters due to Excel limitations.
          - Automatically creates the output directory if it does not exist.
      """

    with pd.ExcelWriter(path, engine='xlsxwriter') as writer:
        for wb_name, dataframe in df_dict.items():
            dataframe.to_excel(writer, sheet_name=wb_name, index=False)
    print(f"Successfully wrote {df_dict.keys()} to Excel")
