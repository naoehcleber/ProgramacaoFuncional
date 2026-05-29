from functools import reduce

def __main__():
    vetor = [1,5,8,10]
    somatorio = reduce(lambda acumulador, x: acumulador + x, vetor)
    print(f'Somatorio: {somatorio}')
    produtorio = reduce(lambda acumulador, x: acumulador *x, vetor)
    print(f'produtorio: {produtorio}')

    maior_numero = reduce(lambda acumulador, x: acumulador if acumulador > x else x, vetor)
    print(f'Maior Numero: {maior_numero}')
    
    filtra_e_dobra = list(map(lambda x: x * 2, filter(lambda x: x > 5, vetor)))
    print(f'Dobro dos numeros maiores que 5: {maior_numero}')


if __name__ == __main__ :
    __main__()