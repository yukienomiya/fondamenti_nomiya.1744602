'''
Si e' appena svolta una gara automobilistica con n piloti aventi per identificativi
gli interi 1,2...n.
Nel corso della gara assistiamo a due tipi di eventi:
- il pilota i viene superato dal suo immediato inseguitore
  (questo evento e' segnalato tramite una stringa 's'+str(i))
- il pilota i abbandona la gara
  (questo evento e' segnalato dalla stringa 'e'+str(i))
Disponiamo di una  lista lista1 in cui sono raccolti sotto forma di stringhe e in ordine
temporale di occorrenza i due tipi di eventi:
-una stringa 's'+str(i) indica che il pilota i e' stato superato del suo immediato inseguitore.
-una stringa 'e'+str(i) indica che il pilota i abbandona la gara.
Disponiamo anche di una lista lista2 che riporta gli identificativi dei piloti nell'ordine
in cui appaiono alla griglia di partenza ( in   lista2[i], 0<=i<n, troviamo
l'identificativo del pilota che occupa l'i-ma posizione nella griglia di partenza).
Quindi il primo è in posizione 0.
Vogliamo ottenere una lista lista3 che riporti l'ordine d'arrivo  dei  piloti che portano a termine la gara
(se m piloti portano a termine la gara la lista lista3 avra' lunghezza m ed
 lista3[i] sara' l'identificativo del pilota che nella gara arriva in posizione i-1).

Progettare una funzione es(lista1,lista2) che date
-lista 1: la lista dei due tipi di  eventi che si sono verificati nel corso della gara
-lista 2: la lista con le posizioni di partenza dei piloti
restituisce la lista contenente  gli identificativi dei  piloti che portano a termine la gara
in ordine di arrivo crescente.
Attenzione, al termine dell'esecuzione della funzione le  liste lista1 e lista2 non  devono
risultare modificate.

Ad esempio nel caso di:
lista1=['e2','s4','s3','s3','e1','s5'] e lista2=[5,3,2,4,1] i 6 eventi determinano i
seguenti 6 cambiamenti nell'ordine di graduatoria:

5 ->e2-> 5 ->s4-> 5 ->s3-> 5 ->s3-> 5 ->e1-> 5->s5->4
3        3        3        1        1        4      5
2        4        1        3        4        3      3
4        1        4        4        3
1

la funzione deve dunque restituire la lista [4,5,3]

NOTA: è VIETATO usare/importare ogni altra libreria a parte quelle già presenti

NOTA: il timeout previsto per questo esercizio è di 1.5 secondi per ciascun test (sulla VM)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)

'''

def es(lista1, lista2):
  array = list(range(1, len(lista2) + 1))

  dLList = Node(lista2[0]) #riempio la doubly linkedlist e l'array di puntatori
  cur = dLList
  array[lista2[0] - 1] = cur #nella posizione i ci sarà il puntatore del pilota i + 1
  for x in range(1, len(lista2)):
    cur.next = Node(lista2[x])
    cur.next.prev = cur
    cur = cur.next
    array[lista2[x] - 1] = cur

  for event in lista1: #for each event
    idPilot = int(event[1:])
    if event[0] == 'e':
      dLList = exitPilot(idPilot, array, dLList)
    elif event[0] == 's':
      dLList = switchPilots(idPilot, array, dLList)

  n = dLList
  finalList = []
  while (n != None): #fill the finalList
    finalList.append(n.val)
    n = n.next
  return finalList



class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

  def __iter__(self):
    here = self
    while here:
      yield here.val
      here = here.next


def exitPilot(pilotNumber, array, dLList): #the return value is the updated head of the linkedList
  x = array[pilotNumber - 1]
  prevX = x.prev
  y = x.next
  if prevX == None: #if x is the head
    if y == None: #if x is the last node in the linked list
      return None #the dLList's head has to be set to None
    else:
      y.prev = None
      return y
  elif y == None: #if x is the tail
    prevX.next = None
  else:
    prevX.next = y
    y.prev = prevX
  array[pilotNumber - 1] = None
  return dLList

def switchPilots(pilotNumber, array, dLList):
  x = array[pilotNumber - 1] #the one being surpassed
  prevX = x.prev
  y = x.next
  nextY = y.next
  if prevX == None: #if the node being switched is the head
    if nextY == None: #and the next one is the tail (the linkedlist in two-nodes long)
      x.next = None
    else:
      x.next = nextY
      nextY.prev = x
    x.prev = y
    y.next = x
    y.prev = None
    return y #if the dLList's head has to be updated (with the next node)

  else: #if the node being swithed is in the middle
    if nextY == None: #and the next one in the tail
      x.next = None
    else:
      x.next = nextY
      nextY.prev = x
    prevX.next = y
    y.prev = prevX
    y.next = x
    x.prev = y
  return dLList



if __name__ == '__main__':
    pass
    # inserisci qui i tuoi test personali
