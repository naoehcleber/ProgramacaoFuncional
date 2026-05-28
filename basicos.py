

def __main__():
    vetor = [1,5,8,10]
    dobrar_valores = list(map(lambda x: x * 2, vetor))
    vetor2= [1,2,3,4,5,6,7,8,9,10, 11,12,13,14,15,16,17,18,19, 20]
    filtrar_pares = list(filter(map(lambda x: x%2 == 0, vetor2)))
    nomes = ["joao", "beatriz", "alice", "felipe"]
    converter_maiusculas = list(map(str.upper, nomes))
    dados = [" python", " funcional ", 'codar ']
    limpar_dados  = list(map(str.strip, dados))

if __name__ == __main__ :
    __main__()