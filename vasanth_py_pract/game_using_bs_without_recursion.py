low =  1
high = 100
while True:
	mid = (low+high)//2
	print(f"is the number {mid}?")
	input1 = input("Type higer, lower, yes :")
	if input1 == 'yes':
		print(f"Guessed the number {mid}")
		break
	elif input1 == 'high':
		low = mid + 1
	elif input1 == 'low':
		high = mid -1