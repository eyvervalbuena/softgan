from sqlalchemy import Column, Integer, String, Numeric, UniqueConstraint
from modelo.base import Base

class Finca(Base):
    __tablename__ = "finca"
    __table_args__ = (
        UniqueConstraint("nit",   name="uq_finca_nit"),
        UniqueConstraint("email", name="uq_finca_email"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(120), nullable=False)
    direccion = Column(String(255))
    hectareas = Column(Numeric(8, 2))        # hasta 999999.99 ha
    num_potreros = Column(Integer)
    encargado = Column(String(120), nullable=False)
    marca_hierro_1 = Column(String(45))
    marca_hierro_2 = Column(String(45))
    marca_hierro_3 = Column(String(45))
    nit = Column(String(20), nullable=False)
    email = Column(String(120), nullable=False)

    def __repr__(self) -> str:
        return f"<Finca id={self.id} nombre='{self.nombre}' nit='{self.nit}'>"
