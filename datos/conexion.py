# -*- coding: latin-1 -*-
# Arriaga Sanchez Genesis, Bajaña Tarira Jenniffer, Landazuri Barcia Liliana,
# Mieles Piloso Andrews, Vera Saltos Jimmy
import sys
import pyodbc as bd


class Conexion:
    """
    Clase que permite abrir conexion a la BBDD y abrir cursor.
    """
    _SERVIDOR = '192.168.100.30' # Sino se conecta es porque cambio el ip en cdm ponemos ipconfig
    # _SERVIDOR = '127.0.0.1'
    _BBDD = 'APP_POO_C1'
    _USUARIO = 'app_poo_user_c1'
    _PASSWORD = '12345678'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        """
        Obtiene la conexion a la BBDD con los parametros de conexion como constantes
        :return:
        """
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + cls._SERVIDOR +
                                           ';DATABASE=' + cls._BBDD + ';UID=' + cls._USUARIO + ';PWD=' + cls._PASSWORD)
                # log.error(f'Conexion exito:{cls._conexion}')
                return cls._conexion
            except Exception as e:
                # log.error(f'Ocurrio una excepcion al obtener la conexion:{e}')
                print(e)
                sys.exit()

        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        """
        Obtiene el cursor que
        :return:
        """
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                # log.debug(f'Se abrio correcto el cursor::{cls._cursor}')
                return cls._cursor
            except Exception as e:
                # log.error(f'Ocurrio una excepcion al obtener el cursor:{e}')
                print(e)
                sys.exit()
        else:
            return cls._cursor


if __name__ == '__main__':
    print(Conexion.obtenerConexion())
    print(Conexion.obtenerCursor())

