

def __main__():
    vetor = [1,5,8,10]
    dobrar_valores = list(map(lambda x: x * 2, vetor))
    print(f'Dobro dos valores do vetor: {dobrar_valores}')
    vetor2= [1,2,3,4,5,6,7,8,9,10, 11,12,13,14,15,16,17,18,19, 20]
    filtrar_pares = list(filter(map(lambda x: x%2 == 0, vetor2)))
    print(f'Pares filtrados: {filtrar_pares}')
    nomes = ["joao", "beatriz", "alice", "felipe"]
    converter_maiusculas = list(map(str.upper, nomes))
    print(f'Nomes em maisculo: {converter_maiusculas}')
    dados = [" python", " funcional ", 'codar ']
    limpar_dados  = list(map(str.strip, dados))
    print(f'Dados "limpos" : {limpar_dados}')

if __name__ == __main__ :
    __main__()