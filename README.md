# ⚡ ETL Project - PowerPulse

This project extracts energy capability data by state from the EIA API, stores the raw JSON in MongoDB, transforms and flattens the data, and saves it to both Excel and MySQL.

## 📁 Project Structure

```
etl-powerpulse/
├── src/
│   ├── config.py
│   ├── decorators.py
│   ├── eia_client.py
│   ├── etl_app.py
│   ├── excel_exporter.py
|   ├── mongo_store.py
|   ├── mysql_loader.py
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚙️ How It Works

1. **Extract**: Fetches energy capability data from EIA API.
2. **Transform**: Flattens the JSON response into structured rows.
3. **Load**: 
   - Saves raw data into MongoDB  
   - Writes transformed data into Excel and inserts into MySQL

## 🚀 Setup Instructions

```bash
git clone https://github.com/yourusername/etl-powerpulse.git
cd etl-powerpulse

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# Set env vars or update config.py manually
export STATE_LIST="CA"
export MONGO_URI="mongodb://localhost:27017"
export MYSQL_HOST="localhost"
export MYSQL_USER="root"
export MYSQL_PWD="root"
export MYSQL_DB="godigitaldb"
export EXCEL_PATH="output.xlsx"

python src/etl_app.py
```

## ✅ Tests

```bash
pytest tests/
```

## 📌 TODOs

- [ ] Add Docker support
- [ ] Add Airflow DAG
- [ ] CI with GitHub Actions

## 📃 License

MIT
