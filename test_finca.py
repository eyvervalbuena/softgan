from modelo.finca import Finca
from dao.finca_dao import FincaDao

dao = FincaDao()

# Lista de fincas a insertar
fincas = [
    Finca(
        nombre="El Nogal",
        direccion="Vereda La Alianza",
        hectareas=50.7,
        num_potreros=10,
        encargado="Julio Ernesto",
        marca_hierro_1="mklz",
        marca_hierro_2="x",
        marca_hierro_3="x",
        nit="123123123-3",
        email="lNogala@correo.com"
    ),
  
]

# Insertar fincas una por una
for finca in fincas:
    fid = dao.insert(finca)
    print(f"Finca '{finca.nombre}' insertada con ID: {fid}")
