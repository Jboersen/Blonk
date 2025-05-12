import pandas as pd
from transform import average_over_years

def test_average_over_years():
    df = pd.DataFrame({
        'Area': ['Brazil', 'Brazil', 'India'],
        'Item': ['Maize', 'Maize', 'Maize'],
        'Element': ['Production', 'Production', 'Production'],
        'Year': ['2020', '2021', '2020'],
        'Value': ['100', '200', '300']
    })

    result = average_over_years(df)

    assert len(result) == 2
    assert round(result[result['Area'] == 'Brazil']['Value'].iloc[0], 1) == 150.0
    assert round(result[result['Area'] == 'India']['Value'].iloc[0], 1) == 300.0