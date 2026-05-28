from functools import reduce

def __main__():
    vetor = [1,5,8,10]
    somatorio = reduce(lambda acumulador, x: acumulador + x, vetor)
    produtorio = reduce(lambda acumulador, x: acumulador *x, vetor)
    maior_numero = reduce(lambda acumulador, x: acumulador if acumulador > x else x, vetor)
    
    filtra_e_dobra = list(map(lambda x: x * 2, filter(lambda x: x > 5, vetor)))


if __name__ == __main__ :
    __main__()