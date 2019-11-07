
'''
    Abbiamo n stringhe di caratteri.
    All'interno delle stringhe  e' nascosta una parola segreta come sottostringa di
    caratteri consecutivi.
    Sappiamo con certezza che la parola si ripete uguale esattamente una volta in ciascuna
    stringa ma non sappiamo dove.
    Della parola conosciamo la lunghezza M e sappiamo che non ci sono altre sottostringhe
    di lunghezza M che si ripetono una sola volta in tutte le stringhe.
    Vogliamo sapere per ogni stringa  la posizione dove compare il primo carattere
    della parola nascosta.
    Ad esempio per le 6 stringhe con parola nascosta di lunghezza 3:

    moneta
    maratoneta
    pitone
    onesto
    storione
    sonetto

    la parola nascosta è 'one' e le posizioni sono nell'ordine: 1, 5, 3, 0, 5, 1



    Progettare una funzione es1(ftesto) che prende in input  un file contenente la lunghezza
    della parola nascosta e le n stringhe di caratteri e restituisce una lista di n interi.
    L'intero in  posizione i della lista e' la posizione dove compare il primo carattere
    della parola nascosta nella stringa i.

    Le informazioni nel file ftesto sono organizzate nel seguente modo:
    - la prima riga contiene la lunghezza della parola nascosta (un intero).
    - seguono poi le stringhe di caratteri, ciascuna stringa occupa una o piu'
    righe consecutive del file ed e' separata dalla stringa seguente da una linea vuota.
    Ogni riga del file termina con un' andata a capo.
    Vedi ad esempio il file ft1.txt che codifica l'istanza vista prima.

    es('ft1.txt') deve restituire la lista [1,5,3,0,5,1]


    NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

    ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)

'''

def es1(ftesto):
  f = open(ftesto)
  length = int(f.readline().rstrip())
  lines = f.readlines()

  words, shortestWord = parseWords(lines)
  subs = findSubstrings(shortestWord, length)

  idx = 0
  while len(subs) > 1:
    comp = findSubstrings(words[idx], length)
    subs = subs.intersection(comp)
    idx += 1
  sharedSS = subs.pop()

  result = list(range(0, len(words)))

  for i in range(len(words)):
    result[i] = words[i].find(sharedSS) ### FIND

  f.close()
  return result








#crea la lista words che contiene ogni parola come elemento
#in piu tiene traccia della parola piu corta
def parseWords(list): #O(nLines)
  result = []
  min = ''
  str = ''
  for i in range(len(list)):
    list[i] = list[i].rstrip()
    str += list[i]
    if (i == len(list) - 1) or (list[i + 1] == '\n'): #la parola è finita
      if (len(str) < len(min)) or (not result):
        min = str
      result.append(str)
      str = ''
  return result, min



#crea un insieme con tutte le sottostringhe lunghe length della parola più corta
def findSubstrings(string, length): #O(len(shortestWord) / length)
  subs = set()
  for i in range(len(string) - (length - 1)):
    s = string[i : i + length]
    if string.count(s) == 1:
      subs.add(s)
  return subs

















if __name__ == '__main__':
  # inserisci qui i tuoi test
  pass
