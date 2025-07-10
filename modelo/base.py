from sqlalchemy.orm import DeclarativeBase
from config import engine

# base para todos los modelos
class Base(DeclarativeBase):
    pass

# Función para crear todas las tablas registradas con Base
def crear_tablas():
    print("Creando tablas...")
    Base.metadata.create_all(engine)
    print("Tablas creadas correctamente.")
