from conexion import Conexion
from persona import Persona
from cursorPool import cursorPool

class personaDAO:

    _SELEC = 'SELECT * FROM "Persona" ORDER BY "idPersona"'
    _INSERTAR = 'INSERT INTO "Persona"("Nombre", "Apellido", "Correo") VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE "Persona" SET "Nombre"=%s, "Apellido"=%s, "Correo"=%s WHERE "idPersona"=%s'
    _ELIMINAR = 'DELETE FROM "Persona" WHERE "idPersona"=%s'

    @classmethod
    def seleccionar(cls):
        with cursorPool() as cursor:
            cursor.execute(cls._SELEC)
            registros = cursor.fetchall()
            return registros

    @classmethod
    def insertar(cls, persona):
        with cursorPool() as cursor:
            obj = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, obj)
            return cursor.rowcount
            
    @classmethod
    def actualizar(cls, persona):
        with cursorPool() as cursor:
            registro = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, registro)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with cursorPool() as cursor:
            registro = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, registro)
            print(f'Objeto Eliminado: {registro}')
            return cursor.rowcount

if __name__ == '__main__':
    test = personaDAO().seleccionar()
    for i in test:
        print(f'Registros: \n{i}')

    #Luis = Persona(nombre='Gabriel', apellido='Vichy', email='vichy@gmail.com')
    #Hola = personaDAO().insertar(Luis)
    #print(Hola)
