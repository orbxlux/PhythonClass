#dato = input("ingrede dato: ")
#lista = ["hola","Mundo","Chanchito","Feliz","dragones"]
#if lista.count(dato) > 0:
 #   print("El dato existe: ", dato)
#else:
    #print("El dato no existe", dato)


primero = input("Ingrese primer numero: ")




try:
    primero = int(primero)
except:
    primero = 'Chanchito feliz'

if primero == "Chanchito feliz":
    print("El valor ingresado no es un entero.")
    exit()




segundo  = input("Ingrese segundo numero: ")



try:
    segundo = int(segundo)
except:
    segundo = 'Chanchito feliz'

if segundo == "Chanchito feliz":
    print("El valor ingresado no es un entero.")
    exit()


simbolo = input('Ingrese operacion: ')
if simbolo == '+':
    print("Suma: ",primero + segundo)
elif simbolo == '-':
    print('Resta: ',primero - segundo)
elif simbolo == '*':
    print('Multiplicacion: ' , primero * segundo)
elif simbolo == '/':
    print('Division: ',primero/segundo)
else: 
    print("Simbolo no adecuado. Ingrese nuevamente")
    



