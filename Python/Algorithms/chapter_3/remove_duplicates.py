def remove_duplicates(arr):
	location = 1
	for i in range(len(arr)):
		if arr[i] != arr[i+1]:
			arr[location] = arr[i+1]
			location+=1
	len(arr) = location - 1
	print arr

array = [1,2,2,3,3,4,4,5,5,6]
remove_duplicates(array)