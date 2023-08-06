import pandas as pd
from sqlalchemy import create_engine

# Define database connection URLs
# source_url = "postgresql://source_user:source_password@source_host/source_database"
source_url = "postgresql://USERNAME:PASSWORD@HOST/payroll_dev"

# target_url = "postgresql://target_user:target_password@target_host/target_database"
target_url = "postgresql://USERNAME:PASSWORD@HOST/payroll_qa"

# Define the tables to compare
source_table = "employee"
target_table = "employee"

# Create SQLAlchemy engine
source_engine = create_engine(source_url)
target_engine = create_engine(target_url)

# Fetch data from the tables
source_query = f"SELECT * FROM {source_table}"
source_data = pd.read_sql(source_query, con=source_engine)

target_query = f"SELECT * FROM {target_table}"
target_data = pd.read_sql(target_query, con=target_engine)

# Compare the dataframes
if source_data.equals(target_data):
    print("Tables have the same data.")
else:
    print("Tables have different data.")
