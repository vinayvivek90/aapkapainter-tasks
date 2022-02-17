word = input()
wordlist = word.split(' ')

if sorted(list(wordlist[0].lower())) == sorted(list(wordlist[1].lower())):
	print('Yes')
else:
	print('No')