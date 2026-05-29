from functools import reduce
vetor = [1,5,8,10]

produtorio = reduce(lambda acumulador, x: acumulador *x, vetor)
print(f'produtorio: {produtorio}')

