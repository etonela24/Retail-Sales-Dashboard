import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("retail_sales.db")
cursor = conn.cursor()

# Ensure the table exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_data (
        sale_id INTEGER PRIMARY KEY,
        product_name TEXT,
        category TEXT,
        sale_date DATE,
        quantity_sold INTEGER,
        unit_price DECIMAL(10,2),
        total_sales DECIMAL(10,2)
    )
""")

# Extract data
query = "SELECT * FROM sales_data"
df = pd.read_sql(query, conn)

# Convert sale_date to datetime format
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Add calculated fields
df['revenue_per_product'] = df['quantity_sold'] * df['unit_price']
df['profit_margin'] = df['revenue_per_product'] * 0.2  # Assuming a 20% profit margin

# Save cleaned data for Power BI
df.to_csv("cleaned_sales_data.csv", index=False)

# Close database connection
conn.close()

print("Data extraction and transformation complete!")
print(df.head())