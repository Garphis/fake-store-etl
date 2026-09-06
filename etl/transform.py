import pandas as pd
from etl.logger import logger

def transform_product(product_df):
    df = product_df.copy()

    df = df.rename(columns={
        'id': 'product_id',
        'title': 'product_name',
        'price': 'product_price',
        'category': 'product_category',
        'description': 'description'
    })

    df = df[[
        'product_id', 'product_name', 'product_price', 'product_category', 'description'
    ]]

    df['product_price'] = df['product_price'].astype(float)

    invalid_prices = df[df['product_price'] <= 0]
    if not invalid_prices.empty:
        logger.warning(f"Found {len(invalid_prices)} products with invalid price (<= 0). Filtering them out.")
        df = df[df['product_price'] > 0]

    null_rows = df[df['product_id'].isna() | df['product_name'].isna()]
    if not null_rows.empty:
        logger.warning(f"Found {len(null_rows)} products with missing ID or name. Dropping them.")
        df = df.dropna(subset=['product_id', 'product_name'])

    logger.info(f"Products prepared: {df.shape[0]} rows, {df.shape[1]} columns.")
    return df

def transform_users(users_df):
    df = users_df.copy()

    df['first_name'] = df['name'].apply(lambda x: x['firstname'])
    df['last_name'] = df['name'].apply(lambda x: x['lastname'])

    df['street'] = df['address'].apply(lambda x: x['street'])
    df['city'] = df['address'].apply(lambda x: x['city'])
    df['zipcode'] = df['address'].apply(lambda x: x['zipcode'])

    df = df.rename(columns={
        'id': 'user_id',
        'email': 'user_email'
    })

    df = df[[
        'user_id', 'user_email', 'first_name', 'last_name', 'street', 'city', 'zipcode'
    ]]

    invalid_emails = df[~df['user_email'].str.contains('@', na=False)]
    if not invalid_emails.empty:
        logger.warning(f"Found {len(invalid_emails)} users with invalid email format.")

    logger.info(f"Users prepared: {df.shape[0]} rows, {df.shape[1]} columns.")
    return df