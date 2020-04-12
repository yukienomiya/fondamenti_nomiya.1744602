

'''
    Es 9: 3 punti
    Si definisca la funzione es9(pathDir ) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che:
    - riceve come argomento l'indirizzo di una cartella.
    - restituisce una lista contenente i nomi delle sottocartelle in essa contenute a
      qualsiasi livello e per ogni sottocartella anche lo spazio  (in byte) occupato all'interno 
      della cartella da eventuali file di tipo .txt.
      La lista contiene dunque coppie, il primo elemento della coppia e' il nome di 
      una sottocartella ed il secondo e' lo spazio occupato dai file .txt presenti nella
      sottocartella.
      Le coppie devono comparire nella lista ordinate in modo decrescente rispetto 
      alla loro seconda componente e  a parita' vanno ordinate poi in modo lessicografico 
      crescente rispetto alla prima componente.
      File e cartelle il cui nome comincia  col carattere '.' non vanno considerati. 
      
      Ai fini dello svolgimento dell'esercizio possono risultare utili 
      le seguenti funzioni nel modulo os:
      os.listdir(), os.path.isfile(), os.path.isdir(), os.path.basename(), 
      os.path.getsize()

    Esempio: con es9('Informatica/Software') viene restituita la lista:
    [('SistemiOperativi', 287), ('Software', 10), ('BasiDati', 0)]

'''

import os

def es9(pathDir):
  pairList = visitPath(pathDir)
  return sorted(sorted(pairList, key=lambda x:x[0]), key=lambda x:x[1], reverse=True)

def visitPath(pathDir):
  ls, lF, lD = getListDir(pathDir)
  if (len(ls) == 0):
    return []
  if (len(lD) == 0):
    return txtFileCalculator(pathDir)
  else:
    acc = txtFileCalculator(pathDir)
    for d in lD:
      acc += visitPath(pathDir + '/' + d)
    return acc


def txtFileCalculator(pathDir):
  ls, lF, lD = getListDir(pathDir)
  mem = 0
  for f in lF:
    pathFile = pathDir + '/' + f
    fileComp = os.path.splitext(pathFile)
    if (fileComp[1] == '.txt'):
      mem += os.path.getsize(pathFile)
  return [(os.path.basename(pathDir), mem)]

def getListDir(pathDir):
  ls = os.listdir(pathDir)
  lF, lD = [], []
  for elem in ls:
    if (os.path.isfile(pathDir + '/' + elem)):
      if (not elem.startswith('.')):
        lF.append(elem)
    else:
      lD.append(elem)
  return ls, lF, lD
