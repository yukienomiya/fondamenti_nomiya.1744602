def es64(l):
  '''
  Scrivere la funzione es64 che prende come input una lista di
  interi non negativi e produce una stringa contenente i numeri della lista in verticale,
  una cifra per riga, allineando le cifre delle unita' alla riga piu' in basso.

  Es: es64([5,69,2090]) torna la stringa
      2
      0
    6 9
  5 9 0
  '''
  res = ''
  newL = []
  for elem in l:
    newL.append(str(elem))
  maxLen = len(max(newL, key = len))
  for i in range(maxLen - 1, -1, -1):
    for w in range(len(newL)):
      word = newL[w]
      if (len(word) - i > 0):
        res += word[len(word) - i - 1]
      else:
        res += ' '
      if (w < len(newL) - 1):
        res += ' '
      else:
        res += '\n'
  return res[:len(res) - 1]