numCase = input()

def pCase(case, output):
  print "Case #%d: %s" % (case, output)

def runOver(Groups, hold, output):
  oriGroups = Groups[:]
  numRun = 0
  allPrice = 0
  while 1 == 1:
    countGroup = 0
    PeoThisRound = 0
    for eachGroup in Groups:
      if PeoThisRound + eachGroup <= hold:
        PeoThisRound += eachGroup
        countGroup += 1
      else:
        break
    
    # new Groups
    Groups = Groups[countGroup:] + Groups[0:countGroup]
    allPrice += PeoThisRound
    numRun += 1
    if Groups == oriGroups:
      output.append(allPrice)
      output.append(numRun)
      exit

for round in xrange(numCase):
  Round, hold, NumPeo = map(int, raw_input().split())
  Groups = map(int, raw_input().split())
  
  allPrice = 0
  for ii in xrange(Round):
    countGroup = 0
    PeoThisRound = 0
    for eachGroup in Groups:
      if PeoThisRound + eachGroup <= hold:
        PeoThisRound += eachGroup
        countGroup += 1
      else:
        break
    
    # new Groups
    Groups = Groups[countGroup:] + Groups[0:countGroup]
    allPrice += PeoThisRound

  pCase(round+1, allPrice)