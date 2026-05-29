vetor2= [1,2,3,4,5,6,7,8,9,10, 11,12,13,14,15,16,17,18,19, 20]
filtrar_pares = list(filter(map(lambda x: x%2 == 0, vetor2)))
print(f'Pares filtrados: {filtrar_pares}')