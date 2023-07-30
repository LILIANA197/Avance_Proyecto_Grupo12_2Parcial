# Arriaga Sanchez Genesis, Bajaña Tarira Jenniffer, Landazuri Barcia Liliana, Mieles Piloso Andrews, Vera Saltos Jimmy

from Proyecto.dominio.docente import Docente
from Proyecto.dominio.estudiante import Estudiante
from Proyecto.dominio.libro import Libro
from Proyecto.dominio.pedido import Pedido
from Proyecto.dominio.revista import Revista


def pedir_material(lista_material, solicitante,material):
    print(f'*Pidio material:')
    if isinstance(lista_material, Libro):
        print(f'---- LIBRO ----\n{materiales}')
        if isinstance(solicitante, Estudiante):
            print(f'---- ESTUDIANTE ----\n{persona}')
        elif isinstance(solicitante, Docente):
            print(f'---- DOCENTE ----\n{persona}')
        elif isinstance(material, Pedido):
            print(f'-- Fecha de prestamo: {Pedido}\n-- fecha_devolucion: {Pedido}')
    elif isinstance(lista_material, Revista):
        print(f'---- REVISTA ----\n{materiales}')
        if isinstance(solicitante, Estudiante):
            print(f'---- ESTUDIANTE ----\n{persona}')
        elif isinstance(solicitante, Docente):
            print(f'---- DOCENTE ----\n{persona}')



e1 = Estudiante(cedula="0123456789", nombre="Pablo", apellido="Pérez", email="pablo@gmail.com",
                telefono="0960354278", direccion="Francisco de Orellana", carrera="Ingeniería", numero_libros=2,
                activo=True, nivel=2)
e2 = Estudiante(cedula="0987456123", nombre="Luisa", apellido="López", email="luisa@gmail.com",
                telefono="0936157689", direccion="Avenida Sixto Garay", carrera="Medicina",
                numero_libros=4, activo=False, nivel=3)
doc1 = Docente(cedula="0123457759", nombre="Marcelo", apellido= "Villalba", email="Marcelo@gmail.com",
               telefono="0944563344", direccion="Avenida El Ejercito", numero_libros=2, activo=True,
                   carrera="Finanzas", titulo_3er_nivel="Licenciatura en Contaduria ",
                   titulo_4to_nivel="Magister en Finanzas")
doc2 = Docente(cedula="0964553423", nombre="Jessica", apellido= "Moncada", email="Jessica@gmail.com",
                  telefono="0960356422", direccion="Avenida Juan TancaMarengo", numero_libros=4, activo=False,
                  carrera="Psicologia", titulo_3er_nivel="Licenciada en Psicopedagogia",
                  titulo_4to_nivel="Magister en estudios sociales")
libro1 = Libro(codigo="620.1/C87", autor="Craig Jr Roy", titulo="Mecanica de materiales", anio=2002,
               editorial="continental", disponible=True, cantidad_disponible=30, tipo_pasta="cubierta carton")
libro2 = Libro(codigo="doi12.123", autor="McGoldrick J.Giordano",
               titulo="Back to the future:An examination of the native american holocaust experience",
               anio=2002, editorial="tercera edicion", disponible=False, cantidad_disponible=0,
               tipo_pasta="Electronico")
revista1 = Revista(codigo=" 10.7560/IC47402", autor="Pierre Mounier Kuhn", titulo="Information & culture",
                   anio=2012, editorial="volume47_number4_2012", disponible=False, cantidad_disponible=0,
                   tipo="online")
revista2 = Revista(codigo=" 10.7660/IC47702", autor="Smith J.M.& Davis H.",
                   titulo="Language acquisition among autistic children", anio=2019,
                   editorial="volume5_Issue2_2011", disponible=True, cantidad_disponible=104, tipo="online")

personas = list()
materiales = list()
pedidos = list()
personas.append(e1)
personas.append(doc2)
personas.append(e2)
personas.append(doc1)
materiales.append(libro2)
materiales.append(libro1)
materiales.append(revista1)
materiales.append(revista2)


for materiales in materiales:
    pedir_material(lista_material=materiales, solicitante=personas, material=Pedido)
    print('*'.center(100, '*'))
for persona in personas:
    pedir_material(lista_material=materiales, solicitante=personas, material=Pedido)
    print('*'.center(100, '*'))

def devolver_material(self, solicitante, fecha_devoluvion=None):
    if self.solicitante == solicitante:
        self.fecha_devolucion = fecha_devoluvion
        print(f'Devolucion con exito')
    else:
        print(f'No se puede devolver el material. El solicitante no coincide.')
