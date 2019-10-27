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
  array = list(range(len(lista2)))
  dLList = DoublyLinkedList()

  for i in lista2: #create the dLList and fill the array
    node = Node(i)
    dLList.append(node)
    array[i - 1] = node

  for event in lista1: #for each event
    node = array[int(event[1:]) - 1]
    if event[0] == 'e':
      dLList.remove(node)
      node = None
    elif event[0] == 's':
      dLList.swap(node)

  finalList = []
  n = dLList.head
  while (n != None): #fill the finalList
    finalList.append(n.val)
    n = n.next
  return finalList





class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, node):
    if self.head == None:
      self.head = node
    else:
      node.prev = self.tail
      self.tail.next = node
    self.tail = node

  def remove(self, node):
    if self.head.next == None: #if the list contains just one node
      self.head = None
    elif self.head == node: #if the node that has to be removed is the head
      self.head = node.next
      self.head.prev = None
    else:
      if node.next != None:
        node.prev.next = node.next
        node.next.prev = node.prev
      else: #if the node that has to be removed is the tail
        node.prev.next = None

  def swap(self, node): #swap the node with the next one
    prevX = node.prev
    y = node.next
    if self.head == node: #if the node being switched is the head
      if y.next == None: #if the linkedlist is two-nodes long
        node.next = None
      else:
        node.next = y.next
        y.next.prev = node
      node.prev = y
      y.next = node
      y.prev = None
      self.head = y

    else: #if the node being swithed is in the middle
      if y.next == None: #if the node is the second-to-last
        node.next = None
      else:
        node.next = y.next
        y.next.prev = node
      prevX.next = y
      y.prev = prevX
      y.next = node
      node.prev = y



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



if __name__ == '__main__':
    pass
    # inserisci qui i tuoi test personali
