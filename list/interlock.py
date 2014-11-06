def interlock(w1,w2):
	l1=list(w1)
	l2=list(w2)
	n=[]
	ln=len(w1)-1
	r=range(ln)
	for i in r:
		n+=w1[i]
		n+=w2[i]
	f=''
	org=f.join(n)
	print "word1:",w1,"word2:",w2
	print org

w1='shoe'
w2='cold'

interlock(w1,w2)
