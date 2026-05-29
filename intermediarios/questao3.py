from functools import reduce
vetor = [1,5,8,10]

maior_numero = reduce(lambda acumulador, x: acumulador if acumulador > x else x, vetor)
print(f'Maior Numero: {maior_numero}')
