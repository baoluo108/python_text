# python_text

import math

def AnagramSolution1(s1,s2)
alist = list(s2)
pos1 = 0
stillok = True
while pos1 < len(s1) and stillok:
  pos2 = 0
  found = False
  while pos2 < len(s2) and not found:
    if s1[pos1] == s2[pos2]:
      found = True
    else:
      pos2 = pos2 + 1
    if found:
      alist[pos2] = None
    else:
      stillok = False
    pos1 = pos1 + 1
return stillok

AnagramSolution1(earth,retrh)
