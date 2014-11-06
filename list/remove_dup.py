a='aswin','ravi','appu','arun','aswin','ravi'

def remove_dup(a):
	s=list(a)
	l=len(s)-1
	r=range(l)
	p=[]
	for i in r:
		if s[i] not in p:
			p.append(s[i])
	print "orginal list:",a
	print p

remove_dup(a)
