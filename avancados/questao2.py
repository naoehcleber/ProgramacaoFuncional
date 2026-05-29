from functools import reduce
from itertools import groupby
import csv

def agrupar_por_letra_inicial(nomes):
    criterio = lambda nome: len(nome)
    nomes_ordenados = sorted(nomes, key=criterio)
    dicionario_agrupado = {
        chave: list(grupo) 
        for chave, grupo in groupby(nomes_ordenados, key=criterio)  
    }
    return dicionario_agrupado