from Proyecto.dominio.docente import Docente
from Proyecto.dominio.estudiante import Estudiante
from Proyecto.dominio.libro import Libro
from Proyecto.dominio.revista import Revista
from Proyecto.dominio.pedido import Pedido

e1 = Estudiante(cedula="0123456789", nombre="Pablo", apellido="Pérez", email="pablo@gmail.com",
                telefono="0960354278", direccion="Francisco de Orellana", carrera="Ingeniería", numero_libros=2,
                activo=True, nivel=2)
e2 = Estudiante(cedula="0987456123", nombre="Luisa", apellido="López", email="luisa@gmail.com",
                telefono="0936157689", direccion="Avenida Sixto Garay", carrera="Medicina",
                numero_libros=4, activo=False, nivel=3)
print('*'.center(100, '*'))
print(f'               ESTUDIANTES               ')
print('*'.center(100, '*'))
print(e1)
print('*'.center(100, '-'))
print(e2)
print('*'.center(100, '*'))

doc1 = Docente(cedula="0123457759", nombre="Marcelo", apellido="Villalba", email="Marcelo@gmail.com",
               telefono="0944563344", direccion="Avenida El Ejercito", numero_libros=2, activo=True,
               carrera="Finanzas", titulo_3er_nivel="Licenciatura en Contaduria ",
               titulo_4to_nivel="Magister en Finanzas")
doc2 = Docente(cedula="0964553423", nombre="Jessica", apellido="Moncada", email="Jessica@gmail.com",
               telefono="0960356422", direccion="Avenida Juan TancaMarengo", numero_libros=4, activo=False,
               carrera="Psicologia", titulo_3er_nivel="Licenciada en Psicopedagogia",
               titulo_4to_nivel="Magister en estudios sociales")
print(f'               DOCENTES               ')
print('*'.center(100, '*'))
print(doc1)
print('*'.center(100, '-'))
print(doc2)
print('*'.center(100, '*'))
libro1 = Libro(codigo="620.1/C87", autor="Craig Jr Roy", titulo="Mecanica de materiales", anio=2002,
               editorial="continental", disponible=True, cantidad_disponible=30, tipo_pasta="cubierta carton")
libro2 = Libro(codigo="doi12.123", autor="McGoldrick J.Giordano",
               titulo="Back to the future:An examination of the native american holocaust experience",
               anio=2002, editorial="tercera edicion", disponible=False, cantidad_disponible=0,
               tipo_pasta="Electronico")
print(f'               LIBROS               ')
print('*'.center(100, '*'))
print(libro1)
print('*'.center(100, '-'))
print(libro2)
print('*'.center(100, '*'))
revista1 = Revista(codigo=" 10.7560/IC47402", autor="Pierre Mounier Kuhn", titulo="Information & culture",
                   anio=2012, editorial="volume47_number4_2012", disponible=False, cantidad_disponible=0,
                   tipo="online")
revista2 = Revista(codigo=" 10.7660/IC47702", autor="Smith J.M.& Davis H.",
                   titulo="Language acquisition among autistic children", anio=2019,
                   editorial="volume5_Issue2_2011", disponible=True, cantidad_disponible=104, tipo="online")
print(f'               REVISTAS               ')
print('*'.center(100, '*'))
print(revista1)
print('*'.center(100, '-'))
print(revista2)
print('*'.center(100, '*'))

# pedido = Pedido(solicitante="Marcelo Villalba", lista_material="kkk", fecha_prestamo="25/07/2022",
# fecha_devolucion="30/07/2022")
print(f'               PEDIDOS                ')
print('*'.center(100, '*'))
# print(pedido1)
# print('*'.center(100, '*'))

materiales = list()
materiales.append(libro1)
materiales.append(revista2)
# print(materiales)

pedido1 = Pedido(solicitante=doc2, lista_materiales=materiales, fecha_prestamo="25/07/2022",
                 fecha_devolucion="30/07/2022")

# pedido1.mostrar_solicitante()
# pedido1.mostrar_materiales()
pedido1.mostrar_pedido()

# personas = list()
# materiales = list()
# pedidos=list()
# personas.append(e1)
# personas.append(doc2)
# personas.append(e2)
# personas.append(doc1)
# materiales.append(libro2)
# materiales.append(libro1)
# materiales.append(revista1)
# materiales.append(revista2)
#
#
# for materiales in materiales:
#     pedir_material(lista_material=materiales, solicitante=personas, material=Pedido)
#     print('*'.center(100, '*'))
# for persona in personas:
#     pedir_material(lista_material=materiales, solicitante=personas, material=Pedido)
#     print('*'.center(100, '*'))
#
# def devolver_material(self, solicitante, fecha_devoluvion=None):
#     if self.solicitante == solicitante:
#         self.fecha_devolucion = fecha_devoluvion
#         print(f'Devolucion con exito')
#     else:
#         print(f'No se puede devolver el material. El solicitante no coincide.')


libro1 = Libro(codigo="620.1/C87", autor="Craig Jr Roy", titulo="Mecanica de materiales", anio=2002,
               editorial="continental", disponible=True, cantidad_disponible=30, tipo_pasta="cubierta carton")

revista2 = Revista(codigo=" 10.7660/IC47702", autor="Smith J.M.& Davis H.",
                   titulo="Language acquisition among autistic children", anio=2019,
                   editorial="volume5_Issue2_2011", disponible=True, cantidad_disponible=104, tipo="online")

# pedido = Pedido(solicitante='joseph paez', lista_material='Compra domicilio',
#                  fecha_prestamo='20/junio/2023', fecha_devolucion='28/Junio/2023')
#
# materiales = list()
# materiales.append(libro1)
# materiales.append(revista2)
# print(materiales)

# pedido1.mostrar_solicitante()
# pedido1.mostrar_materiales()
# pedido1.mostrar_pedido()
