array = ["teste", "whatever", "oi", "teste", "oi"]

print(len(array))

def check(string, test):
	if string in array:
		print("Entry found.")
	else:
		print("No entry.")

check("te2te", False)

