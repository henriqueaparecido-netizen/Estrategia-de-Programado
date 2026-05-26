def busca_linear(lista, alvo):

    comparacoes = 0
    resposta = -1   # NOT-FOUND

    for i in range(0, len(lista)):

        comparacoes += 1

        if lista[i] == alvo:
            resposta = i
            break

    return resposta, comparacoes


A = [6, 9, 1, 13, 8, 2, 15]

# Procurando 1
indice1, comp1 = busca_linear(A, 1)

# Procurando 12
indice2, comp2 = busca_linear(A, 12)

print("Busca pelo 1")
print("Índice:", indice1)
print("Comparações:", comp1)

print("\n")

print("Busca pelo 12")
print("Índice:", indice2)
print("Comparações:", comp2)