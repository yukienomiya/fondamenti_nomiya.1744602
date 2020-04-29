import immagini
import json

def es23(fileJson, filePng):
  '''
  Abbiamo un file di tipo json contenente una matrice (lista di liste) M i cui elementi 
  sono stringhe. La matrice e' il risultato della codifica di un'immagine.
  L'immagine ha ampiezza w e altezza h dove w e' il numero di colonne della matrice M e h 
  il numero di righe. Il colore (r,g,b) del  pixel di coordinate x,y e' codificato con 
  la stringa presente in M[y][x], piu' precisamente la stringa e' composta da 9 cifre. 
  Le tre piu' significative sono la codifica di r, le tre centrali sono la codica di g e le tre 
  meno significative la codifica di b.  

  Scrivete la funzione es7(fileJson, filePng) che riceve come argomenti:
      :param fileJson: il path del file json dove si trova la matrice dell'immagine codificata
      :param filePng:  il path del file PNG dove salvare l'immagine decodificata.
      :return: il colore che appare piu' spesso tra quelli dei pixel dell'immagine (a parita'
      viene selezionato il colore che precede nell'ordinamento crescente 
      rispetto alla prima, alla seconda e poi alla terza coordinata).
  '''
  f = open(fileJson, 'r')
  matrix = json.load(f)
  f.close()
  img = []
  occurrencesDict = dict()
  for row in range(len(matrix)):
    imgRow = []
    for col in range(len(matrix[0])):
      pixelStr = matrix[row][col]
      pixel = (int(pixelStr[:3]), int(pixelStr[3:6]), int(pixelStr[6:9]))
      occurrencesDict[pixel] = occurrencesDict.get(pixel, 0) + 1
      imgRow.append(pixel)
    img.append(imgRow)
  immagini.save(img, filePng)

  occ = list(sorted(sorted(occurrencesDict.keys()), key = occurrencesDict.get, reverse = True))
  return occ[0]