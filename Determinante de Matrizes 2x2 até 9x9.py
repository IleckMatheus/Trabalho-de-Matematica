import numpy as np
import time
import matplotlib.pyplot as plt

# Entrada e Processamentos dos dados

ordem = [x for x in range(2, 10)] # lista com ordem da matriz
tempo = [] # lista para armazenar o tempo

# laço for para calcular o determinante das matriz
for x in range(2,10):
  tempo_inicial = time.perf_counter_ns()
  matriz_A = np.random.randint(10, size=(x, x)) # monta uma matriz com valores aleatorios
  determinante = np.linalg.det(matriz_A) # calcula o determinante da matriz
  tempo_final = time.perf_counter_ns()
  tempo_total = tempo_final - tempo_inicial
 # calcula o tempo total da execucao do algoritmo
  tempo.append(tempo_total)
  print(f'''Matriz = 
  {matriz_A}\n
  Determinante da Matriz de Ordem {x} = {determinante:.0f}\n 
  Tempo de execução, Matriz de Ordem {x} = {tempo_total}\n''')
print("================================================ \n")
print(f'''O tamanho das Matrizes{ordem} \n
O tempo de processamento foi de: {tempo}''')



fig, ax = plt.subplots()

grfmatriz = ['2x2', '3x3', '4x4', '5x5', '6x6', '7x7', '8x8', '9x9'] # X
counts = tempo # Y
bar_labels = 'Rosa'
bar_colors = ['tab:pink']

ax.bar(grfmatriz, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('Tempo de execução em nanosegundo')
ax.set_title('')
ax.legend(title='')

plt.show()