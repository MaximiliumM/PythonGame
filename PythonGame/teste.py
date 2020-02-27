def word_count(text):
	
	result = {}
	words = text.lower().split()
	
	for word in words:
		
		if word in result:
			result[word] += 1
			
		else:
			result[word] = 1
			
	return result
	

result = word_count("The quick brown fox jumps over the lazy dog")

palavra = ""
quantidade = 0

for key, value in result.items():
	
	if value > quantidade:
		quantidade = value
		palavra = key
		
print(palavra)




