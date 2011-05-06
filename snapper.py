numCase = input()

def pCase(case, output):
  print "Case #%d: %s" % (case, output)

for round in range(numCase):
  N, K = map(int, raw_input().split())
  ans = pow(2,N)
  
  div = (K + 1) / ans
  if ans * div == K + 1:
    pCase(round+1, "ON")
  else:
    pCase(round+1, "OFF")