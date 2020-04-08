
def es30(fname1,fname2,fname3):
  ''' 
  Si implementi la funzione es30(fname1,fname2,fname3) prende in input l'indirizzo di tre file di testo.
  Il primo file di testo contiene un messaggio codificato dove ogni carattere e' stato 
  sostituito da un intero di tre cifre.
  Tutti i caratteri non numerici devono essere trasferiti come sono.
  Nel secondo file  e' possibile ritrovare le corrispondenze numeri-caratteri tra i numeri 
  del testo e il rispettivo carattere. 
  Piu' precisamente questo secondo file e' organizzato in righe,  in ciascuna riga sono 
  presenti un carattere  e un intero  di tre cifre  che gli corrisponde nel file di testo separati da almeno uno spazio.
  Numeri diversi possono far riferimento ad uno stesso carattere e non tutti i numeri che appaiono in fname1
  sono necessariamente presenti nel file di decodifica.
  La funzione es30 deve decodificare il messaggio presente nel primo file grazie 
  alle informazioni contenute nel secondo.
  I numeri non presenti nel secondo file vanno decodificati con il simbolo '?'.
  Il messaggio decodificato va poi salvato nel terzo file.
  La funzione infine restituisce il numero di caratteri decodificati con il valore '?' presenti nel file decodificato.
  Ad esempio se 
  - il file fname1 contiene il testo '991118991991345      103    091027003091103?'
  - il file fname2 contiene il testo 'n   091\n   t 991\n a   103\n a 127\n n 003\n  u 118 '
  il testo decodificato da registrare in file3 sara': 'tutt? a n?nna?' e la funzione restituisce il numero 2.
  Potete assumere che i caratteri numerici appaiano sempre raggruppati in triplette.
  '''
  charList = getSecretMessage(fname1)
  decoder = getDecoder(fname2)
  msg = ''
  count = 0

  for c in charList:
    if (len(c) == 3 and c[0].isdigit()):
      if (c in decoder):
        msg += decoder[c]
      else:
        msg += '?'
        count += 1
    else:
      msg += c
  
  f = open(fname3, 'w')
  f.write(msg)
  f.close()

  return count




# parser for file 1
def getSecretMessage(fname):
  f = open(fname, 'r')
  l = splitWithSpace(f.read())
  lista = []
  for s in l:
    if (len(s) == 0):
        lista.append(' ')
        continue
    i = 0
    while (i < len(s)):
      if (s[i].isdigit()):
        lista.append(s[i : i + 3])
        i = i + 3
      else:
        lista.append(s[i])
        i += 1
  f.close()
  return lista
    
# parser for file 2
def getDecoder(fname):
  f = open(fname, 'r')
  lines = f.readlines()
  decoder = dict()
  for line in lines:
    strList = []
    c, n = line.split()
    decoder[n] = c
  f.close()
  return decoder

# splits the string where the spaces are, but keeps them in the list
def splitWithSpace(string):
  listRes = []
  s = ''
  for c in string:
    if (c == ' '):
      if (len(s) == 0):
        listRes.append(' ')
      else:
        listRes.append(s)
        s = ''
        listRes.append(' ')
    else:
      s += c
  listRes.append(s)
  return listRes






















