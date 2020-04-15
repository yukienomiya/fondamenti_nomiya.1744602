
def es43(ftesto):
  '''
  Si progetti la funzione es43(ftesto) che, preso in input l'indirizzo di un file di testo
  contenente righe contenenti interi separati da spazi, restituisce una lista  di interi.
  La lunghezza della lista e' data dal numero massimo di interi che compaiono nelle righe
  del file. E nella generica posizione i della lista c'e' l'intero corrispondente alla somma di tutti
  gli interi presenti in posizione  i  nelle varie righe che contengono almeno i interi.
  Ad esempio per il file contenente le  3 righe:
  ' 0 2  4
    6 8 10
    4 0  1'
  la funzione restituisce la lista [10,10,15] cioe' le somme in colonna
  Per il file contenente le  4 righe (nota, di lunghezza diversa):
  ' 1 2 3
    4 5 6 7 3 6
    1
    1 2'
  la funzione restituisce la lista [7,9,9,7,3,6] cioe' le somme in colonna
  '''
  sumDict = dict()
  numList = getNumLists(ftesto)
  for l in numList:
    for i in range(len(l)):
      sumDict[i] = sumDict.get(i, 0) + int(l[i])
  maxLen = max(sumDict)
  res = [0] * (maxLen + 1)
  for elem in sumDict:
    res[elem] = sumDict[elem]
  return res

def getNumLists(fname):
  numList = []
  f = open(fname, 'r')
  lines = f.readlines()
  for line in lines:
    l = []
    line = line.strip().split(' ')
    for c in line:
      if (len(c) > 0):
        l.append(c)
    numList.append(l)
  f.close()
  return numList



