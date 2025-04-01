from app.models import OperadoraModel
import pandas as pd  

operadora_model = OperadoraModel("C:/Users/Pichau/Downloads/Relatorio_cadop.csv")

def get_carriers(term, filter_date_from=None, filter_date_to=None):
    results = operadora_model.get_carriers(term)

    if filter_date_from and filter_date_to:
        filter_date_from = pd.to_datetime(filter_date_from, errors='coerce')
        filter_date_to = pd.to_datetime(filter_date_to, errors='coerce')

        filtered_results = []
        for op in results:
            if pd.notna(op.get('Data_Registro_ANS')): 
                try:
                    data_registro = pd.to_datetime(op['Data_Registro_ANS'], errors='coerce')
                    if filter_date_from <= data_registro <= filter_date_to:
                    
                        op['Data_Registro_ANS'] = data_registro.strftime('%Y-%m-%d')
                        filtered_results.append(op)
                except Exception:
                    continue  
        results = filtered_results

    return results

def get_carriers_by_date(date):
    return get_carriers('', filter_date_from=date, filter_date_to=date)

def get_carriers_by_period(start_date, end_date):
    return get_carriers('', filter_date_from=start_date, filter_date_to=end_date)

