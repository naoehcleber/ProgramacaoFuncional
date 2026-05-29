from functools import reduce
from itertools import groupby
import csv

def calcular_juros(file_path):
    apply_fee = lambda row: {
    'id': row['id'],
    'valor_original': float(row['valor']),
    'taxa_10_porcento': round(float(row['valor']) * 0.10, 2),
    'valor_total': round(float(row['valor']) * 1.10, 2),
    'parcelas': int(row['quantidade_parcelas'])
}
    maior_que_mil = lambda row: float(row['valor']) > 1000
    with open(file_path, mode='r', encoding='utf-8') as file:
        
        csv_reader = csv.DictReader(file)
        
        
        filtrado = filter(maior_que_mil, csv_reader)
        
        
        juros_aplicados = map(apply_fee, filtrado)
        
        # Since map/filter are lazy, we cast to a list here to execute the pipeline and see results
    results = list(juros_aplicados)

calcular_juros('emprestimos_simulados.csv')
