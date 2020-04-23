def es41(fname1):
  ''' 
  Data una sequenza S di  interi definiamo sequenza derivata da S la  sequenza di n interi dove l'i-esimo 
  elemento e' dato dalla somma dei primi i interi di S.
  Ad esempio:
  la sequenza derivata da 
  S= 2, -3, -4,  4, 4, -5, 3, 1,-1  e'
      2, -1, -5, -1, 3, -2, 1, 2, 1.
  
  Implementate la funzione es41(fname1) che prende in input l'indirizzo fname1 di un file di testo contenente una 
  sequenza S di interi e restituisce il numero che compare con maggior frequenza nella sequenza derivata da S.
  Nel caso in cui i numeri con maggior frequenza siano piu' di uno viene restituito quello di valore massimo.
  Ad esempio se il file fname contiene la sequenza S= 2, -3, -4,  4, 4, -5, 3, 1, -1   la funzione restituisce il valore 2.
  Nel file fname1, ciascun intero della sequenza  e' separato dal successivo da una virgola ed eventuali spazi.
  '''
  f = open(fname1, 'r')
  l = f.readline()
  seq = l.strip().split(',')
  tot = 0
  occurrences = dict()
  for elem in seq:
    tot += int(elem.strip())
    occurrences[tot] = occurrences.get(tot, 0) + 1
  maxValue = max(occurrences, key = occurrences.get)
  l = []
  for elem in occurrences:
    if (occurrences[elem] == occurrences[maxValue]):
      l.append(elem)
  l.sort(reverse = True)
  f.close()
  return l[0]









