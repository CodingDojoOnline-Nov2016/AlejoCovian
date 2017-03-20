def function(arr):
	max = 0
	sum = 0
	min = arr[0]
	for i in range(len(arr)):

		if arr[i]>max:
			max = arr[i]

		if arr[i]<min:
			min = arr[i]

		sum += arr[i]
		if i>0:
			avg = sum / int(i)

	print max
	print min
	print avg


function([6,1,7,2,21,6,3,9])