import pandas as pd

def extract_data():
    print("Extracting data...")
    data = {
        "date": ["2025-10-20", "2025-10-21", "2025-10-21"],
        "item": ["apple", "banana", "apple"],
        "quantity": [10, 5, 8],
        "price": [30, 10, 30]
    }
    df = pd.DataFrame(data)
    return df
