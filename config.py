from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Datos de conexion a MySQL
DB_USER = "invitado"
DB_PASSWORD = "Adso2977369"
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_NAME = "softgan_db"

# Construcción de la URL de conexión
DB_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear motor y sesión
engine = create_engine(DB_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Mostrar conexión exitosa solo si no hay error
try:
    with engine.connect() as conn:
        conn.execute("SELECT 1")  # comando mínimo para validar conexión
        print("Conexión exitosa a la base de datos")
except Exception as e:
    print(" Error de conexión:", e)

