# -*- coding: utf-8 -*-
'''
    In un immagine a sfondo nero  e' disegnata  una griglia
    dove  alcuni segmenti che ne connettono i nodi in orizzontale
    o in verticale sono stati cancellati (i nodi della griglia sono in
    verde mentre i segmenti sono in rosso).
    La dimensione del lato dei quadrati della griglia non è data.

    Si veda ad esempio la figura foto_1.png.
    Progettare la funzione es1(fimm, k) che prende in input l'indirizzo
    dell'immagine contenente la griglia ed un intero k e restituisce un intero.
    L'intero restituito e' il numero di
    quadrati rossi (con pixel verdi) di lato k (steps della griglia) che sono presenti nell'immagine.
    Ad esempio  es1(foto_1.png,2) deve restituire 2 (i due quadrati rossi presenti nella
    sottogriglia hanno il vertice in alto a sinistra con coordinate (3,0) e
    (4,2) nelle coordinate della griglia, rispettivamente)

    Per caricare e salvare  file PNG si possono usare load e save della libreria immagini allegata.

    NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

    ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)

'''
import immagini

def es1(fimm,k):
  count = 0
  img = immagini.load(fimm)
  red = (255, 0, 0)

  if hasGrid(img):
    grid, side = getGrid(img)
  else:
    return 0

  for r in range(0, len(grid) - (k * (side + 1)), side + 1):
    for c in range(0, len(grid[0]) - (k * (side + 1)), side + 1):
      x, y = c, r
      xUR = c + k * (side + 1)
      yBL = r + k * (side + 1)
      for idx in range(k):
        if (grid[r][x + 1] == grid[y + 1][c] == grid[y + 1][xUR] == grid[yBL][x + 1] == red):
          if idx == k - 1:
            count += 1
          else:
            x += side + 1
            y += side + 1
        else:
          break

  return count








def hasGrid(img):
  green = (0, 255, 0)
  red = (255, 0, 0)

  # checks that the image actually contains a grid
  bG = False
  bR = False
  for row in img:
    if green in row:
      bG = True
      break
  for row in img:
    if red in row:
      bR = True
      break

  return (bG and bR)




def getGrid(img):
  l = 0
  rows = len(img)
  columns = len(img[0])
  grid = []
  green = (0, 255, 0)
  black = (0, 0, 0)
  startX = startY = endX = endY = 0

  # finds the coordinates of the first pixel of the grid (up left)
  b = False
  for idxR in range(rows):
    for idxP in range(columns):
      if img[idxR][idxP] == green:
        startX, startY = idxP, idxR
        b = True
        break
    if b:
      break

  # finds l - the length of the side of the square
  if img[startY].count(green) > 1:
    for idxP in range(startX + 1, len(img[0])):
      if img[startY][idxP] == green:
        break
      else:
        l += 1
  else:
    for idxR in range(startY + 1, len(img)):
      if img[idxR][startX] == green:
        break
      else:
        l += 1

  next = l + 1
  # finds the x coordinate of the up right-most pixel of the grid
  for idxP in range(startX, len(img[0]), next):
    if ((img[startY][idxP] == green) and ((idxP + next  >= len(img[0])) or (img[startY][idxP + next] == black))):
      endX = idxP
      break

  # finds the y coordinate of the bottom left-most pixel of the grid
  for idxR in range(startY, len(img), next):
    if ((img[idxR][startX] == green) and ((idxR + next >= len(img)) or (img[idxR + next][startX] == black))):
      endY = idxR
      break

  # creates a new grid
  for idxR in range(startY, endY + 1):
    row = img[idxR]
    grid.append(row[startX:endX + 1])

  return grid, l



if __name__ == '__main__':
    pass
    # inserisci qui i tuoi test
