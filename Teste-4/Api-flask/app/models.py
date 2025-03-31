import pandas as pd

class OperadoraModel:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path, delimiter=';', dtype=str)  # Ajuste o delimitador se necessário

    def get_carriers(self, term):
        filtro = self.df.apply(lambda row: row.astype(str).str.contains(term, case=False, na=False).any(), axis=1)
        return self.df[filtro].to_dict(orient='records')
