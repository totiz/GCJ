numCase = input()

def jCase(case):
  print "Case #%d: " % (case),

def pCase(case, output):
  print "Case #%d: %s" % (case, output)


for round in xrange(numCase):
  allin = raw_input().split()
  
  combiFrom = []
  combiTo = []
  opp = []
  
  index = 0
  C = int(allin[index])
  index += 1
  for i in xrange(C):
    combiFrom.append( allin[index][0:2] )
    combiTo.append( allin[index][2] )
    index += 1
  
  D = int(allin[index])
  index += 1
  for i in xrange(D):
    opp.append(allin[index])
    index += 1

  index += 1
  seq = allin[index]
  
  #print 'allin', allin
  #print 'combiFrom', combiFrom
  #print 'combito', combiTo
  #print 'opp', opp
  #print 'seq', seq

  board = []
  while seq != '':
    board += seq[0]
    seq = seq[1:]

    if len(board) > 1:
      a = board[-1]
      b = board[-2]
      
      #print 'befor: ', board
      action = 0
      for com in [b + a, a + b]:
        if com in combiFrom:
          index = combiFrom.index(com)
          board = board[:-2]
          board += combiTo[index]
          action = 1
          break
    #print 'after: ', board

      if action == 0:
        for char in board[:-1]:
          for com in [a + char, char + a]:
            if com in opp:
              board = []


  output = ''
  output += '['
  if len(board) >= 1:
    if len(board) == 1:
      output += board[0]
    else:
      output += board[0]
      for char in board[1:]:
        output += ', ' + char
  output += ']'

  pCase(round+1, output)
  