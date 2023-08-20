def binary_search(list, low, high, x):
	if high >= low:
		mid = (high + low) // 2
		if list[mid] == x:
			return mid
		elif list[mid] > x:
			return binary_search(list, low, mid - 1, x)
		else:
			return binary_search(list, mid + 1, high, x)
	else:
		return -1
	
list = [ 8, 18, 30, 54, 61 ]
x = 61
result = binary_search(list, 0, len(list)-1, x)
if result != -1:
	print("Element is present at index", {result})
else:
	print("Element is not present in array")
