# ----------------------------
# 1️⃣  Base image
# ----------------------------
FROM python:3.9-slim

# ----------------------------
# 2️⃣  Working directory inside container
# ----------------------------
WORKDIR /app

# ----------------------------
# 3️⃣  Copy files from local → container
# ----------------------------
COPY . .

# ----------------------------
# 4️⃣  Install dependencies
# ----------------------------
RUN pip install --no-cache-dir -r requirements.txt

# ----------------------------
# 5️⃣  Default command to run ETL
# ----------------------------
CMD ["python", "main.py"]
