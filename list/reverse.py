a='aswin','appu','rahul','sfds','aspop','uppa','niwsa'

def reverse(a):
	s=list(a)
	l=len(s)
	r=range(l)
	n=[]
	for i in s:
		k=list(i)
		p=k[::-1]
		f=''
		t=f.join(p)
		if t in a:
			n.append(i)
	print "list:",a
	print n

	
reverse(a)
