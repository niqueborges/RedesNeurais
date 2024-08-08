# Description: Perceptron simples (de uma camada) com 3 entradas e 3 pesos

entradas = [1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(e, p): # Função que calcula a soma ponderada
    s = 0 # Inicializa a variável s
    for i in range(3): # Loop para percorrer as entradas e pesos
        #print(entradas[i]) 
        #print(pesos[i])
        s += e[i] * p[i] # Calcula a soma ponderada
    return s # Retorna o valor da soma ponderada
        
s = soma(entradas, pesos) # Chama a função soma com as entradas e pesos

print(s) # Exibe o resultado   

def stepFunction(soma): 
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s) # Chama a função stepFunction com o valor da soma ponderada 

print(r)  # Exibe o resultado

# Exibe o resultado de ativação ou não do neurônio

entradas = [-1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(e, p): # Função que calcula a soma ponderada
    s = 0 # Inicializa a variável s
    for i in range(3): # Loop para percorrer as entradas e pesos
        #print(entradas[i]) 
        #print(pesos[i])
        s += e[i] * p[i] # Calcula a soma ponderada
    return s # Retorna o valor da soma ponderada
        
s = soma(entradas, pesos) # Chama a função soma com as entradas e pesos

print(s) # Exibe o resultado   

def stepFunction(soma): 
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s) # Chama a função stepFunction com o valor da soma ponderada 

print(r)  # Exibe o resultado
