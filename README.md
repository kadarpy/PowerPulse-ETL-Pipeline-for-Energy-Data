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

The **PowerPulse ETL pipeline** automates extracting, transforming, and loading energy capability data from the U.S. EIA API into multiple storage systems for analysis and reporting.  

Here’s how the main components work:

### 🔧 Source Modules

- **`config.py`**  
  Stores environment variables and configuration, such as API keys, file paths, and database credentials.

- **`decorators.py`**  
  Provides reusable decorators for logging, timing, and error handling across the pipeline.

- **`eia_client.py`**  
  Handles communication with the EIA API to fetch state-wise energy capability data. Manages API key authentication and response parsing.

- **`etl_app.py`**  
  The main orchestrator of the ETL pipeline:
  - Extracts data from the EIA API
  - Transforms and cleans it
  - Triggers loaders to export data to various destinations

- **`excel_exporter.py`**  
  Converts structured data into Excel format for manual analysis or sharing.

- **`mongo_store.py`**  
  Persists raw JSON API responses into MongoDB for long-term storage and traceability.

- **`mysql_loader.py`**  
  Inserts transformed data into MySQL for use with analytics platforms and BI tools.

---

### 📊 Workflow Summary

1. **Extract**  
   Connects to the EIA API and retrieves raw energy data in JSON format.

2. **Transform**  
   Flattens, cleans, and structures the JSON into tabular format using Python.

3. **Load**  
   - **Raw Data** → Stored in **MongoDB**
   - **Cleaned Data** → Exported to:
     - Excel spreadsheet (`.xlsx`)
     - MySQL database for structured queries and reporting

---

### ✅ Future Enhancements

- [ ] Docker support for containerized deployment
- [ ] Airflow DAG for scheduled and production-ready ETL runs
- [ ] GitHub Actions for CI/CD integration and automated testing



## 📃 License

MIT
