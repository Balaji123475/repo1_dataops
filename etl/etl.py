import boto3
import os
import pandas as pd

# AWS S3 details
bucket = os.environ.get("S3_BUCKET")
input_file = "input/data.csv"
output_file = "output/transformed.csv"

s3 = boto3.client("s3")

# Download file from S3
s3.download_file(bucket, "incoming/data.csv", input_file)

# Process data
df = pd.read_csv(input_file)
df["Total"] = df["Quantity"] * df["Price"]
df.to_csv(output_file, index=False)

# Upload processed file back to S3
s3.upload_file(output_file, bucket, "processed/transformed.csv")

print("ETL completed successfully!")
