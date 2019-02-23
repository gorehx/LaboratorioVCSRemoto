a=float(input("Ingrese el número a:"))
b=float(input("Ingrese el número b:"))
c=float(input("Ingrese el número c:"))
d=(((b*2)-(4*a*c))*(1/2))
neg=(((-1*b)-(d**(1/2))/2*a))
pos=(((-1*b)+(d**(1/2))/2*a))
if d>0:
 print( "La parte negativa es: ", neg , "y la parte postiva es: ", pos)
else:
	if d==0:
		print("El valor negativo: ", (-d/2*a), "es igual al valor positivo, el cual es:", (-d/2*a))
	else:
		if d<0:
			print("No existe solucion en los numeros reales")
