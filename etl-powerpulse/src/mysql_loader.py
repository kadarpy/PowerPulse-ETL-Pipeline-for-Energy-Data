import pymysql
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PWD, MYSQL_DB
from decorators import log_step

class MySQLLoader:
    @log_step
    def insert(self, rows):
        conn = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB
        )
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS state_profiles (
                id INT AUTO_INCREMENT PRIMARY KEY,
                period VARCHAR(10),
                stateId VARCHAR(10),
                stateDescription VARCHAR(255),
                producertypeid VARCHAR(10),
                producerTypeDescription VARCHAR(255),
                energysourceid VARCHAR(50),
                energySourceDescription VARCHAR(255),
                capability DECIMAL(20,2),
                capability_units VARCHAR(50)
            );
        """)

        for row in rows:
            cur.execute("""
                INSERT INTO state_profiles (
                    period, stateId, stateDescription, producertypeid,
                    producerTypeDescription, energysourceid,
                    energySourceDescription, capability, capability_units
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                row.get("period"),
                row.get("stateId"),
                row.get("stateDescription"),
                row.get("producertypeid"),
                row.get("producerTypeDescription"),
                row.get("energysourceid"),
                row.get("energySourceDescription"),
                float(row.get("capability")) if row.get("capability") else None,
                row.get("capability-units")
            ))

        conn.commit()
        conn.close()