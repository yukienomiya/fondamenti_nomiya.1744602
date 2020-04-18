def es3(ins1, ins2):
  '''
  progettare la funzione es3(ins1, ins2) che:
  - riceve  in input due insiemi  di numeri naturali
  - trova le terne (a,b,c) con a,b e c in insi1 con la proprieta' che a<b<c e a+b+c e' in insi2
  - restituisce l'insieme di tutte le triple trovate.
  Nella lista restituita le triple devono essere  rappresentate tramite tuple e le
  varie tuple devono comparire nella lista per somma di componenti crescenti e in caso di parita'
  in ordine lessicografico crescente.
  ESEMPIO:
  se ins1={ 2,4,5,6,8,9} e ins2={5,15,19,25} la funzione restituisce la lista
  [(2, 4, 9), (2, 5, 8), (4, 5, 6), (2, 8, 9), (4, 6, 9), (5, 6, 8)]
  '''
  res = []
  for a in ins1:
    bSet = getSet(ins1, a)
    for b in bSet:
      cSet = getSet(ins1, b)
      for c in cSet:
        tot = a + b + c
        if (tot in ins2):
          t = (a, b, c)
          res.append(t)
  return sorted(sorted(res), key = lambda t: t[0] + t[1] + t[2])

def getSet(ins, value):
  res = set()
  for elem in ins:
    if (elem > value):
      res.add(elem)
  return res
