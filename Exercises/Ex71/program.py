import os
import os.path

def es71(dirC, minimo, massimo):
  """
  Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es71(dir, minimo, massimo)
  che cerca nella directory dir  i files che hanno una dimensione compresa tra minimo e massimo (inclusi).
  La funzione deve tornare un dizionario che contiene come chiavi i nomi dei files individuati (senza path),
  e come valori le corrispondenti profondita' (contando la directory 'dir' iniziale come profondita' 0)
  Nel caso in cui un nome di file sia presente a profondita' diverse, il dizionario deve contenere quella maggiore.
  Nota: per individuare la dimensione del file potete usare la funzione os.stat

  Test:   date alcune directory contenenti files di dimensioni varie a varie profondita',
          controllare che il risultato sia il dizionario corretto
  Test:   che la funzione sia ricorsiva
  """
  tList = visitPath(dirC, minimo, massimo, 0)
  return makeDict(tList)


def visitPath(path, minDim, maxDim, depth):
  dirList, fileList = getDirFile(path, minDim, maxDim)
  if (len(dirList) == 0):
    return getTupleList(path, fileList, minDim, maxDim, depth)
  else:
    acc = []
    for d in dirList:
      acc += visitPath(path + '/' + d, minDim, maxDim, depth + 1)
    return acc + getTupleList(path, fileList, minDim, maxDim, depth)

def makeDict(tList):
  resDict = dict()
  for t in tList:
    resDict[t[0]] = max(resDict.get(t[0], t[1]), t[1])
  return resDict

def getTupleList(path, fileList, minDim, maxDim, depth):
  tupleList = []
  for n in fileList:
    t = (n, depth)
    tupleList.append(t)
  return tupleList

def getDirFile(path, minDim, maxDim):
  dirList = []
  fileList = []
  for d in os.listdir(path):
    completePath = path + '/' + d
    if (os.path.isdir(completePath)):
      dirList.append(d)
    if ((os.path.isfile(completePath)) and not ((os.path.basename(d)).startswith('.'))):
      dim = os.path.getsize(completePath)
      if (dim >= minDim  and dim <= maxDim):
        fileList.append(os.path.basename(d))
  return dirList, fileList

