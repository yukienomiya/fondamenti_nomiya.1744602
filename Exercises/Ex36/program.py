def es36(listaDizionari):
  '''
  Si implementi la funzione es36(listaDizionari) che presi in input una lista di dizionari
  restituisce  un dizionario.
  I dizionari in input della listaDizionari  hanno come  chiave stringhe
  di caratteri tra 'a' e 'z' e come attributo liste di interi.
  Il dizionario restituito deve avere le  chiavi che risultano presenti in tutti i dizionari della  listaDizionari.
  A ciascuna chiave x di questo dizionario e' associata una lista di interi.
  Un intero e' presente nella lista se e solo se e' presente in tutte le liste di attributi della chiave x.
  La lista deve risultare ordinata in modo crescente.

  Ad esempio se la listaDizionari contenente i tre dizionari
  {'a': [1,3,5],'b':[2,3 ],'d':[3]},
  {'a':[5,1,2,3], 'b':[2],'d':[3]},
  {'a':[3,5], 'c':[4,1,2],'d':[4]}
  il dizionario restituito sara' {'a':[3,5],'d':[]}
  '''
  resDict = dict()
  keySet = getKeySet(listaDizionari)
  for k in keySet:
    resDict[k] = getValueList(listaDizionari, k)
  return resDict

def getKeySet(dictList):
  res = set(dictList[0].keys())
  for d in range(1, len(dictList)):
    res = res.intersection(set(dictList[d].keys()))
  return res

def getValueList(dictList, k):
  res = set(dictList[0][k])
  for d in range(1, len(dictList)):
    res = res.intersection(dictList[d][k])
  resList = list(res)
  resList.sort()
  return resList