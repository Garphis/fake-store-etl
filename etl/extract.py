import pandas as pd
import requests
from etl.logger import logger

BASE_URL = 'https://fakestoreapi.com'

def extract_product():
    url = f'{BASE_URL}/products'

    try: 
        response = requests.get(url, timeout=(1, 1))
        response.raise_for_status()

        data = response.json()
        product_df = pd.DataFrame(data)

        logger.info(f"Products extracted successfully. Total records: {len(data)}")
        return product_df

    except Exception as e:
        logger.error(f"Failed to extract products: {e}")
        return None

def extract_users():
    url = f'{BASE_URL}/users'

    try:
        response = requests.get(url, timeout=(1, 1))
        response.raise_for_status()

        data = response.json()
        users_df = pd.DataFrame(data)

        logger.info(f"Users extracted successfully. Total records: {len(data)}")
        return users_df

    except Exception as e:
        logger.error(f"Failed to extract users: {e}")
        return None