from etl.extract import extract_product,extract_users
from etl.transform import transform_product,transform_users
from etl.load import load_to_postgres
from etl.logger import logger

def run_pipeline():
    logger.info("=== ETL PIPELINE BASLATILDI ===")

    product_df = extract_product()
    user_df = extract_users()

    logger.info("=== TRANSFORM BASLATILDI ===")

    product_df = transform_product(product_df)
    user_df = transform_users(user_df)

    logger.info("=== LOADİNG BASLATILDI ===")

    load_to_postgres(product_df, 'products')
    load_to_postgres(user_df, 'users')

    logger.info("=== ETL PIPELINE SONLANDI ===")

if __name__ == '__main__':
    run_pipeline()