from sqlalchemy import create_engine, text

# Datos visibles para el instructor
DB_USER = "invitado"
DB_PASSWORD = "Adso2977369"
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_NAME = "softgan_db"

DB_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DB_URL, echo=True, future=True)

try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        base_actual = conn.execute(text("SELECT DATABASE()")).scalar()
        print(f"✅ Conexión exitosa a la base de datos: {base_actual}")
except Exception as e:
    print("❌ Error de conexión:", e)
