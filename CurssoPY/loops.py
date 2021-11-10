# i = 0
# while i  < 5:
#     i += 1
#     if i == 3:
#         continue
    # print(i) 


# usuarios = ["Chanchito Feliz", 'Felipe','Roberto','Nicolas']

# for Usuario in usuarios:
#     print(Usuario)

# usuario = 'Chanchito Feliz'
# for c in usuario:
#     print(c)

# usuarios = ["Chanchito Feliz", 'Felipe','Roberto','Nicolas']

# for Usuario in usuarios:
#     if Usuario == 'Felipe':
#         break
#     print(Usuario)

# usuarios = ["Chanchito Feliz", 'Felipe','Roberto','Nicolas']

# for Usuario in usuarios:
#     if Usuario == 'Felipe':
#         continue
#     print(Usuario)

# for x in range(3,30):
#     print(x)
# else: 
#     print('Ya terminado.')

# usuarios = ["Chanchito Feliz", 'Felipe','Roberto','Nicolas']
# edades = [24,25,26,27]

# for usuario in usuarios:
#     for edad in edades:
#         print(usuario,edad)


def miFuncion():
    print('Mi primera funcion.')

miFuncion()

def imprimeDato(*nombres):
    for nombre in nombres:
        print(nombre) #Dupla


imprimeDato('Rodrigo', 'Bonilla', 'Juan', 'Pedro')

def nombreCompleto(apellido, nombre):
    print(nombre,apellido)


#nombreCompleto(nombre= 'Rodrigo', apellido = 'Chanchito Feliz')

def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

nombreCompleto2(nombre= 'Rodrigo', apellido = 'Chanchito Feliz')


# def miFuncion2(argumento = 'chanchito'):
#     print('Mi primera funcion: ', argumento)

# miFuncion2('Batman')
def mifuncionLista(lista):
    for el in lista:
        print(el)

# mifuncionLista(['Chanchito','Feliz'])

def ConcatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + ' ' + el
    return i

# nombres = ConcatenaNombres(['Chanchito', 'Feliz'])
# print(nombres)

def recursion(i):
    if i < 1 :
        return i
    print(i)
    recursion(i-1)

Dato = recursion(5) 
print(Dato) 