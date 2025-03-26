'''
TIPOS DE DATOS
strings: Cadena de texto <class 'str'>
'''
dato= "Enca24"
dato_2='Enca24'

print(type(dato))
print(type(dato_2))

#concatenacion de string
texto_1="programa "
texto_2="desarrollador junior"
enunciado=texto_1 + texto_2
print(enunciado)
#indexacion de string
#la indexacion se refiere acceder a un elemento de una cadena en una posicion
nombre="Andres Felipe"
#       012345
print(nombre[0])
'''
python es un lenguaje indexado en cero
'''
print(nombre[5])
print(nombre[-3])

#slicign de cadenas (porcion de la cadena)
# print(nombre[0:3]) # esta forma de porcionar no incluye el extremo derecho
# print(nombre[2:4])
# print(nombre[0:-5])
nombre="Andres F e l i p e"
    #            -6 -5 -4 -3 -2 -1


'''
tipos de datos numericos
<class 'int'> : se refiere a numeros enteros
<class 'float'> : se refeiere a numeros flotantes que continuen decimales
'''
x=5
print(type(x))
y=5.0
print(type(y))

'''
datos boolean
1,0 o falso / verdadero
<class 'bool>
True
False
'''
asistencia=False
print(type(asistencia))
print (not asistencia)

'''
TIPOS DE ESTRUCTURAS Y METODOS
sets : se define en python con {,,,,}
tuplas: se definen en python con (,,,,,)
listas: se definen en python con [,,,,,,]
diccionario: se identifica en python con {'clave': 'valor', 'clave_2': 'valor_2,,}
'''
#set o conjuntos '
'''
se utilizan para almacenar informacion cuando no interesa el orden ni la posicion no permite valores duplicados'
'''
conjunto_1={"a", "b", "c"}
conjunto_2={"d", "e", "f"}
# print(type(conjunto_1))
# print(conjunto_1)

#metodos de los conjuntos 
conjunto_1.add("h")
# print(conjunto_1)

conjunto_2.remove("f")
# print(conjunto_2)

conjunto_3=conjunto_1.union(conjunto_2)
# print(conjunto_3)

#aplicar un metodo
conjunto_2.update(conjunto_1)
# print(conjunto_2)

conjunto_2.clear()
# print(conjunto_2)

'''
TUPLAS
son estructuras en python mas rigidas,
son inmutables,
almacenan distintos tipos de datos
las tuplas tiene posicion
'''
tupla_1=(1,1,1,1,1, "b", True)
print(type(tupla_1))
print(tupla_1.count("b"))

print(tupla_1.index("b"))