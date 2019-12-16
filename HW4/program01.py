
'''
    Data una matrice di caratteri ed una parola, diciamo che la  parola e' presente
    nella matrice se e' possibile ottenerla collezionando i caratteri
    che si incontrano con una serie di spostamenti tra celle adiacenti.
    I soli spostamenti permessi sono:
    a) da una cella alla cella adiacente a destra (D)
    b) da una cella alla cella in basso (B)
    la parola, se presente nella matrice, e'  individuata dalle coordinate
    di riga e colonna della cella da cui si parte e dalla stringa di 'D' e 'B'
    che denota la sequenza di spostamenti da effettuare per collezionare i suoi caratteri.

    Si consideri ad esempio la matrice

      ANTANDBER
      LNOANRLNT
      EIOSGEARO
      SSUNALSIC
      AANDEOAAO

    in questa matrice:
    'ANGELO' e' presente ed e' individuata da (1,3) e 'DGDGG'
    'ANDREA' e' presente ed e' individuata da (0,3) e 'DDGGD'
    'ENRICO' e' presente ed e' individuata da (0,7) e 'GGGDG'
    'ALESSANDRO', 'ANTONIO' e 'ALBERTO' sono parole non presenti.

    Abbiamo una matrice ed una lista di parole e vogliamo sapere quali sono presenti
    nella matrice e quali no.

    Progettare una funzione es1(ftesto) che preso l'indirizzo di un file
    di testo in cui e' registrata la matrice e la lista di parole da ricercare e
    restituisce una lista.
    Nella lista restituita all'i-esimo posto troviamo:
    - -1 se la parola non e' presente nella matrice.
    - la posizione dell'i-esima parola della lista nella matrice
      (vale a dire la terna (riga,colonna,s) con (riga,colonna) coordinate iniziali
      della cella d'inizio degli spostamenti ed s stringa che denota gli spostamenti).
      Nel caso la parola sia presente piu' volte nella matrice deve essere restituita
      la posizione piu' in alto  a sinistra in cui compare e nel caso compaia
      piu' volte a partire dalla stessa casella delle diverse stringhe che
      la individuano va presa quella che precede le altre lessicograficamente.

    Ad esempio, Per la matrice vista  sopra e la lista
    ['ALBERTO','ALESSANDRO','ANDREA', 'ANGELO', 'ANTONIO', 'ENRICO']
    la funzione es1 restituira' la lista
    [-1,-1,(0,3, 'DDGGD'),(1,3, 'DGDGG'),-1,(0,7, 'GGGDG')]

    Il file ftesto  contiene  la matrice  e, di seguito  l'elenco delle parole.
    Una serie di 1 o piu'  linee vuote precede la reppresentazione della matrice,
    separa il diagramma dall'elenco delle parole e segue l'elenco delle parole.
    La matrice  e' registrata per righe (una riga per linea e in linee consecutive) gli
    elementi di ciascuna riga sono adiacenti a formare una stringa.
    La lista delle parole occupa  invece linee consecutive con  una o piu' parole o
    separate da spazi per ciascuna linea.
    Per un esempio si veda il file esempio_Disney.pdf

    NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

    NOTA: almeno una delle funzioni realizzate DEVE essere ricorsiva, ad esempio
    potete scandire la matrice iterativamente e le lettere della parola cercata ricorsivamente.

    NON usate nessuna libreria.

    ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)

'''

def es1(ftesto):
  f = open(ftesto)
  fList = f.readlines()
  f.close()
  matrix, wordList = parseFile(fList)
  result = [-1 for x in range(len(wordList))]
  initDict = createDict(wordList)

  for row in range(len(matrix)):
    if len(initDict) > 0:
      for col in range(len(matrix[0])):
        initial = matrix[row][col]
        if initial in initDict:
          lista = initDict[initial]
          wSet = set()
          for word in lista:
            pathStr = searchWord(matrix, '', word, col, row, 0)
            if pathStr != None:
              result[wordList.index(word)] = (row, col, pathStr)
              wSet.add(word)
          if len(wSet) > 0:
            lSet = set(lista)
            lSet = lSet.difference(wSet)
            if len(lSet) > 0:
              initDict[initial] = list(lSet)
            else:
              del initDict[initial]
  return result



def parseFile(fileList):
  m = []
  wL = []
  idx = 0
  for i in range(len(fileList)): #skips empty lines
    line = fileList[i].strip()
    if len(line) > 0:
      idx = i
      break
  for i in range(idx, len(fileList)): #fills up the matrix
    line = fileList[i].strip()
    if len(line) > 0:
      m.append(list(line))
    else:
      idx = i
      break
  for i in range(idx, len(fileList)): #skips empty lines
    line = fileList[i].strip()
    if len(line) > 0:
      idx = i
      break
  for i in range(idx, len(fileList)): #fills up the wordList
    s = ''
    line = fileList[i]
    for c in range(len(line)):
      ch = line[c]
      if ch == ' ':
        if len(s) > 0:
          wL.append(s)
        s = ''
        continue
      if ch == '\n':
        if len(s) > 0:
          wL.append(s)
        s = ''
        break
      elif c == len(line) - 1:
        if len(s) > 0:
          wL.append(s + ch)
        s = ''
        break
      else:
        s += ch
  return m, wL


def createDict(wordList):
  initDict = {}
  for word in wordList:
    initDict.setdefault(word[0], [])
    initDict[word[0]].append(word)
  return initDict


def searchWord(matrix, pathStr, word, x, y, i):
  s1 = None
  s2 = None
  if (i == len(word) - 1):
    return pathStr
  else:
    if ((x < len(matrix[0]) - 1) and (matrix[y][x + 1] == word[i + 1])) and ((y < len(matrix) - 1) and (matrix[y + 1][x] == word[i + 1])):
      s1 = searchWord(matrix, pathStr + 'D', word, x + 1, y, i + 1)
      s2 = searchWord(matrix, pathStr + 'G', word, x, y + 1, i + 1)
    elif (x < len(matrix[0]) - 1) and (matrix[y][x + 1] == word[i + 1]):
      s1 = searchWord(matrix, pathStr + 'D', word, x + 1, y, i + 1)
    elif (y < len(matrix) - 1) and (matrix[y + 1][x] == word[i + 1]):
      s1 = searchWord(matrix, pathStr + 'G', word, x, y + 1, i + 1)

    if (s1 == None and s2 == None):
      return None
    elif s1 != None:
      return s1
    elif s2 != None:
      return s2
    else:
      return s1







if __name__ == '__main__':
  pass
    # inserite qui i vostri test
