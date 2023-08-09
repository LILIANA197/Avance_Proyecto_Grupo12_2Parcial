from Proyecto.datos.conexion import Conexion
from Proyecto.dominio.estudiante import Estudiante
from pyodbc import ProgrammingError
from pyodbc import IntegrityError


class EstudianteDao:
    _INSERTAR = "INSERT INTO Estudiantes (cedula,nombre, apellido,email,carrera,activo) VALUES(?,?,?,?,?,?)"
    _SELECCIONAR_X_CEDULA = ('select id, cedula, nombre, apellido, email, carrera, activo from Estudiantes '
                             'where cedula = ?')
    @classmethod
    def insertar_estudiante(cls, estudiante):
        # Conexion.obtenerConexion() YA NO CREAMOS PORQUE LA BASE YA LO CREABA
        # cursor = Conexion.obtenerCursor()
        respuesta = {'exito': False, 'mesnsaje': ''}
        flag_exito = False
        mensaje = ''
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.cedula, estudiante.nombre, estudiante.apellido, estudiante.email, estudiante.carrera
                         , estudiante.activo)
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
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.cedula,)
                resultado = cursor.execute(cls._SELECCIONAR_X_CEDULA, datos)
                persona_encontrar = resultado.fetchone()
                estudiante.id = persona_encontrar[0]
                estudiante.cedula = persona_encontrar[1]
                estudiante.nombre = persona_encontrar[2]
                estudiante.apellido = persona_encontrar[3]
                estudiante.email = persona_encontrar[4]
                estudiante.carrera = persona_encontrar[5]
                estudiante.activo = persona_encontrar[6]
                resultado.fetchone()
        except Exception as e:
            print(e)
        finally:
            print('----- ESTUDIANTE ------')
            return estudiante
if __name__ == '__main__':
    e1 = Estudiante()
    e1.cedula = '0952762679'
    e1.nombre = 'Andrea'
    e1.apellido = 'Parrales'
    e1.email = 'andrea@gmail.com'
    e1.carrera = 'ADM'
    e1.activo = True
    # EstudianteDao.insertar_estudiante(e1)
    persona_encotrada = EstudianteDao.seleccionar_por_cedula(e1)
    print(persona_encotrada)
