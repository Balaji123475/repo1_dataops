from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
import os

os.makedirs("output", exist_ok=True)

if __name__ == "__main__":
    df = extract_data()
    transformed_df = transform_data(df)
    load_data(transformed_df)

