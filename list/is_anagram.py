def is_anagram(t1,t2):
	if t1 is t2:
		return True
	else:
		a1=list(t1)
		a2=list(t2)
		l=len(t1)-1
		rl=range(l)
		for i in rl:
			if a1[i]==a2[i]:
				True
			else:
				a1[i]=a2[i]
		f=''
		j1=f.join(a1)
		j2=f.join(a2)
		print t1,"&",t2		
		print j1,"&",j2
	return True

t1='wswin'
t2='aswin'

print is_anagram(t1,t2)

		
