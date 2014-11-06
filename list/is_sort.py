def is_sort(t):
	p=len(t)-1
	k=range(p)
	for i in k:
		if t[i]<=t[i+1]:
		 	True
		else:
			return False
	return True
t=[1,2,2,4]
print is_sort(t)
