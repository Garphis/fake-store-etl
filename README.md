# 🛒 FakeStore E-Commerce ETL Pipeline

A modular **ETL (Extract, Transform, Load)** pipeline built with **Python, pandas, and PostgreSQL**.

This project extracts product and user data from the **FakeStore API**, transforms and validates the data, and loads the cleaned datasets into PostgreSQL.

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │    FakeStore API    │
                    │    REST Endpoints   │
                    └──────────┬──────────┘
                               │
                            HTTP GET
                               │
                               ▼
                    ┌─────────────────────┐
                    │     extract.py      │
                    │                     │
                    │ • API requests      │
                    │ • HTTP validation   │
                    │ • Timeout handling  │
                    │ • Error handling    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    transform.py     │
                    │                     │
                    │ • Data cleaning     │
                    │ • JSON flattening   │
                    │ • Type conversion  │
                    │ • Data validation   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       load.py       │
                    │                     │
                    │ • SQLAlchemy        │
                    │ • PostgreSQL        │
                    │ • Data loading      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     PostgreSQL      │
                    │                     │
                    │ • products          │
                    │ • users             │
                    └─────────────────────┘

                         logger.py
                            │
                    ┌───────┴────────┐
                    ▼                ▼
                 Terminal         etl.log
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.10+** | ETL pipeline development |
| **pandas** | Data transformation and manipulation |
| **requests** | REST API requests |
| **PostgreSQL** | Relational database storage |
| **SQLAlchemy** | Database connection and data loading |
| **psycopg2** | PostgreSQL database driver |
| **python-dotenv** | Environment variable management |
| **logging** | Application logging |

---

## 📁 Project Structure

```text
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
```

> **Note:** `.env` contains database credentials and should never be committed to GitHub.

---

## 🔄 ETL Process

### 1. Extract

The `extract.py` module retrieves product and user data from the FakeStore API.

The extraction layer provides:

- HTTP status validation
- Connection timeout handling
- Read timeout handling
- Error logging
- Graceful failure handling

Requests use:

```python
timeout=(2, 5)
```

If an API request fails, the pipeline stops instead of processing incomplete data.

---

### 2. Transform & Validate

The `transform.py` module converts raw API responses into clean pandas DataFrames.

The transformation process includes:

- Flattening nested JSON objects
- Renaming columns
- Converting data types
- Removing invalid records
- Validating required fields

### Data Quality Rules

| Rule | Action |
|------|--------|
| Product price must be greater than `0` | Invalid records are dropped |
| Product ID cannot be null | Invalid records are removed |
| Product title cannot be null | Invalid records are removed |
| User ID cannot be null | Invalid records are removed |
| Malformed email address | Warning is logged |

Non-critical data-quality issues do not interrupt the entire pipeline.

---

### 3. Load

The `load.py` module loads the transformed DataFrames into PostgreSQL using SQLAlchemy.

The pipeline currently loads two tables:

- `products`
- `users`

The current loading strategy uses:

```python
if_exists="replace"
```

This means the existing tables are replaced with the latest successfully transformed dataset on each run.

---

## 🗄️ Database Tables

### Products

The `products` table contains:

| Column | Description |
|--------|-------------|
| `product_id` | Unique product identifier |
| `product_name` | Product name |
| `product_price` | Product price |
| `product_category` | Product category |
| `description` | Product description |

### Users

The `users` table contains:

| Column | Description |
|--------|-------------|
| `user_id` | Unique user identifier |
| `user_email` | User email address |
| `first_name` | User first name |
| `last_name` | User last name |
| `street` | Street address |
| `city` | City |
| `zipcode` | Postal code |

Nested fields from the API are flattened into relational database columns during transformation.

---

## ⚙️ Configuration

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=fakestore
DB_USER=postgres
DB_PASSWORD=your_password
```

> ⚠️ **Important:** Never commit `.env` to GitHub. Database credentials should remain private.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Garphis/fake-store-etl.git
cd fake-store-etl
```

### 2. Create a virtual environment

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create the database:

```sql
CREATE DATABASE fakestore;
```

Then update your `.env` file with your PostgreSQL credentials.

### 5. Run the pipeline

```bash
python main.py
```

---

## 📋 Logging

The pipeline uses Python's built-in `logging` module.

Logs are written to:

```text
etl.log
```

and displayed in the terminal.

### Example Output

```text
[2026-09-06 16:19:38] [INFO] === ETL PIPELINE STARTED ===
[2026-09-06 16:19:39] [INFO] Products extracted successfully. Total records: 20
[2026-09-06 16:19:40] [INFO] Users extracted successfully. Total records: 10
[2026-09-06 16:19:40] [INFO] === TRANSFORM STARTED ===
[2026-09-06 16:19:40] [INFO] Products prepared: 20 rows, 5 columns.
[2026-09-06 16:19:40] [INFO] Users prepared: 10 rows, 7 columns.
[2026-09-06 16:19:40] [INFO] === LOADING STARTED ===
[2026-09-06 16:19:40] [INFO] Loading 20 rows into 'products' table...
[2026-09-06 16:19:40] [INFO] Loading 10 rows into 'users' table...
[2026-09-06 16:19:40] [INFO] === ETL PIPELINE COMPLETED ===
```

---

## 🛡️ Error Handling

The pipeline is designed to fail safely when critical errors occur.

### API Failure

```text
API request fails
       │
       ▼
Error is logged
       │
       ▼
Pipeline stops
       │
       ▼
No incomplete data is loaded
```

### Data Quality Issue

```text
Invalid record detected
       │
       ▼
Warning is logged
       │
       ▼
Record is filtered
       │
       ▼
Pipeline continues
```

---

## 🔮 Future Improvements

Possible future improvements include:

- [ ] Add automated tests with `pytest`
- [ ] Add API retry logic with exponential backoff
- [ ] Implement database upserts
- [ ] Add incremental ETL processing
- [ ] Add Docker support
- [ ] Add CI/CD with GitHub Actions
- [ ] Add data-quality reporting
- [ ] Add database migrations
- [ ] Add ETL orchestration

---

## 👨‍💻 Author

**Garphis**

Built as a practical ETL project demonstrating:

- REST API ingestion
- Data transformation
- Data validation
- PostgreSQL integration
- Error handling
- Structured logging
- Modular Python development

