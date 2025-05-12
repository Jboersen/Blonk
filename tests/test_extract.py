import pytest
from unittest.mock import patch
from extract import extract_from_faostat

@patch('extract.faostat.get_par')
@patch('extract.faostat.get_data_df')
def test_extract_from_faostat(mock_get_data_df, mock_get_par):
    mock_get_par.side_effect = lambda db, key: {
        'area': {'Brazil': 1, 'India': 2},
        'item': {'56': 'Maize'},
        'element': {'2312': 'Production'},
        'year': {'2020': 2020, '2021': 2021}
    }[key]

    mock_get_data_df.return_value = 'FAKE_DF'

    result = extract_from_faostat(
        database='QCL',
        countries=['Brazil', 'India'],
        item_codes=['56'],
        element_codes=['2312'],
        years=['2020', '2021']
    )

    assert result == 'FAKE_DF'