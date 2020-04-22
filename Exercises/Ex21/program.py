def es21(matrice):
  '''
  es21(matrice) presa la matrice di caratteri rappresentata tramite una lista di liste di caratteri, 
  la restituisce dopo averne ordinato le colonne in ordine lessicografico. 
  La matrice passata in input al termine della funzione non deve risultare modificata.  
  Ad esempio se la matrice di input e'
    [['q','s','g','g'],
    ['b','a','m','f'],
    ['a','b','n','z']] 
  la funzione restituira' la matrice:
    [['a','a','g','f'],
    ['b','b','m','g'],
    ['q','s','n','z']]
  '''
  revMatrix = [[0 for x in range(len(matrice))] for y in range(len(matrice[0]))]
  res = [[0 for x in range(len(matrice[0]))] for y in range(len(matrice))]

  for col in range(len(matrice[0])):
    for row in range(len(matrice)):
      revMatrix[col][row] = matrice[row][col]
    revMatrix[col] = sorted(revMatrix[col])

  for col in range(len(revMatrix[0])):
    for row in range(len(revMatrix)):
      res[col][row] = revMatrix[row][col]
  
  return res