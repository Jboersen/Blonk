import pandas as pd
from load import write_dfs_to_excel

def test_write_dfs_to_excel(tmp_path):
    df = pd.DataFrame({'A': [1, 2]})
    df_dict = {'Sheet1': df}
    output_file = tmp_path / "test_output.xlsx"

    write_dfs_to_excel(df_dict, path=str(tmp_path) + '/', name='test_output.xlsx')
    assert output_file.exists()