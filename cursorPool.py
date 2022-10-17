from conexion import Conexion
from Loggin_Base import log

class cursorPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Inicio del metodo __Enter__ With')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipoExcep, valorExcep, detailsExcep):
        log.debug('Se ejecuta metodo exit')
        if valorExcep != None:
            self._conexion.rollback()
            log.info(f'Ocurrio una exepcion: {valorExcep}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    """with cursorPool() as cursor:
         print('Dentro del bloque With')
         cursor.execute('SELECT * FROM "Persona" ORDER BY "idPersona"')
         print(cursor.fetchall())
    """