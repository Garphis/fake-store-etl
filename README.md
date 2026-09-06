Markdown

# 🛒 FakeStore E-Commerce ETL Pipeline

A modular ETL (Extract, Transform, Load) pipeline built with Python, pandas, and PostgreSQL.

The project extracts product and user data from the FakeStore API, transforms and validates the data, and loads the cleaned datasets into PostgreSQL.

---

## 🏗️ Architecture

```text
┌────────────────────┐
│   FakeStore API    │
│   REST Endpoints   │
└─────────┬──────────┘
          │
          │ HTTP GET
          ▼
┌────────────────────┐
│    extract.py      │
│                    │
│  API requests      │
│  HTTP validation   │
│  Timeout handling  │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│   transform.py     │
│                    │
│  Data cleaning     │
│  JSON flattening   │
│  Type conversion   │
│  Data validation   │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│      load.py       │
│                    │
│  SQLAlchemy        │
│  PostgreSQL        │
│  Data loading      │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│    PostgreSQL      │
│                    │
│  products          │
│  users             │
└────────────────────┘

       logger.py
          │
          ├──► Terminal
          └──► etl.log

🛠️ Tech Stack

    Python 3.10+

    pandas — data transformation and manipulation

    requests — API requests

    PostgreSQL — relational database storage

    SQLAlchemy — database connection and loading

    psycopg2 — PostgreSQL driver

    python-dotenv — environment variable management

    logging — application logging

📁 Project Structure
Plaintext

fake-store-etl/
│
├── etl/
│   ├── extract.py        # Extracts data from the FakeStore API
│   ├── transform.py      # Cleans and validates API data
│   ├── load.py           # Loads data into PostgreSQL
│   └── logger.py         # Logging configuration
│
├── main.py               # Main ETL pipeline entry point
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (git-ignored)
├── .gitignore            # Git ignore rules
├── etl.log               # Pipeline logs
└── README.md             # Project documentation

🔄 ETL Process
1. Extract

extract.py retrieves product and user data from the FakeStore API.

The extraction process includes:

    HTTP status validation

    Connection timeout

    Read timeout

    Error logging

    Graceful failure handling

Requests use a timeout of:
Python

timeout=(2, 5)

If an API request fails, the pipeline stops rather than processing incomplete data.
2. Transform & Validate

transform.py converts the raw API responses into clean pandas DataFrames.

The transformation process includes:

    Flattening nested JSON objects

    Renaming columns

    Converting data types

    Removing invalid records

    Validating required fields

Data quality rules include:

    Product price must be greater than 0 (invalid prices dropped)

    Product ID cannot be null

    Product title cannot be null

    User ID cannot be null

    Malformed email addresses generate warnings without interrupting pipeline flow

3. Load

load.py loads the transformed DataFrames into PostgreSQL using SQLAlchemy.

The pipeline currently loads two datasets:

    products

    users

The current loading strategy replaces the existing tables during each successful run (if_exists='replace').
🗄️ Database Tables
Products

The products table contains:

    product_id

    product_name

    product_price

    product_category

    description

Users

The users table contains:

    user_id

    user_email

    first_name

    last_name

    street

    city

    zipcode

Nested fields from the API are flattened into relational columns.
⚙️ Configuration

Create a .env file in the project root:
Kod snippet'i

DB_HOST=localhost
DB_PORT=5432
DB_NAME=fakestore
DB_USER=postgres
DB_PASSWORD=your_password

    Important: Never commit .env to GitHub. Database credentials should remain private.

🚀 Installation
1. Clone the repository
Bash

git clone [https://github.com/Garphis/fake-store-etl.git](https://github.com/Garphis/fake-store-etl.git)
cd fake-store-etl

2. Create a virtual environment

Linux/macOS:
Bash

python3 -m venv venv
source venv/bin/activate

Windows:
DOS

python -m venv venv
venv\Scripts\activate

3. Install dependencies
Bash

pip install -r requirements.txt

4. Configure PostgreSQL

Create a PostgreSQL database:
SQL

CREATE DATABASE fakestore;

Then update your .env file with your database credentials.
5. Run the pipeline
Bash

python main.py

📋 Logging

The pipeline uses Python's built-in logging module. Logs are displayed in the terminal and saved to etl.log:
Plaintext

[2026-09-06 16:19:38] [INFO]: === ETL PIPELINE STARTED ===
[2026-09-06 16:19:39] [INFO]: Products extracted successfully. Total records: 20
[2026-09-06 16:19:40] [INFO]: Users extracted successfully. Total records: 10
[2026-09-06 16:19:40] [INFO]: === TRANSFORM STARTED ===
[2026-09-06 16:19:40] [INFO]: Products prepared: 20 rows, 5 columns.
[2026-09-06 16:19:40] [INFO]: Users prepared: 10 rows, 7 columns.
[2026-09-06 16:19:40] [INFO]: === LOADİNG STARTED ===
[2026-09-06 16:19:40] [INFO]: Loading 20 rows into 'products' table...
[2026-09-06 16:19:40] [INFO]: Loading 10 rows into 'users' table...
[2026-09-06 16:19:40] [INFO]: === ETL PIPELINE OVER ===

🛡️ Error Handling

The pipeline is designed to handle failures gracefully:
Plaintext

API request fails
       ↓
Error is logged
       ↓
Pipeline stops
       ↓
No incomplete data is loaded

For non-critical data-quality issues:
Plaintext

Invalid record detected
       ↓
Warning is logged
       ↓
Record filtered or flagged
       ↓
Pipeline continues

👨‍💻 Author

Garphis

Built as a practical ETL project demonstrating API ingestion, data transformation, validation, logging, and PostgreSQL integration.
