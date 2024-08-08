# Description: Perceptron simples (de uma camada) com 3 entradas e 3 pesos com biblioteca numpy

import numpy as np # Importa a biblioteca numpy

entradas = np.array([1, 7, 5]) # Define as entradas como um array numpy
pesos = np.array([0.8, 0.1, 0]) # Define os pesos como um array numpy

def soma(e, p): # Função que calcula a soma ponderada
    return e.dot(p) # Retorna o valor da soma ponderada
# dot product / produto escalar
        
s = soma(entradas, pesos) # Chama a função soma com as entradas e pesos
print(s) # Exibe o resultado   

def stepFunction(soma): 
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s) # Chama a função stepFunction com o valor da soma ponderada 
print(r)  

# Exibe o resultado de ativação ou não do neurônio

entradas = np.array([-1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

def soma(e, p): 
   return e.dot(p) 
        
s = soma(entradas, pesos) 
print(s) 

def stepFunction(soma): 
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s) 
print(r)  