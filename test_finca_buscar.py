from modelo.finca import Finca
from dao.finca_dao import FincaDao

dao = FincaDao()

# Buscar la finca por su id
fid = 4  # <--  Cambia según el ID que quieras consultar
finca = dao.find_by_id(fid)

# Verificar si existe
if finca:
    print(" - Datos de la finca encontrada:")
    print(" - nombre:", finca.nombre)
    print(" - hectáreas:", finca.hectareas)
    print(" - encargado:", finca.encargado)
    print(" - num_potreros:", finca.num_potreros)
    print(" - marca_hierro_1:", finca.marca_hierro_1)
    print(" - marca_hierro_2:", finca.marca_hierro_2)
    print(" - marca_hierro_3:", finca.marca_hierro_3)
    print(" - NIT:", finca.nit)
    print(" - Email:", finca.email)
else:
    print(f" No se encontró finca con ID {fid}")
