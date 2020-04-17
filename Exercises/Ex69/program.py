import os
import os.path

def es69(dirc, profondita, estensioni):
  """
  Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es69(dir, profondita, estensioni),
  che deve eliminare tutti i file che appartengono ad una delle estensioni indicate,
  solo se si trovano alla profondita' indicata, e che riceve come argomenti:
      dir: la directory in cui cercare (i file in questa directory si trovano a profondita 0)
      profondita: la profondita' in cui dobbiamo cancellare i file, contando da 0 per la directory radice passata come argomento
      estensioni: una lista di stringhe "estensioni" (le ultime lettere del nome dei files che cerchiamo)
  La funzione deve tornare il numero totale di files presenti nelle directories di profondita' minore o uguali a 'profondita',
  che NON sono stati cancellati

  NOTA: ignorate tutti i file e directory che iniziano con '.'

  NOTA: per eliminare un file usate la funzione os.remove

  Tests: date alcune directories contenenti file con estensioni diverse a diverse profondita', si chiama la funzione e si controlla che i file contenuti nelle directories esistano/non esistano a seconda del caso (senza usare una soluzione ricorsiva ma testando direttamente i path dei files relativi alla dir iniziale)
  Test: che la funzione sia ricorsiva
  """
  
  return visitPath(dirc, profondita, estensioni)

def visitPath(path, depth, extList):
  dirList, fileList = getDirFile(path)
  if (depth == 0):
    return removeFiles(path, fileList, extList)
  if (len(dirList) == 0):
    return len(fileList)
  else:
    acc = 0
    for d in dirList:
      acc += visitPath(path + '/' + d, depth - 1, extList)
    return len(fileList) + acc

def getDirFile(path):
  dirList = []
  fileList = []
  for d in os.listdir(path):
    if (os.path.isdir(path + '/' + d)):
      dirList.append(d)
    if ((os.path.isfile(path + '/' + d)) and not ((os.path.basename(d)).startswith('.'))):
      fileList.append(d)
  return dirList, fileList

def removeFiles(path, fileList, extList):
  count = 0
  for d in fileList:
    dExt = (os.path.splitext(d))[1]
    if (dExt[1:] in extList):
      os.remove(path + '/' + d)
    else:
      count += 1
  return count

