from eia_client import EIAClient
from mysql_loader import MySQLLoader
from excel_exporter import ExcelWriter
from mongo_store import MongoStore
from decorators import log_step


def flatten(state, data):
    rows = []
    for d in data.get("response", {}).get("data", []):
        rows.append({
            "period": d.get("period"),
            "stateId": d.get("stateId", state),
            "stateDescription": d.get("stateDescription"),
            "producertypeid": d.get("producertypeid"),
            "producerTypeDescription": d.get("producerTypeDescription"),
            "energysourceid": d.get("energysourceid"),
            "energySourceDescription": d.get("energySourceDescription"),
            "capability": d.get("capability"),
            "capability-units": d.get("capability-units")
        })
    return rows


@log_step
def run_etl():
    api = EIAClient()
    mysql = MySQLLoader()
    excel = ExcelWriter()
    mongo = MongoStore()
    all_rows = []

    data_bundle = api.fetch(states= ["CA","TX","NY"])

    for state, data in data_bundle:
        rows = flatten(state, data)
        all_rows.extend(rows)
        excel.add(rows)
        try:
            mongo.save(data)
        except Exception as error:
            print(error)

    mysql.insert(all_rows)
    excel.write()
    

if __name__ == "__main__":
    run_etl()