def load_data(df):
    print("Loading data...")
    df.to_csv("output/sales_summary.csv", index=False)
    print("Data loaded to output/sales_summary.csv")

