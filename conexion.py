from Loggin_Base import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE='test_db'
    _USERNAME= 'postgres'
    _PASSWORD='admin'
    _PORT='5432'
    _HOST='127.0.0.1'
    """ _conexion = None
    _cursor = None """
    _MAX_CON = 5
    _MIN_CON = 1
    _pool = None

    @classmethod
    def getPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                    host = cls._HOST,
                                                    user = cls._USERNAME,
                                                    password = cls._PASSWORD,
                                                    port = cls._PORT,
                                                    database= cls._DATABASE)
                print(f'Conexion Pool Exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                print(f'Ocurrio un error al obtener conexion: {e}')
        else: 
            return cls._pool

    @classmethod        
    def obtenerConexion(cls):
        conexion = cls.getPool().getconn()
        print(f'Conexion obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.getPool().putconn(conexion)
        print(f'Regresamos la conexion: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.getPool().closeall()

    """ @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None or cls._conexion.closed:
            try:
                cls._conexion = psycopg2.connect(host=cls._HOST, 
                                                user=cls._USERNAME,
                                                password=cls._PASSWORD,
                                                port=cls._PORT,
                                                database=cls._DATABASE)
                log.debug(f'Conexion exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.debug(f'Ocurrio una excepcion: {e}')
                sys.exit()
        else:
            return cls._conexion """

    """ @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None or cls._cursor.closed:
            try:
                cls._cursor=cls.obtenerConexion().cursor()
                print(f'Se abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                print(f'Ocurrio una exepcion: {e}')
                sys.exit()
        else:
            return cls._cursor """

if __name__ == '__main__':
   
    """Conexion().obtenerConexion()
    Conexion().obtenerCursor() """
    cone1 = Conexion().obtenerConexion()
    Conexion().liberarConexion(cone1)
    Conexion().obtenerConexion()