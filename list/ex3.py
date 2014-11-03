t=[1,2,3,4,5]

def cumulative(t):
	list=[]
	s=0
	for j in t:
		s=s+j
		list.append(s)
	print list

print "list of elements:",t
cumulative(t)	
