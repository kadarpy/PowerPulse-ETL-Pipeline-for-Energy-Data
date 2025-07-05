import pandas as pd
from config import EXCEL_PATH
from decorators import log_step

class ExcelWriter:
    def __init__(self):
        self.records = []

    def add(self, rows):
        self.records.extend(rows)

    @log_step
    def write(self):
        df = pd.DataFrame(self.records)
        df.to_excel(EXCEL_PATH, index=False)