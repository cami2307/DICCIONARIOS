#Ejercicio: Escriba una función en Python que reproduzca lo siguiente: 𝑓(𝑥, 𝑦) = 𝑥2 + 𝑦2  Valor para X=3 y valor para Y=5
def f(x, y):
    return x*2 + y*2  # Definición de una función llamada 'f' que toma dos argumentos, 'x' e 'y', y retorna el resultado de la expresión x*2 + y*2.

x = 3  # Asignación de valor 3 a la variable 'x'.
y = 5  # Asignación de valor 5 a la variable 'y'.
result = f(x, y)  # Llamada a la función 'f' con los valores de 'x' e 'y' como argumentos, y se asigna el resultado a la variable 'result'.
print(result)  


#Ejercicio: Tomé el presente ejercicio,  y pasé a la función la lista con los días de la semana restantes

def diccionario(arg, resultado={}):

#Esta función toma un argumento `arg` y un diccionario `resultado`.Agrega `arg` al diccionario y luego imprime el diccionario actualizado.

    resultado[arg] = arg
    print(resultado)

diasSemana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado']

for dia in diasSemana:
    diccionario(dia)

#Declaración de un diccionario 

    diccionario = dict()
# Diccionario vacío inicializado con llaves
diccionario= {}
# Diccionario inicializado con valores
Diccionario = {'nombre':'Sandra' , 'edad': 44}

#Accediendo a los elementos de  un diccionario 
print(Diccionario ['nombre'])
print(Diccionario.get('nombre','No existe'))

#Agregar datos al diccionario después de creado
calificaciones.update({"Rosa": 3.7, "German": 4.8})

# Definición de un diccionario llamado 'calificaciones' con una clave 'nombre' y un valor 'Sandra'
# Nota: Esta línea se sobrescribe en la siguiente, por lo que la primera definición se descarta.
calificaciones = {
 'nombre': 'Sandra', 
 'notafinal': 5.0
 }

# Definición de un nuevo diccionario 'calificaciones' con claves como nombres de estudiantes y valores como sus notas finales.
calificaciones = {
 'Sandra': 5.0, 
 'Adriana':5.0,
 'Mauricio':4.5,
 'Jose':2.5
 }

# Iteración a través de los elementos del diccionario 'calificaciones'
for i, j in calificaciones.items():

    # Impresión de las claves (nombres) y valores (notas finales)
    print(i,j)

#ejercicio de la clave

# Imprime un encabezado
print("Técnicas por clave")

# Itera a través de las claves del diccionario 'calificaciones'
for i in calificaciones.keys():
    print(i)  # Imprime cada clave del diccionario

# Imprime un encabezado
print("Iterar por valor")

# Itera a través de los valores del diccionario 'calificaciones'
for j in calificaciones.values():
    print(j)  # Imprime cada valor del diccionario

# Lista de nombres
nombres = ['Maria', 'Sebastian', 'Ana']

# Lista de edades
edades = ['18', '25', '30']

# Itera a través de las listas 'nombres' y 'edades' al mismo tiempo usando la función 'zip'
for n, e in zip(nombres, edades):
    print('Tú nombre es {0}  y tu edad {1}.'.format(n, e))  # Imprime el nombre y la edad usando formateo de cadenas

#ejercicio operaciones en diccionarios

# Crea un diccionario llamado 'dicaleatorio' donde las claves son los números 2, 4 y 6, 
# y los valores son el cuadrado de cada número correspondiente.
dicaleatorio={x: x**2 for x in (2, 4, 6)}

# Imprime el diccionario creado anteriormente.
print(dicaleatorio)

# Imprime el texto "Números en reversa".
print("Números en reversa")

# Itera a través de una secuencia de números en orden inverso, 
# comenzando en 9 y disminuyendo de 2 en 2 hasta llegar a 1.
for i in reversed(range(1, 10, 2)):
    print(i)

# Elimina el elemento con la clave 'Rosa' del diccionario 'calificaciones'. 
# Nota: No se proporciona el código para 'calificaciones', por lo que esta línea podría causar un error.
del(calificaciones['Rosa'])

# Itera a través de los elementos del diccionario 'calificaciones' e imprime cada clave y valor.
for i, j in calificaciones.items():
    print(i, j)


# funciones 

# Definición de una función llamada "saludar"
def saludar():
    print("saludo")

# Definición de una función llamada "retornarnumero"
def retornarnumero():
    return 1

# Llamada a la función "saludar"
Saludar()  # Aquí hay un error tipográfico, debería ser "saludar" en lugar de "Saludar"

# Llamada a la función "retornarnumero" y su valor de retorno se ignora
retornarnumero()

# Se verifica si el valor retornado por la función "retornarnumero" es igual a 1
if retornarnumero()==1:
    print("devolvió un uno")
else:
    print("No devolvió un uno")

#funciones con parametros

# Definición de una función llamada 'raiz' que toma un argumento 'value'
def raiz(value):
    return value ** (1/2)  # Devuelve la raíz cuadrada de 'value'

# Imprime el resultado de llamar a la función 'raiz' con el argumento 4
print(f'La raiz cuadrada es: {raiz(4)}')

# Definición de una función llamada 'validarsiexiste' que toma un argumento 'obj'
def validarsiexiste(obj):
    # Comprueba si 'obj' es verdadero (truthy) y si es así, imprime un mensaje
    if obj:
        print(f"{obj} is True")
    else:
        # Si 'obj' es falso (falsy), imprime otro mensaje
        print(f"{obj} is False")

# Llamada a la función 'validarsiexiste' con el argumento 1
validarsiexiste(1)

#Funciones con Parámetros Posicionales
def compra(marca, cantidad, valor):
    # Esta línea define una función llamada 'compra' que toma tres argumentos: 'marca', 'cantidad' y 'valor'.
    # La función retorna un diccionario con tres claves: 'marca', 'cantidad' y 'valor*cantidad'.
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

print(f' lo comprado fue:{compra("AMD",3,2500000)}')
# Esta línea imprime el resultado de llamar a la función 'compra' con los argumentos dados.
# La función 'compra' se llama con los valores "AMD", 3 y 2500000.
# El resultado se imprime en una cadena de texto que incluye el texto "lo comprado fue:" y el diccionario devuelto por la función.

#Funciones con Parámetros Nominales
# Definiendo una función llamada 'compra' que toma tres argumentos: marca, cantidad y valor.
def compra(marca, cantidad, valor):
# Devolver un diccionario con las claves 'marca', 'cantidad' y 'valor', y sus respectivos valores.
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

# Imprimir una cadena formateada que llama a la función 'compra' con argumentos específicos.
print(f' lo comprado fue:{compra(marca="AMD", cantidad=3, valor=2500000)}')

#Parámetros por defecto

# Definir una función llamada 'compra' que toma tres argumentos: 'marca', 'cantidad' y 'valor' (con un valor predeterminado de 2500000).
def compra(marca, cantidad, valor=2500000):
    # Devuelve un diccionario que contiene las claves 'marca', 'cantidad' y 'valor', con sus valores correspondientes.
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

# Llama a la función 'compra' con los argumentos "AMD" y 3, e imprime el resultado.
print(f' lo comprado fue:{compra("AMD",3)}')

#Modificando parámetros mutables

def lista(arg, result=[]):
    # Esta función llamada 'lista' toma dos argumentos: 'arg' y 'result'. 'arg' es el elemento que se va a añadir a la lista 'result'.
    # 'result' es una lista que se inicializa por defecto como una lista vacía si no se proporciona un valor al llamar la función.
    
    result.append(arg)
    # Se añade el argumento 'arg' a la lista 'result'.
    
    print(result)
    # Se imprime la lista 'result' después de añadir 'arg'.
    
lista('domingo', [])
# Se llama a la función 'lista' con 'arg' como 'domingo' y 'result' como una lista vacía.

#Modificando parámetros mutables

def listalimpia(arg, result=None):
    # Esta función recibe dos argumentos: arg (el elemento que se va a agregar a la lista) y result (una lista opcional, que por defecto es None).
    
    if result is None:
        # Si result es None (es decir, no se proporcionó una lista), se crea una nueva lista vacía.
        result = []
        
    # Se agrega el argumento arg a la lista result.
    result.append(arg)
    
    # Se imprime la lista result después de agregar el argumento.
    print(result)

# Llamada a la función con "a" como argumento. Como no se proporcionó una lista, se crea una nueva.
listalimpia("a")

# Llamada a la función con "b" como argumento. Como no se proporcionó una lista, se crea una nueva.
listalimpia("b") 

#Funciones anónimas «lambda»

numero_palabras = lambda t: len(t.strip().split())

print(numero_palabras("hola, esto es una prueba con lambda"))

# Este bucle exterior itera dos veces, con i tomando valores 0 y 1.
for i in range(2):
    
    # Este bucle interior también itera dos veces, con j tomando valores 0 y 1.
    for j in range(2):
        # Imprime el valor de i, el valor de j y el resultado de la operación AND entre i y j.
        print(f"{i} & {j} = {operadorand(i, j)}")

# Definición de la función operadorand utilizando una expresión lambda.
operadorand = lambda x, y: x & y
