from etl.extract import extract_product,extract_users
from etl.transform import transform_product,transform_users
from etl.load import load_to_postgres
from etl.logger import logger

def run_pipeline():
    logger.info("=== ETL PIPELINE STARTED ===")

    product_df = extract_product()
    user_df = extract_users()

    if product_df is None or user_df is None:
        logger.error("Pipeline aborted due to extraction failure.")
        return

    logger.info("=== TRANSFORM STARTED ===")

    product_df = transform_product(product_df)
    user_df = transform_users(user_df)

    logger.info("=== LOADİNG STARTED ===")

    load_to_postgres(product_df, 'products')
    load_to_postgres(user_df, 'users')

    logger.info("=== ETL PIPELINE OVER ===")

if __name__ == '__main__':
    run_pipeline()