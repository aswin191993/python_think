
p=7
w="cheer"
def rotateword(w,p):
	pr=""
	a="abcdefghijklmnopqrstuvwxyz"
	for i in w:
		k=range(25)
		for j in k: 
			if i is a[j]:
				 pr=pr+a[j+p]
	print pr
rotateword(w,p)
