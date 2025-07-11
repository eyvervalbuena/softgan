from modelo.finca import Finca
from dao.finca_dao import FincaDao

dao = FincaDao()

# Buscar la finca por su ID
fid = 3  # <--  cambia este ID por el que se va a actualizar
finca = dao.find_by_id(fid)

# Verificar si existe
if finca:

    # Cambiar datos
    finca.nombre = "El Nuevo Nogal"
    finca.direccion = "Vereda La Alianza"
    finca.hectareas = 99.5
    finca.num_potreros = 20
    finca.encargado = "Eyver Valbuena"
    finca.marca_hierro_1 = "KLTZ" 
    finca.marca_hierro_2 = "no"
    finca.marca_hierro_3 = "no"
    finca.nit = "nn"
    finca.email = "nogal@correo.com"

    # Guardar los cambios
    dao.update(finca)
    print("Finca actualizada con éxito.")

    # Confirmar los cambios
    finca_actualizada = dao.find_by_id(fid)
    print("Datos nuevos de Finca:")
    print(" - nombre:", finca_actualizada.nombre)
    print(" - dirección", finca_actualizada.direccion)
    print(" - hectáreas:", finca_actualizada.hectareas)
    print(" - num_poteros", finca_actualizada.num_potreros)
    print(" - encargado:", finca_actualizada.encargado)
    print(" - marca_hierro_1", finca_actualizada.marca_hierro_1)
    print(" - marca_hierro_2", finca_actualizada.marca_hierro_2)
    print(" - marca_hierro_3", finca_actualizada.marca_hierro_3)
    print(" - nit",finca_actualizada.nit) # verificar que no exista un nit igual para evitar duplicar 
    print(" - email",finca_actualizada.email) # verificar que no exista un email igual para evitar duplicar 
else:
    print(f" No se encontró finca con ID {fid}")
