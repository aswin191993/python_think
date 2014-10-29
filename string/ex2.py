sfix='JKLMNOPQ'
suf='ack'
sufx='uack'
k= len(sfix)
for ltr in sfix:
	if 'O' and 'Q' in ltr:
		print ltr+sufx
	else:
		print ltr+suf	

