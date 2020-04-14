  
    

'''
    Es 10: 3 punti
progettare la funzione es10(ftesto,k) che, presi in input 
l'indirizzo di un file di testo ed un intero k, restituisce una stringa di caratteri lunga k.
Il file di testo contiene stringhe di diversa lunghezza 
(una per riga ed ogni riga termina con '\n'), si guardi 
ad esempio il file f9.txt. 
I k caratteri della stringa restituita  dalla funzione si ottiengono
considerando le stringhe lunghe k presenti nel file di testo. 
L'i-mo carattere della stringa sara' il carattere che compare con maggior 
frequenza come i-mo carattere delle stringhe lunghe k nel file di testo (in caso 
di parita' di occorrenze viene scelto il carattere che precede 
gli altri lessicograficamente). 
Nel caso il file di testo non contenga parole lunghe k allora viene restituita 
la stringa vuota.  
Ad Esempio, per il file di testo f9.txt e k=3 la funzione restituisce  la stringa 'are' a 
seguito della presenza in f9.txt delle seguenti 4 stringhe lunghe 3:
tre
due
amo
ora 
'''

def es10(ftesto,k):
  f = open(ftesto, 'r')
  lines = f.readlines()
  filteredLines = filterStrK(lines, k)
  if (len(filteredLines) == 0):
    return ''
  occDict = getOccurrencesDict(filteredLines, k)
  return getStringa(occDict)

def getStringa(listDict):
  if (len(listDict) == 1):
    return findMax(listDict[0])
  return findMax(listDict[0]) + getStringa(listDict[1:])

def filterStrK(lines, k):
  filteredList = []
  for line in lines:
    l = line.strip()
    if (len(l) == k):
      filteredList.append(l)
  return filteredList

def getOccurrencesDict(wordList, k):
  dictList = []
  for i in range(k):
    occ = dict()
    for word in wordList:
      occ[word[i]] = occ.get(word[i], 0) + 1
    dictList.append(occ)
  return dictList

def findMax(occDict):
  charMax = max(occDict, key = occDict.get)
  res = []
  for d in occDict:
    if (occDict[d] == occDict[charMax]):
      res.append(d)
  res.sort()
  return res[0]