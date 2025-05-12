import pandas as pd
from load import write_dfs_to_excel

import pandas as pd
from load import write_dfs_to_excel


def test_write_dfs_to_excel(tmp_path):
    # Arrange
    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df2 = pd.DataFrame({'X': [9, 8], 'Y': [7, 6]})
    df_dict = {'Sheet1': df1, 'Sheet2': df2}

    output_file = tmp_path / "test_output.xlsx"

    # Act
    write_dfs_to_excel(df_dict, path=str(output_file))

    # Assert
    assert output_file.exists()