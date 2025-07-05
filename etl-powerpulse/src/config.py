import os

EIA_API_KEY = os.getenv("EIA_API_KEY", "")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PWD = os.getenv("MYSQL_PWD", "appleSE@786")
MYSQL_DB = os.getenv("MYSQL_DB", "godigitaldb")
EXCEL_PATH = os.getenv("EXCEL_PATH","output.xlsx")