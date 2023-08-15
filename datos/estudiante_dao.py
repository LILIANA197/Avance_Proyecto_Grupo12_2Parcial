# Arriaga Sanchez Genesis, Bajaña Tarira Jenniffer, Landazuri Barcia Liliana,
# Mieles Piloso Andrews, Vera Saltos Jimmy
from Proyecto.datos.conexion import Conexion
from Proyecto.dominio.estudiante import Estudiante
from pyodbc import ProgrammingError
from pyodbc import IntegrityError


class EstudianteDao:
    _INSERTAR = ("INSERT INTO Estudiantes (cedula,nombre,apellido,email,carrera,activo,fecha_nacimiento,edad,"
                 "estatura,peso) VALUES(?,?,?,?,?,?,?,?,?,?)")
    _SELECCIONAR_X_CEDULA = ("SELECT id, cedula, nombre, apellido, email, carrera, activo, fecha_nacimiento, edad, "
                             "estatura, peso FROM Estudiantes WHERE cedula = ?")
    _SELECCIONAR = ("SELECT id, cedula, nombre, apellido, email, carrera, activo, fecha_nacimiento, edad, estatura, "
                    "peso FROM Estudiantes")

    # where activo = 1

    @classmethod
    def insertar_estudiante(cls, estudiante):
        # Conexion.obtenerConexion() YA NO CREAMOS PORQUE LA BASE YA LO CREABA
        # cursor = Conexion.obtenerCursor()
        respuesta = {'exito': False, 'mensaje': ''}
        flag_exito = False
        mensaje = ''
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.cedula, estudiante.nombre, estudiante.apellido, estudiante.email,
                         estudiante.carrera, estudiante.activo, estudiante.fecha_nacimento, estudiante.edad,
                         estudiante.estatura, estudiante.peso)
                cursor.execute(cls._INSERTAR, datos)
                flag_exito = True
                mensaje = 'Ingreso Exitoso'
        except IntegrityError as e:
            flag_exito = False
            # print('La cedula que intenta ingresar ya existe')
            if e.__str__().find('Cedula') > 0:
                print('Cedula ya ingresada')
                mensaje = 'Cedula ya ingresada'
            elif e.__str__().find('Email') > 0:
                print('Email ya ingresada')
                mensaje = 'Email ya ingresada'
            else:
                print('Error de integridad')
                mensaje = 'Error de integridad'
        except ProgrammingError as e:
            flag_exito = False
            print('Los datos ingresados no son del tamano permitido')
            mensaje = 'Los datos ingresados no son del tamano permitido'
        except Exception as e:
            print(e)
            # print(type(e))
        finally:
            respuesta['exito'] = flag_exito
            respuesta['mensaje'] = mensaje
            return respuesta

    @classmethod
    def seleccionar_por_cedula(cls, estudiante):
        persona_encotrada = None
        print('*'.center(100, '*'))
        print('ESTUDIANTE:')
        print('*'.center(100, '*'))
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.cedula,)
                resultado = cursor.execute(cls._SELECCIONAR_X_CEDULA, datos)
                persona_encontrada = resultado.fetchone()
                estudiante.id = persona_encontrada[0]
                estudiante.cedula = persona_encontrada[1]
                estudiante.nombre = persona_encontrada[2]
                estudiante.apellido = persona_encontrada[3]
                estudiante.email = persona_encontrada[4]
                estudiante.carrera = persona_encontrada[5]
                estudiante.activo = persona_encontrada[6]
                estudiante.fecha_nacimiento = persona_encontrada[7]
                estudiante.edad = persona_encontrada[8]
                estudiante.estatura = persona_encontrada[9]
                estudiante.peso = persona_encontrada[10]
                # resultado.fetchone()
        except Exception as e:
            print(e)
        finally:
            return estudiante

    @classmethod
    def seleccionar_estudiantes(cls):
        lista_estudiantes = list()
        try:
            with Conexion.obtenerCursor() as cursor:
                resultado = cursor.execute(cls._SELECCIONAR)
                for tupla_estudiante in resultado.fetchall():
                    estudiante = Estudiante()
                    estudiante.id = tupla_estudiante[0]
                    estudiante.cedula = tupla_estudiante[1]
                    estudiante.nombre = tupla_estudiante[2]
                    estudiante.apellido = tupla_estudiante[3]
                    estudiante.email = tupla_estudiante[4]
                    estudiante.carrera = tupla_estudiante[5]
                    estudiante.activo = tupla_estudiante[6]
                    estudiante.fecha_nacimiento = tupla_estudiante[7]
                    estudiante.edad = tupla_estudiante[8]
                    estudiante.estatura = tupla_estudiante[9]
                    estudiante.peso = tupla_estudiante[10]
                    lista_estudiantes.append(estudiante)
                # print(resultado.fetchall())
                # print(resultado)
        except Exception as e:
            lista_estudiantes = None
        finally:
            return lista_estudiantes


if __name__ == '__main__':
    # e1 = Estudiante()
    # e1.cedula = '0952762679'
    # e1.nombre = 'Andrea'
    # e1.apellido = 'Parrales'
    # e1.email = 'andrea@gmail.com'
    # e1.carrera = 'ADM'
    # e1.activo = True
    # # EstudianteDao.insertar_estudiante(e1)
    # persona_encotrada = EstudianteDao.seleccionar_por_cedula(e1)
    # print(persona_encotrada)
    # EstudianteDao.seleccionar_personas()
    print('*'.center(100, '*'))
    print('ESTUDIANTES:')
    print('*'.center(100, '*'))
    estudiantes = EstudianteDao.seleccionar_estudiantes()
    for estudiante in estudiantes:
        print(estudiante)
        print('*'.center(100, '*'))
