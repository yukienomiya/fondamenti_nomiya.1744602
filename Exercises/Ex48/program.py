import albero


def es48(tree):
    '''
    Si definisca la funzione es48(tree) ricorsiva (o che fa uso di funzioni o metodi ricorsive/i) che:
    - riceve come argomento 'tree' un  albero  formato da nodi di tipo
      AlberoBinario definito nella libreria albero.py allegata
    - calcola il numero di nodi che nell'albero hanno ESATTAMENTE due figli
    - torna come risultato il numero calcolato
    Esempio: se l'albero e':

             7
            /\
           1  3
          / \
        4    6
       /    /
      5    2
     /     \
    9       8

    Nell'albero ci sono solo due nodi con esattamente due figli (il nodo con valore 7 ed il nodo
    con valore 1) cosi'  la funzione tornera' il valore 2.
    '''
    return treeVisit(tree, 0)

def countOffspring(node):
  count = 0
  if (node.dx != None):
    count += 1
  if (node.sx != None):
    count += 1
  return count


def treeVisit(tree, count):
  if (countOffspring(tree) == 0):
    return count
  if (countOffspring(tree) == 1):
    if (tree.dx != None):
      return treeVisit(tree.dx, count)
    return treeVisit(tree.sx, count)
  else:
    return 1 + treeVisit(tree.dx, count) + treeVisit(tree.sx, count)
