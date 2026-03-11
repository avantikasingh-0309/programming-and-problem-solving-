def reverse_string(s):
	new_st =""
	length = len(s)
	for ch in range(length-1,-1,-1):
		new_st = new_st + s[ch]
	return new_st



user_input = input("Enter a string: ")
result = reverse_string(user_input)
print(f"Original String: {user_input}")
print(f"Reversed String: {result}")
