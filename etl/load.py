import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

def load_to_postgres(df, table_name):
    with engine.connect() as conn:
        df.to_sql(
            table_name,
            conn,
            if_exists='append',
            index=False
        )
    print(f"Data loaded to {table_name} table successfully.")