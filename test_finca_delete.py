from modelo.finca import Finca
from dao.finca_dao import FincaDao

dao = FincaDao()

# ID de la finca que se va a eliminar
fid = 3  # Cambia por el ID que desees eliminar

# Buscar la finca
finca = dao.find_by_id(fid)

# Verificar si existe
if finca:
    print(" Finca encontrada:")
    print(" - nombre:", finca.nombre)
    print(" - encargado:", finca.encargado)

    # Confirmar la eliminación (opcional si lo haces automático)
    confirmacion = input("¿Estás seguro que quieres eliminar esta finca? (s/n): ").lower()
    if confirmacion == 's':
        dao.delete(fid)
        print(f" Finca con ID {fid} eliminada correctamente.")
    else:
        print(" Operación cancelada.")
else:
    print(f"No se encontró finca con ID {fid}")
