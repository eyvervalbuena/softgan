# Importar los modelos para registrarlos antes de crear las tablas
from config import engine
from modelo.base import crear_tablas

from modelo import finca
#from modelo import usuario
#from modelo import semoviente
#from modelo import sanitario
#from modelo import almacen
#from modelo import alerta

# importar la función que crea las tablas
from modelo.base import crear_tablas

# creación de tablas
crear_tablas()
