
'''    
Es 3: 3 punti
due parole possono fondersi se la prima ha un suffisso di almeno due caratteri 
che coincide col prefisso di pari lunghezza della seconda. 
Il risultato della fusione e' la parola che si ottiene concatenando la prima parola 
con la seconda grazie alla parte comune.
Ad esempio:  
- le due parole 'candela' ed 'elastico' possono fondersi grazie al suffisso 
  'ela' di  3 caratteri, il risultato della fusione e' la parola  'candelastico' 
_ le parole 'Angelo' e 'gelo' possono fondersi grazie al suffisso 'gelo', la parola 
  risultante e''Angelo'. 
_ le parole 'aaaaa' e 'aaab' possono fondersi in diversi, modi: 
    _ grazie al suffisso 'aa' si ottiene la fusione 'aaaaaab' 
    _ grazie al suffisso 'aaa' si ottiene la fusione 'aaaaab'.
  Si definisca la  funzione es2(insieme) che, dato un insieme di parole, restituisce 
  la lista con tutte le possibili fusioni. 
  La lista deve risultare ordinata lessicograficamente e vanno eliminati eventuali 
  duplicati.
  
ESEMPIO: 
se  insieme={  'aaaa', 'acde', 'aacd', 'aaaade'} la funzione restituira' la lista: 
['aaaaaade', 'aaaaade', 'aaaacd', 'aaaade', 'aacde'] 
grazie alle seguenti fusioni:
'aaaa'  'aaaade' ---> 'aaaaaade' con suffisso 'aa'
'aaaa'  'aaaade' ---> 'aaaaade'  con suffisso 'aaa'
'aaaa'  'aaaade' ---> 'aaaade'   con suffisso 'aaaa'
'aaaa'  'aacd'   ---> 'aaaacd'   con suffisso 'aa'
'aacd'  'acde'   ---> 'aacde'    con suffisso 'acd'
'''
def es8(insieme):
  prefixDict, suffixDict = getPrefixSuffixDict(insieme)
  setFusion = set()
  for word1 in suffixDict:
    for word2 in prefixDict:
      if (word1 != word2):
        commonSubstr = suffixDict[word1].intersection(prefixDict[word2])
        if (len(commonSubstr) > 0):
          setFusion = setFusion.union(getFusionWords(word1, word2, commonSubstr))
  result = list(setFusion)
  result.sort()
  return result


def getFusionWords(word1, word2, fusionSet):
  fusionWords = set()
  for f in fusionSet:
    l = len(f)
    w = word1 + word2[l:]
    fusionWords.add(w)
  return fusionWords

def getPrefixSuffixDict(wordSet):
  prefixDict = dict()
  suffixDict = dict()
  for word in wordSet:
    prefixSet = set()
    suffixSet = set()
    for i in range(2, len(word) + 1):
      prefixSet.add(word[:i])
    for i in range(len(word) - 1):
      suffixSet.add(word[i:])
    prefixDict[word] = prefixSet
    suffixDict[word] = suffixSet
  return prefixDict, suffixDict