def calcular_hash(nome, tamanho_tabela = 10):
    soma = 0
    uni = 0
    
    print("Nome: " + nome)
    
    print("Valores em UniCode: ", end="")    
    
    for letra in nome:
        uni = ord(letra)
        print(letra + "(" + str(uni) + ") ", end="")
        soma += uni
        
    print("= " + str(soma))
    
    index = soma % tamanho_tabela
    
    print("Índice: " + str(soma) + " mod 10 = " + str(index) + "\n")

    return index

calcular_hash("Henrique")

calcular_hash("Maria")

calcular_hash("Carina")