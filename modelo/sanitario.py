from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from modelo.base import Base
from enum import StrEnum


class TipoRegistroEnum(StrEnum):
    INDIVIDUAL = "individual"
    CICLO = "ciclo"
    PATOLOGIA = "patologia"

class CondicionEnum(StrEnum):
    DELGADO = "2"
    NORMAL = "3"
    OBESO = "4"

class AccionSanitariaEnum(StrEnum):
    BRUCELOSIS = "brucelosis"
    RABIA = "rabia"
    AFTOSA = "aftosa"
    CARBON = "carbon"
    DESPARASITACION = "desparasitacion"
    VITAMINAS = "vitaminas"
    MODIFICADOR = "modificador"
    BAÑO = "baño"
    CASTRACION = "castracion"
    MARCAJE = "marcaje"
    OTRO = "otro"


class CicloSanitario(Base):
    __tablename__ = "ciclo_sanitario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date)
    tipo_ciclo = Column(String(50), nullable=False)  # ejemplo: vacunación, desparasitación
    responsable = Column(String(120))
    observaciones = Column(Text)

    registros = relationship("Sanitario", back_populates="ciclo")


class Sanitario(Base):
    __tablename__ = "sanitario"
    __table_args__ = (
        UniqueConstraint("semoviente_id", "ciclo_id", name="uq_sanitario_ciclo_semoviente"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_registro = Column(Date, nullable=False)
    tipo_registro = Column(Enum(TipoRegistroEnum), default=TipoRegistroEnum.INDIVIDUAL)

    # Datos de semoviente
    semoviente_id = Column(Integer, ForeignKey("semoviente.id_semoviente"), nullable=False)
    nombre_semo = Column(String(100), nullable=False)
    condicion = Column(Enum(CondicionEnum), nullable=False)
    foto = Column(String(255))

    # Asociación a ciclo (opcional)
    ciclo_id = Column(Integer, ForeignKey("ciclo_sanitario.id"))
    ciclo = relationship("CicloSanitario", back_populates="registros")

    # Datos clínicos y acciones
    acciones = Column(String(255))  # Lista separada por coma: "rabia,aftosa,castracion"
    patologia = Column(String(255))  # solo si es patología
    tratamiento = Column(Text)
    observaciones = Column(Text)

    # Detalles de productos aplicados
    producto = Column(String(100))
    lote = Column(String(50))
    vencimiento = Column(Date)
    observacion_producto = Column(String(255))

    semoviente = relationship("Semoviente", backref="registros_sanitarios")

    def __repr__(self):
        return f"<Sanitario id={self.id} tipo={self.tipo_registro} fecha={self.fecha_registro}>"
