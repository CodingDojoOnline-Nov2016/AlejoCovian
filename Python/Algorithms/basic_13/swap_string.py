def SwapString(arr):
	for i in range(len(arr)):
		if arr[i] < 0:
			arr[i] = "Dojo"
	print arr

SwapString([2,5,-9, 8, -14])