def es59(ftesto):
  '''
  La funzione es6(ftesto) che restituisce una stringa di caratteri '0' oppure '1'.
  La stringa ha tanti caratteri '0' o '1' quante sono le righe nel file di testo  il cui
  percorso e' dato da ftesto. Il file di testo contiene righe di interi separati da un
  numero arbitrario di spazi.
  L'i-esimo carattere della stringa e' '0' se la somma degli interi presenti nell'i-esima riga del file
  e' un numero pari. L'i-esimo carattere della stringa e' '1' se la somma degli interi presenti
  nell'i-esima riga del file  e' un numero pari.
  '''
  res = ''
  f = open(ftesto, 'r')
  lines = f.readlines()
  for line in lines:
    words = line.strip().split()
    s = 0
    for word in words:
      s += int(word)
    if (s % 2 == 0):
      res += '0'
    else:
      res += '1'
  f.close()
  return res
