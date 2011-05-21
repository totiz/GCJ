numCase = input()

def pCase(case, output):
  print "Case #%d: %.6f" % (case, output)


for round in range(numCase):
  N = input()
  list1 = [int(x)-1 for x in raw_input().split()]
  
  count = 0
  list1_sort = list1[:]
  list1_sort.sort()
  while list1 != list1_sort:
    for i in range(N):
      if list1[i] != i:
        index = list1.index(i)
        #swap
        tmp = list1[i]
        list1[i] = list1[index]
        list1[index] = tmp
        count += 1
        break

  pCase(round+1, count * 2 )