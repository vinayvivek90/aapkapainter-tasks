array = input()
array = array.strip('[]').split(',')

temp = []
for value in array:
	if value not in temp:
		temp.append(value)
	elif value in temp:
		print(value)
		break
