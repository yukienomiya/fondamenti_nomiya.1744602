import json

def es39(n, jsonFile):
  '''     
  Dato un intero n, una matrice a spirale di ordine n e' una matrice  di dimensioni n x n
  che riporta i numeri da 1 a n**2 seguendo un andamento a spirale in senso orario. 
  Ad esempio  la matrice a spirale di ordine 4 e'
  
   1  2  3 4 
  12 13 14 5
  11 16 15 6
  10  9  8 7 
  
  si definisca la funzione es39(n, jsonFile), che presi come argomenti:
  - n: intero
  - jsonFile: il path di un file json
  registra in formato json nel file jsonFile una matrice a spirale di ordine n 
  rappresentata come lista di liste. 
  La funzione deve anche restituire la somma dei valori presenti nelle colonne 
  di indice pari della matrice.
  Ad esempio per n=4 il jsonFile conterra'
    [[1,  2,  3, 4],[12, 13, 14, 5],[11, 16, 15, 6], [10,  9,  8, 7]]
    e il valore restituito sara' 74.
  '''
  f = open(jsonFile, 'w')
  matrix = createMatrix(n)
  json.dump(matrix, f)
  f.close()
  count = 0
  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      if (col % 2 == 0):
        count += matrix[row][col]
  return count


def createMatrix(n):
  matrix = [[0 for j in range(n)] for i in range(n)]
  x, y = 0, 0
  directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
  l = n 
  dIdx = 0 
  count = 0 
  for i in range(1, n ** 2 + 1):
    matrix[y][x] = i
    direction = directions[dIdx]
    x += direction[0]
    y += direction[1]
    count += 1
    if (count == l - 1): 
      count = 0
      dIdx += 1
    if (dIdx == 3 and count == l - 2):
      l -= 2
      dIdx = 0
      count = -1
  return matrix