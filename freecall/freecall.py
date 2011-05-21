

def run(  ):
	N, Pd, Pg = map(int, raw_input().split())
	
	if Pg == 100 and Pd != 100:
		return "Broken"
	if Pg == 0 and Pd != 0:
		return "Broken"
	if Pd == 0:
		return "Possible"
	
	for i in xrange(100):
		D = i + 1
		if D > N:
			return "Broken"
		if (D * Pd) % 100 == 0:
			return "Possible"
		
numCase = input()
for round in xrange(numCase):
	print "Case #%d: %s" % (round + 1, run())