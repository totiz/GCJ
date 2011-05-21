from itertools import combinations

numCase = input()

def pCase(case, output):
  print "Case #%d: %s" % (case, output)

def addChild(pile):
  ans = 0
  for candy in pile:
    ans = ans ^ candy
  return ans

for round in xrange(numCase):
  myMaxAns = -1
  N = input()
  Ci = map(int, raw_input().split())
  
  for i in xrange(1, (N/2)+1):
    allCombi = combinations(Ci, i)
    for pile1 in allCombi:
      pile2 = Ci[:]
      for candy1 in pile1:
        pile2.remove(candy1)
      
      child1 = addChild(pile1)
      child2 = addChild(pile2)
      if child1 == child2:
        myMax = max( sum(pile1), sum(pile2) )
        myMaxAns = max( myMaxAns, myMax)
    if myMaxAns != -1:
      break
  
  if myMaxAns == -1:
    ans = 'NO'
  else:
    ans = myMaxAns
  pCase(round+1, ans)
      