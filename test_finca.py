from modelo.finca import Finca
from dao.finca_dao import FincaDao

dao = FincaDao()

# Lista de fincas a insertar
fincas = [
    Finca(
        nombre="La Pradera",
        direccion="Vereda Buenos Aires",
        hectareas=45.7,
        num_potreros=6,
        encargado="Carlos Ruiz",
        marca_hierro_1="LP1",
        marca_hierro_2="LP2",
        marca_hierro_3="LP3",
        nit="987654321-0",
        email="lapradera@correo.com"
    ),
    Finca(
        nombre="El Retiro",
        direccion="Vereda Santa Rita",
        hectareas=62.3,
        num_potreros=10,
        encargado="Luisa Fernanda",
        marca_hierro_1="ER1",
        marca_hierro_2="ER2",
        marca_hierro_3="ER3",
        nit="123456789-1",
        email="elretiro@correo.com"
    )
]

# Insertar fincas una por una
for finca in fincas:
    fid = dao.insert(finca)
    print(f"✅ Finca '{finca.nombre}' insertada con ID: {fid}")
