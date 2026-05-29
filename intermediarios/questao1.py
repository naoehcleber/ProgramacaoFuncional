from functools import reduce

vetor = [1,5,8,10]
somatorio = reduce(lambda acumulador, x: acumulador + x, vetor)
print(f'Somatorio: {somatorio}')