def transform_data(df):
    print("Transforming data...")
    df['total'] = df['quantity'] * df['price']
    result = df.groupby('item')['total'].sum().reset_index()
    return result