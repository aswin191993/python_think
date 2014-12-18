def histogram(word):
	dic={}
	for letter in word:
		dic[letter] = dic.get(letter,0) + 1
	return dic
print histogram('brontosaurus')
