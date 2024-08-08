# Description: Perceptron simples com 3 entradas e 3 pesos

entradas = [1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(e, p): # Função que calcula a soma ponderada
    s= 0 # Inicializa a variável s
    for i in range(3): # Loop para percorrer as entradas e pesos
        print(entradas[i]) 
        print(pesos[i])
        
soma(entradas, pesos) # Chama a função soma com as entradas e pesos           