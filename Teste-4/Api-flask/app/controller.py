from app.models import OperadoraModel

operadora_model = OperadoraModel("Api-flask\csv\Relatorio_cadop.csv")

def get_carriers(term):
    return operadora_model.get_carriers(term)
