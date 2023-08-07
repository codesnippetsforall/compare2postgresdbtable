import sqlalchemy
import pandas as pd

# Database connection details for source and target PostgreSQL databases
source_db_name = "payroll_dev"
source_user = "USERNAME"
source_password = "PASSWORD"
source_host = "HOST"  # Default is "localhost"
source_port = "PORT"  # Default is "5432"

target_db_name = "payroll_qa"
target_user = "USERNAME"
target_password = "PASSWORD"
target_host = "HOST"  # Default is "localhost"
target_port = "PORT"  # Default is "5432"

# Function to fetch list of tables from a database
def get_table_list(engine):
    inspector = sqlalchemy.inspect(engine)
    return inspector.get_table_names()

# Create SQLAlchemy engine for source and target databases
source_engine = sqlalchemy.create_engine(
    f"postgresql://{source_user}:{source_password}@{source_host}:{source_port}/{source_db_name}"
)

# Function to fetch data from a table and return a DataFrame
def fetch_data(engine, table):
    query = f"SELECT * FROM {table}"
    with engine.connect() as conn:
        data = pd.read_sql(query, con=conn)
    return data

target_engine = sqlalchemy.create_engine(
    f"postgresql://{target_user}:{target_password}@{target_host}:{target_port}/{target_db_name}"
)

# Fetch list of tables from source and target databases
source_tables = get_table_list(source_engine)
target_tables = get_table_list(target_engine)

# Compare data for each table
for table in source_tables:
    source_data = fetch_data(source_engine, table)
    target_data = fetch_data(target_engine, table)

    if source_data.equals(target_data):
        print(f"Table '{table}' has the same data in both databases.")
    else:
        print(f"Table '{table}' has different data in the databases.")
