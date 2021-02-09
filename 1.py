#1.- ingreso de N
print('Ingrese un numero')
N=input('N=')
#2.- validacion de mayor a 1
while True:
	if N>1:
		break
	else:
		print('El numero no puede ser menor a 1')
#llega aqui solo si es mayor a 1
print('Avanzando...')
if N==2:
	print('El 2 Es el primer numero primo')
else:
	#verificando si es primo o no
	aux= 'Es primo'
	for i in range(2, N):
		if N%i == 0:
	          aux="No es primo"
              print(aux)
	#5.- Obteniendo los primos anteriores
	cont=0
	contPrimos=0
	sumaPrimos=0
	for n in range(1, N + 1):
    		for d in range(1, n + 1):
        		if n % d == 0:
            			cont += 1
    		if cont == 2:
			#6.- Contar Sumar de primos 2,N
        		sumaPrimos= sumaPrimos+n
			contPrimos += 1
			print('Numero Primo:',n)
    		cont = 0
print('Existen ',contPrimos,' en el intervalo')
#7.- promedio
promedio=(sumaPrimos+0.0)/contPrimos 
print('El promedio es: ',promedio)

