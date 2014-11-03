l=[1,2,3,4,5,6]
def chop(l):
	del l[0],l[len(l)-1]
	print l

print "list:",l
chop(l)
