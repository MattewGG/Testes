import pandas as pd

class OperadoraModel:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path, delimiter=';', dtype=str)
        
    def get_carriers(self, term):
      
        if not term:
            return self.df.to_dict(orient='records')
            
    
        mask = self.df.apply(
            lambda row: row.astype(str).str.contains(term, case=False, na=False).any(),
            axis=1
        )
        return self.df[mask].to_dict(orient='records')