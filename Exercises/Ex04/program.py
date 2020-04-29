import immagini

def es4(fimm, fimm1, h1, w1):
  '''
  Si definisca la  funzione es4(fimm,fimm1) che, 
  - riceve gli  indirizzi fimm e fimm1 di due file .PNG. e due interi h1 e w1 maggiori di zero.
  - legge l'immagine da fimm e crea una seconda  immagine. L'immagine da creare 
    ha h1 volte la lunghezza di quella letta e w1 volte la larghezza di quella letta e si ottiene 
    sostituendo ad ogni pixel dell'immagine letta un rettangolo di pixels di altezza h e ampiezza w aventi 
    tutti il colore del pixel originario.
  - salva l'immagine creata all'indirizzo fimm.
  - restituisce la tupla con il colore che compare piu' spesso nell'immagine letta e in 
  caso di parita' di occorrenze massime il colore del pixel che viene prima lessicograficamente.
  Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
  '''
  img = immagini.load(fimm)
  newImg = []
  occurrencesDict = dict()

  for row in range(len(img)):
    newRow = []
    for col in range(len(img[0])):
      pixel = img[row][col]
      occurrencesDict[pixel] = occurrencesDict.get(pixel, 0) + 1
      for i in range(w1):
        newRow.append(pixel)
    for i in range(h1):
      newImg.append(newRow)
  immagini.save(newImg, fimm1)

  occ = list(sorted(sorted(occurrencesDict.keys()), key = occurrencesDict.get, reverse = True))
  return occ[0]
