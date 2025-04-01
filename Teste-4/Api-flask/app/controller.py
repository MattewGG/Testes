from app.models import OperadoraModel
import pandas as pd  

operadora_model = OperadoraModel("C:/Users/Pichau/Downloads/Relatorio_cadop.csv")

def get_carriers(term, filter_date_from=None, filter_date_to=None):
    results = operadora_model.get_carriers(term)
    

    if filter_date_from and filter_date_to:
        results = [op for op in results 
                  if (pd.notna(op.get('Data_Registro_ANS')) and 
                  (filter_date_from <= op['Data_Registro_ANS'] <= filter_date_to))]
    
    return results