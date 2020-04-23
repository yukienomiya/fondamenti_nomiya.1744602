def es56(tabella):
  '''
  la funzione es56(tabella) che presa in input:
  - una tabella  di interi (rappresentata tramite lista di liste in cui ciascuna lista e' 
  una riga della tabella) restituisce la lista con gli interi che occorrono il massimo 
  numero di volte nella tabella e modifica la tabella distruttivamente. 
  La lista restituita deve risultare  ordinata in modo crescente. Al termine della funzione, 
  nella tabella i numeri che occorrevano un numero massimo di volte devono risultare sostituiti dal 
  carattere '*'.
  Ad esempio per tabella= [[3,2,1,3],[2,1,3,5],[1,3,2,1]] al termine della funzione la lista 
  restituita e' [1,3] e la tabella diviene [[*,2,*,*],[2,*,*,5],[*,*,2,*]] 
  '''
  mostFrequentElem = []
  occurrences = dict()
  for row in range(len(tabella)):
    for col in range(len(tabella[0])):
      value = tabella[row][col]
      occurrences[value] = occurrences.get(value, 0) + 1
  maxOcc = max(occurrences, key = occurrences.get)
  for elem in occurrences:
    if (occurrences[elem] == occurrences[maxOcc]):
      mostFrequentElem.append(elem)
  for row in range(len(tabella)):
    for col in range(len(tabella[0])):
      if (tabella[row][col] in mostFrequentElem):
        tabella[row][col] = '*'
  return sorted(mostFrequentElem)