# INCOMPLETE

arr = [4, 2, 6, 1, 3, 5, 7, 0]
for i in arr:
	if arr[i] > arr[i - 1]:
		temp = arr[i]
		arr[i] = arr[i-1]
		arr[i-1] = temp
	print arr