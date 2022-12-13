#Inicio Determinante com Numpy
from numpy import matrix, linalg
import matplotlib.pyplot as plt
import time

tempo_numpy = time.perf_counter_ns()


matriz = matrix([[2,3,-1,2],
                 [0,4,-3,5],
                 [1,2,1,3],
                 [0,4,1,0]])


print("A Matriz A é: "'\n',matriz)

resultado = linalg.det (matriz)

print("\n O derteminante da matriz A é: ", round(resultado),"\n")

tempo_final = time.perf_counter_ns()
tempo_total_NP= (tempo_final - tempo_numpy)
print(f'\n O tempo de processamento do código com numpy foi de: {tempo_total_NP} nanosegundos')

print("\n ============================================================================= \n")

#Fim determinante com Numpy

""" 
/////////////////////////////////////////////////////////////// 
"""

#Inicio determinante sem Numpy

tempo_inicial = time.perf_counter_ns()
def remover(matriz_original,tirar_i,tirar_j):
    matriz_nova = [[int(0) for i in range(len(matriz_original)-1)] for j in range(len(matriz_original)-1)]
    ni = 0
    for i in range(len(matriz_original)):
        nj = 0
        for j in range(len(matriz_original)): 
            if j != tirar_j: 
                matriz_nova[ni][nj] = matriz_original[i][j]
                nj += 1
        if i != tirar_i: 
            ni += 1
    return matriz_nova


def determinante(matriz_original):
    if len(matriz_original) != len(matriz_original[0]): 
        print("A matriz não é quadrada!")
        return matriz_original
    resposta = 0
    if len(matriz_original) == 2: 
        resposta = (matriz_original[0][0] * matriz_original[1][1]) - (matriz_original[1][0] * matriz_original[0][1])
        return resposta
    if len(matriz_original) > 2:
        for j in range(len(matriz_original)):
            resposta += matriz_original[0][j] * (-1)**(0+j) * determinante(remover(matriz_original,0,j))
        return resposta 
    
matriz_1 = [[2,3,-1,2],
            [0,4,-3,5],
            [1,2,1,3],
            [0,4,1,0]]

for i in range(0, 4):
  for j in range(0, 4):
    print(f'[{matriz_1[i][j]:^5}]', end='')
  print()

print("\n Determinante : ",determinante(matriz_1),"\n")
#Restante do código

#Print do tempo que demorou para rodar a parte específica do código
tempo_final = time.perf_counter_ns()
tempo_total = tempo_final - tempo_inicial

print("\nTempo para excecução sem numpy foi de: ", tempo_total ,"nanosegundos", "\n")

#Fim determinante sem Numpy

Matrizes=["Matriz sem numpy" , "Matriz com Numpy"]
vl_tempo_total=[(tempo_total)*10, tempo_total_NP]

plt.stem(Matrizes, vl_tempo_total)
plt.xlabel('Tamanho da Matriz')
plt.ylabel('Tempo de execução em nanosegundo')
plt.title('Relação tempo de execução X tamanho da Matriz')

plt.show()