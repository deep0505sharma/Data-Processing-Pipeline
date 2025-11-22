import pandas as pd
from my_pipeline.extract import extract_data
from my_pipeline.transform import transform_data
from my_pipeline.load import load_data
from pathlib import Path

def test_transform_data():
    data = {
    'Column A': [1, 2, None, 4, 5],
    'Column B': ['apple', 'banana', 'orange', None, 'grape'],
    'Column C': [10.1, None, 30.3, 40.4, 50.5]
    }

    # Create the DataFrame
    df = pd.DataFrame(data)
    result = transform_data(df)
    # Check that missing values are dropped
    assert result.isnull().sum().sum() == 0
    return result

