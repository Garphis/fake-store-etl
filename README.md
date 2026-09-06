# 🛒 FakeStore E-Commerce ETL Pipeline

A production-ready, modular ETL (Extract, Transform, Load) pipeline built with Python, pandas, and PostgreSQL. This pipeline extracts raw e-commerce data (products and users) from a RESTful API, cleans and normalizes nested schemas, and loads structured relational data into a PostgreSQL instance.

---

## 🏗️ Architecture & Data Flow

```text
┌────────────────────┐
│  FakeStoreAPI      │
│  (REST endpoints)  │
└─────────┬──────────┘
          │ HTTP GET (JSON)
          ▼
┌────────────────────┐
│    1. EXTRACT      │ ➔ requests + status validation
└─────────┬──────────┘
          │ Raw DataFrames
          ▼
┌────────────────────┐
│   2. TRANSFORM     │ ➔ JSON flattening, type casting, schema renaming
└─────────┬──────────┘
          │ Clean DataFrames
          ▼
┌────────────────────┐
│     3. LOAD        │ ➔ SQLAlchemy engine with context manager
└─────────┬──────────┘
          │ SQL INSERT / Append
          ▼
┌────────────────────┐
│ PostgreSQL Storage │
│ (products & users) │
└────────────────────┘

🛠️ Tech Stack

    Language: Python 3

    Data Manipulation: pandas

    HTTP Client: requests

    Database / ORM: PostgreSQL, SQLAlchemy, psycopg2

    Environment Management: python-dotenv

🚀 Getting Started

    Prerequisites

    Python 3.10+

    PostgreSQL server running locally or remotely
