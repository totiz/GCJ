numCase = input()

def pCase(case, output):
  print "Case #%d: %s" % (case, output)


for round in xrange(numCase):
  ainput = raw_input().split()
  
  orange = []
  blue = []
  
  index = 1
  for ii in xrange(int(ainput[0])):
    color = ainput[index]
    pos = ainput[index + 1]
    
    if color == 'O':
      orange.append([index/2, int(pos) ])
    else:
      blue.append([index/2, int(pos) ])
    
    index += 2


  blue_cur = 1
  orange_cur = 1
  timere = 0
  while orange != [] or blue != []:
    action = 0
    if orange != []:
      orange_order = orange[0][0]
      orange_pos = orange[0][1]
    else:
      orange_order = 100000000009000
      orange_pos = -1
    
    if blue != []:
      blue_order = blue[0][0]
      blue_pos = blue[0][1]
    else:
      blue_order = 100000000009000
      blue_pos = -1

    if orange_pos != -1:
      if orange_cur != orange_pos:
        if orange_cur < orange_pos:
          orange_cur += 1
        else:
          orange_cur -= 1
      elif orange_order < blue_order:
        orange = orange[1:]
        action = 1
      
    
    if blue_pos != -1:
      if blue_cur != blue_pos:
        if blue_cur < blue_pos:
          blue_cur += 1
        else:
          blue_cur -= 1
      elif blue_order < orange_order and action == 0:
        blue = blue[1:]


    timere += 1
  pCase(round + 1, timere)
    
    