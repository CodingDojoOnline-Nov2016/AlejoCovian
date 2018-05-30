# def odd_even():
#     for x in range(1,2001):
#         if x % 2 == 0:
#             print( x, "this is an even number.")
#         else:
#             print( x, "this is an odd number.")
#
# odd_even()

def multiply(arr, num):
    for x in range(0, len(arr)):
        arr[x] *= num
    return arr

numbers_array = [3,6,8,10,67]
print (multiply(numbers_array, 5))

def layered_multiples(arr):
    print (arr)
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print (x)
