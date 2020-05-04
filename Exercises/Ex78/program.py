def es78(parola):
  '''
  Si definisca la funzione ricorsiva (o che usa una vostra funzione ricorsiva)  
  es78(parola), che presa in input una stringa di caratteri  parola restituisce la lista delle  
  diverse "sottoparole crescenti"  di parola. Le sottoparole devono comparire nella lista in ordine lessicografico.
  Si ricorda che una sottoparola e' quello che si ottiene da una parola concellandone 0 o piu'
  caratteri (in testa, in coda o nel mezzo).
  Inoltre una sottoparola si dice crescente se i caratteri che la compongono
  letti da sinistra  a destra risultano ordinati lessicograficamente.
  
  Ad esempio  la lista restituita da es78('zanzara') sara'
  ['a', 'aa', 'aaa', 'aar', 'an', 'anr', 'anz', 'ar', 'az', 'n', 'nr', 'nz', 'r', 'z', 'zz']
  '''
  substr = getSubstrings(parola, 0, '', [])
  return sorted(list(set(substr)))


def getSubstrings(s, idx, substr, res):
  if (idx == len(s)):
    if (len(substr) != 0):
      if (list(substr) == sorted(list(substr))):
        res.append(substr)
  else:
    getSubstrings(s, idx + 1, substr, res)
    getSubstrings(s, idx + 1, substr + s[idx], res)
  return res



