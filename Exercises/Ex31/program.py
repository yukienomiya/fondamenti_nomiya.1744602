def es31(fname1,fname2):
  ''' 
  Implementate la funzione es31(fname1,fname2) che prende in input l'indirizzo di due  file di testo.
  Il testo del primo file va modificato come segue:
  - ciascun carattere tra 'a' e 'z' (minuscoli) che compare nel file in un numero dispari di parole
  (una parola e' una sequenza massimale di caratteri diversi dallo spazio, tab o a capo)
  va sostituito dal corrispondente carattere maiuscolo.
  Il file cosi' ottenuto va poi registrato all'indirizzo fname2.
  La funzione deve restituire quanti dei 26 caratteri tra 'a' e 'z' 
  da minuscoli son diventati maiuscoli nella trasformazione del file di testo. 
  Ad esempio se 
  - il file fname1 contiene  il testo 'Monti, Sterbini e Spognardi'
  - il file fname2 conterra' il testo 'MoNtI, SterBINI e SPoGNArDI'
  il valore restituito dalla funzione sara' 7 (le lettere cambiate sono NIBPGAD)
  '''
  res = ''
  f1 = open(fname1, 'r')
  f2 = open(fname2, 'w')
  text = f1.readlines()
  words = getWords(text)
  selectedLetters = getSelectedLetters(words)
  for line in text:
    for letter in line:
      if ((letter.islower()) and (letter in selectedLetters)):
        res += letter.upper()
        continue
      res += letter
  f2.write(res)
  f1.close()
  f2.close()
  return len(selectedLetters)

def getSelectedLetters(wordList):
  selectedLetters = set()
  letters = set()
  for word in wordList:
    for letter in word:
      if (letter.islower()):
        letters.add(letter)
  for letter in letters:
    count = 0
    for word in wordList:
      if (letter in word):
        count += 1
    if (count % 2 == 1):
      selectedLetters.add(letter)
  return selectedLetters

def getWords(lines):
  words = []
  for line in lines:
    line = line.strip()
    words += line.split()
  return words





















 