
import os
import os.path

def es68(dir, estensioni):
  """
  Si definisca la funzione ricorsiva (o che usa una vostra funzione ricorsiva) es68(dir, estensioni),
  che deve contare quanti file di certi tipi si trovano in una directory o in una delle sue sottodirectories,
  e che riceve come argomenti
      dir: il path della directory in cui cercare
      estensioni: una lista di stringhe "estensioni" (le ultime lettere del nome dei files che cerchiamo)
  La funzione deve tornare un dizionario che ha come chiavi le estensioni passate come argomento
  e come valori il numero di file il cui nome termina in quel modo, solo se > 0
  (ovvero, se nessun file con una data estensione appare nella directory o nelle sottodirectories
  la chiave non deve apparire nel dizionario tornato dalla funzione).

  Tests: date alcune directory contenenti file di tipo (ext) diverso, si chiama la funzione per contare alcuni dei tipi di file nelle diverse directory
  Test: che la funzione sia ricorsiva
  """
  extSet = set(estensioni)
  extList = visitPath(dir)
  diz = dict()
  for l in extList:
    e = l[1:]
    if (e in extSet):
      diz[e] = diz.get(e, 0) + 1
  return diz


def visitPath(path):
  l = listdirSENZAPUNTO(path)
  lF, lD = getListDir(path, l)

  if (len(l) == 0):
    return []
  if (len(lD) == 0):
    return fileExtList(lF)
  else:
    acc = []
    for d in lD:
      acc += visitPath(path + '/' + d)
    return fileExtList(lF) + acc

def getListDir(path, lista):
  lF = []
  lD = []
  for elem in lista:
    if (os.path.isdir(path + '/' + elem)):
      lD.append(elem)
    else:
      lF.append(elem)
  return lF, lD

def fileExtList(filesList):
  newList = []
  for elem in filesList:
    name = os.path.splitext(os.path.basename(elem))
    newList.append(name[1])
  return newList

def listdirSENZAPUNTO(path):
  lista = []
  for e in os.listdir(path):
    if (e.startswith('.')):
      continue
    lista.append(e)
  return lista


