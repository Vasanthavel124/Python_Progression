def binary_search(list, x):
	low = 0
	high = len(list) - 1
	mid = 0

	while low <= high:
		mid = (high + low) // 2
		if list[mid] < x:
			low = mid + 1
		elif list[mid] > x:
			high = mid - 1
		else:
			return mid
	return -1

list = [ 8, 18, 30, 54, 61 ]
x = 54
result = binary_search(list, x)
if result != -1:
	print("Element is present at index", {result})
else:
	print("Element is not present in array")
