from functools import reduce
vetor = [1,5,8,10]
filtra_e_dobra = list(map(lambda x: x * 2, filter(lambda x: x > 5, vetor)))
print(f'Dobro dos numeros maiores que 5: {filtra_e_dobra}')