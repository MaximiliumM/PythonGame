nomes = ["Felipe", "Lucas", "Guilherme", "Marcos", "Bruno", "Leonardo"]

# DESCOBRIR QUANTOS NOMES DA LISTA QUE TEM MAIS DE 6 LETRAS
contador = 0

for nome in nomes:
	
	if len(nome) > 6:
		contador += 1
		
print(contador)

