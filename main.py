def fatorial():
	print("insira um numero")
	num = int(input())
	cont = 2
	fatorial = 1
	while cont <= num:
		fatorial = fatorial * cont
		cont = cont +1
	
	print(fatorial)


fatorial()