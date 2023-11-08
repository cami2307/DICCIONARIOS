# Crear un diccionario vacío llamado 'equipos' para almacenar información sobre los equipos.
equipos = {}

# Definir una función 'agregarEquipo' que toma tres argumentos: idEquipo, cargador y mouse.
def agregarEquipo(idEquipo, cargador, mouse):
    # Agregar un elemento al diccionario 'equipos' con la clave 'idEquipo' y un diccionario como valor.
    # El diccionario contiene información sobre el cargador, el mouse y una lista vacía de 'novedades'.
    equipos[idEquipo] = {'cargador': cargador, 'mouse': mouse, 'novedades': []}

# Definir una función 'agregarNovedad' que toma tres argumentos: idEquipo, fecha y descripción.
def agregarNovedad(idEquipo, fecha, descripcion):
    # Verificar si el 'idEquipo' existe en el diccionario 'equipos'.
    if idEquipo in equipos:
        # Si existe, agregar una nueva novedad a la lista de novedades del equipo.
        equipos[idEquipo]['novedades'].append({'fecha': fecha, 'descripcion': descripcion})
    else:
        # Si el 'idEquipo' no existe, mostrar un mensaje de error.
        print("El equipo con ID {} no existe.".format(idEquipo))

# Definir una función 'buscarEquipo' que toma un argumento 'idEquipo'.
def buscarEquipo(idEquipo):
    # Verificar si el 'idEquipo' existe en el diccionario 'equipos'.
    if idEquipo in equipos:
        # Si existe, mostrar la información del equipo.
        print("Información del equipo con ID {}: {}".format(idEquipo, equipos[idEquipo]))
    else:
        # Si el 'idEquipo' no existe, mostrar un mensaje de error.
        print("El equipo con ID {} no existe.".format(idEquipo))

# Definir una función 'mostrarReporteNovedades' que no toma argumentos.
def mostrarReporteNovedades():
    # Iterar a través de los elementos del diccionario 'equipos'.
    for idEquipo, equipo in equipos.items():
        # Verificar si el equipo tiene novedades (la lista de novedades no está vacía).
        if equipo['novedades']:
            # Si tiene novedades, mostrarlas.
            print("Equipo con ID {}: {}".format(idEquipo, equipo['novedades']))

# Definir una función 'mostrarEquipos' que no toma argumentos.
def mostrarEquipos():
    # Iterar a través de los elementos del diccionario 'equipos'.
    for idEquipo, equipo in equipos.items():
        # Mostrar la información básica de cada equipo (ID, cargador y mouse).
        print("ID {}: Cargador: {}, Mouse: {}".format(idEquipo, equipo['cargador'], equipo['mouse']))

# Definir una función 'modificarEquipo' que toma tres argumentos: idEquipo, cargador y mouse.
def modificarEquipo(idEquipo, cargador, mouse):
    # Verificar si el 'idEquipo' existe en el diccionario 'equipos'.
    if idEquipo in equipos:
        # Si existe, actualizar la información del cargador y el mouse del equipo.
        equipos[idEquipo]['cargador'] = cargador
        equipos[idEquipo]['mouse'] = mouse
    else:
        # Si el 'idEquipo' no existe, mostrar un mensaje de error.
        print("El equipo con ID {} no existe.".format(idEquipo))

# Definir una función 'eliminarEquipo' que toma un argumento 'idEquipo'.
def eliminarEquipo(idEquipo):
    # Verificar si el 'idEquipo' existe en el diccionario 'equipos'.
    if idEquipo in equipos:
        # Si existe, eliminar el equipo del diccionario.
        del equipos[idEquipo]
    else:
        # Si el 'idEquipo' no existe, mostrar un mensaje de error.
        print("El equipo con ID {} no existe.".format(idEquipo))

# Ejemplos de uso:
# Agregar dos equipos con sus respectivos cargadores y mouse.
agregarEquipo(1, 'Cargador 1', 'Mouse 1')
agregarEquipo(2, 'Cargador 2', 'Mouse 2')

# Agregar novedades a los equipos.
agregarNovedad(1, '2023-01-01', 'Problemas de conexión')
agregarNovedad(2, '2023-01-02', 'Pantalla rota')

# Buscar información de un equipo por su ID.
buscarEquipo(1)

# Mostrar un reporte de novedades para todos los equipos.
mostrarReporteNovedades()

# Mostrar información básica de todos los equipos.
mostrarEquipos()

# Modificar la información de un equipo.
modificarEquipo(1, 'Nuevo cargador', 'Nuevo mouse')

# Eliminar un equipo por su ID.
eliminarEquipo(2)
