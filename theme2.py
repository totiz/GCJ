numCase = input()

def pCase(case, output):
  print "Case #%d: %s" % (case, output)


for round in range(numCase):
  Round, hold, NumPeo = map(int, raw_input().split())
  Groups = map(int, raw_input().split())
  
  Prevs_r = []
  Prevs_g = []
  Prevs_p = []
  
  allPrice = 0
  
  ii = 0
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
  
    if Groups in Prevs_g:
      index = Prevs_g.index(Groups)
      
      thisPrice = allPrice
      beforePrice = Prevs_p[index]
      difPrice = thisPrice - beforePrice
      
      remain = Round - (ii + 1)
      diff_index = ii - index
      remain_mod = remain % diff_index
      finalPrice = allPrice + (remain / diff_index) * difPrice + ( Prevs_p[index + remain_mod] - Prevs_p[index] )
      allPrice = finalPrice
      break
    
    Prevs_r.append(ii)
    Prevs_g.append(Groups[:])
    Prevs_p.append(allPrice)
#print "remain %d" % remain

  pCase(round+1, allPrice)