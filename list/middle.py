def middle(t):
	a=len(t)
	new=[]
	if a%2 is 0:
		k=(a/2)-1
		new.append(t.pop(k))
		new.append(t.pop(k))
	else:
		k=(a/2)
		new.append(t.pop(k))
	print new

t=[1,2,3,4,5,6]
print "list:",t
middle(t)
