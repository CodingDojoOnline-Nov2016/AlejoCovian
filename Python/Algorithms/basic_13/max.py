arr = ['hi', 'array', 'this', 'is', 'fun', 'pneumonovolcanic']
arrindex = ''
for i in range(0, len(arr)):
	if len(arr[i])>len(arrindex):
		arrindex = arr[i]
print arrindex