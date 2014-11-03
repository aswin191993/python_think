t=[2,3,4,5]
def nested(t):
	sm=0
	for i in t:
		sm+=(i+1)
	return sm

print nested(t)
print "sum of t is:",sum(t)
