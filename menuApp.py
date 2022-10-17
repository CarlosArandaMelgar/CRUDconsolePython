import sys
from Loggin_Base import log
from persona import Persona
from personaDAO import personaDAO

from personaDAO import personaDAO

x = 0

while x != 5:
    print('Welcome to the program \nChoose an option: ')
    print('1. Listar Personas')
    print('2. Agregar Personas')
    print('3. Modificar Persona')
    print('4. Eliminar Persona')
    print('5. Salir')
    opcion = int(input('Escribe tu opcion (1-5): '))
    try:
        if opcion == 1:
            registros = personaDAO().seleccionar()
            for i in registros:
                log.info(i)
        elif opcion == 2:
            nombre = input('Escribe el nombre: ')
            apellido = input('Escribe el apellido: ')
            email = input('Escribe el Email: ')
            usuario = Persona(nombre=nombre, apellido=apellido, email=email)
            personaDAO().insertar(usuario)

        elif opcion == 3:
            usuario = int(input('Ingrese ID de usuario: '))
            nombre = input('Ingrese nuevo nombre: ')
            apellido = input('Ingrese nuevo apellido: ')
            email = input('Ingrese nuevo nombre email: ')
            obj = Persona(usuario, nombre, apellido, email)
            personaDAO.actualizar(obj)

        elif opcion == 4:
            usuario = int(input('Ingresa ID de usuario a eliminar: '))
            obj = Persona(id_persona=usuario)
            personaDAO.eliminar(obj)

        else:
            sys.exit()
    except Exception as e:
        print(f'Ocurrio un error: {e}')