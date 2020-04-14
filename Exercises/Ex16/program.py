def es16(s, k):
  '''
  Es 5: 3 punti
  progettare la funzione es16(s,k) che: 
  - riceve  in input una stringa s di caratteri   ed un intero k 
  - costruisce la lista con  le diverse sottostringhe  di s  in cui compaiono 
    esattamente k caratteri distinti
  - restituisce la lista delle sottostringhe dopo averla ordinata  per
    lunghezze decrescenti e, a parita' di lunghezza, in ordine lessicografico
  Nota che la lista non deve contenere duplicati.
  Si ricorda che una sottostringa di s e' quello che si ottiene da s eliminando 0 o piu' 
  caratteri iniziali  e 0 o piu' caratteri finali.
  ESEMPI: 
  con  s='aabbb' e k=1 la funzione restituisce la lista ['bbb', 'aa', 'bb', 'a', 'b']
  cons s='bcafedg' e k=3 la funzione restituisce la lista ['afe', 'bca', 'caf', 'edg', 'fed']
  cons s='ccaabbdd' e k=3 la funzione restituisce la lista 
      ['aabbdd', 'ccaabb', 'aabbd', 'abbdd', 'caabb', 'ccaab', 'abbd', 'caab']
  '''
  
  substrSet = getSubstr(s)
  res = []
  for substr in substrSet:
    if letterCount(substr, k):
      res.append(substr)
  return sorted(sorted(res), key = lambda x:len(x), reverse = True)


def getSubstr(s):
  substrSet = set()
  for c in range(len(s)):
    for i in range(c + 1, len(s) + 1):
      substrSet.add(s[c:i])
  return substrSet

def letterCount(substr, k):
  s = set(substr)
  return (len(s) == k)