def ReturnZero(arr):
	for i in range(len(arr)):
		if arr[i]<0:
			arr[i]=0
	print arr

ReturnZero([5,8,-9, -200, 14])