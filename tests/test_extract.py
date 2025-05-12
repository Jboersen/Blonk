import pytest
from extract import extract_from_faostat
from unittest.mock import patch

@patch('extract.faostat.get_par')
@patch('extract.faostat.get_data_df')
def test_extract_from_faostat_invalid_country(mock_get_data_df, mock_get_par):
    # Mock return values
    mock_get_par.side_effect = lambda db, key: {
        'area': {'Brazil': 1, 'India': 2},
        'item': {'Maize': '56'},
        'element': {'Production': '2312'},
        'year': {'2020': 2020, '2021': 2021}
    }[key]

    mock_get_data_df.return_value = 'FAKE_DF'

    # Attempt to extract with an invalid country
    with pytest.raises(KeyError, match="country Atlantis is not in FAOSTAT database"):
        extract_from_faostat(
            database='QCL',
            countries=['Brazil', 'Atlantis'],  # "Atlantis" is not valid
            item_codes=['56'],
            element_codes=['2312'],
            years=['2020', '2021']
        )