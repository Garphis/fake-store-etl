import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from etl.logger import logger

load_dotenv()

host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

def load_to_postgres(df, table_name):

    logger.info(f"Loading {len(df)} rows into '{table_name}' table...")

    with engine.connect() as conn:
        df.to_sql(
            table_name,
            conn,
            if_exists='replace',
            index=False
        )