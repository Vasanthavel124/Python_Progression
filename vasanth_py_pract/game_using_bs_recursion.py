def machine(low,high):
	mid = (low+high)//2
	print(f"is the number {mid}?")
	input1 = input("Type higer, lower, yes :")
	if input1 == 'yes':
		print(f"Guessed the number {mid}")
	elif input1 == 'high':
		machine(mid+1,high)
	elif input1 == 'low':
		machine(low,mid-1)
		
machine(1,100)
