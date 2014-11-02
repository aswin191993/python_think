# here the vale of length of both words are same.
# but in array operation len(w1 or w2) . will taken out of range.
# eg:- len of 'apple' is 5. w1[5] can't working array start from 0 to (length -1).

w1='apple'
w2='elppa'

def revs(w1,w2):
	i=0
	p=len(w2)
	j=p-1
	k=len(w1)
	if p!=k:
		return False
	while j>=0:
		if w1[j]==w2[i]:
			i=i+1
			j=j-1
		else:
			return False
	return True

print revs(w1,w2)

 		
