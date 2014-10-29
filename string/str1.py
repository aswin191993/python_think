fruit = 'banana'
def rev(fruit):
	p=len(fruit)-1
	ptr=range(p)
	c=ptr[::-1]
	for i in c:
		print fruit[i]


rev(fruit)
