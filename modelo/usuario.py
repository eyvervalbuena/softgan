from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from modelo.base import Base

class RolEnum(str, Enum):
    ADMINISTRADOR = "administrador"
    SUPERVISOR    = "supervisor"
    OPERARIO      = "operario"

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(120), nullable=False)
    rol = Column(Enum(RolEnum), nullable=False, default=RolEnum.OPERARIO)

    finca_id = Column(Integer, ForeignKey("finca.id"), nullable=False)

    # Relaciones
    finca = relationship("Finca", backref="usuarios")

    def __repr__(self) -> str:
        return f"<Usuario id={self.id} nombre='{self.nombre}' rol='{self.rol}'>"
