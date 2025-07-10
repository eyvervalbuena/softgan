from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey
from sqlalchemy.orm import relationship
from modelo.base import Base

# Enumeraciones
class SexoEnum(str, Enum):
    MACHO = "M"
    HEMBRA = "H"

class TipoEnum(str, Enum):
    CARNE       = "carne"
    LECHE       = "leche"
    REPRODUCTOR = "reproductor"

    @staticmethod
    def valid_for(sexo: str) -> set[str]:
        return (
            {"leche", "carne"} if sexo == SexoEnum.HEMBRA
            else {"reproductor", "carne"}
        )

class CondicionEnum(str, Enum):
    DELGADO = "2"
    NORMAL  = "3"
    OBESO   = "4"

class EstatusEnum(str, Enum):
    ACTIVO   = "activo"
    INACTIVO = "inactivo"

class OrigenEnum(str, Enum):
    COMPRA = "compra"
    CRIA   = "cría"

class DesincorporacionEnum(str, Enum):
    VENTA    = "venta"
    MUERTE   = "muerte"
    DESCARTE = "descarte"
    PERDIDA  = "perdida"

    @staticmethod
    def validar(estatus: str, causa: str | None) -> bool:
        if estatus == EstatusEnum.ACTIVO:
            return causa is None
        return causa in DesincorporacionEnum.__members__

# Modelo Semoviente
class Semoviente(Base):
    __tablename__ = "semoviente"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(80), nullable=False)
    sexo = Column(Enum(SexoEnum), nullable=False)
    tipo = Column(Enum(TipoEnum), nullable=False)
    condicion = Column(Enum(CondicionEnum), nullable=False)
    estatus = Column(Enum(EstatusEnum), default=EstatusEnum.ACTIVO)
    origen = Column(Enum(OrigenEnum), nullable=False)

    fecha_nacimiento = Column(Date)
    fecha_incorporacion = Column(Date)
    fecha_desincorporacion = Column(Date)
    causa_desincorporacion = Column(Enum(DesincorporacionEnum), nullable=True)
    foto = Column(String(255))

    padre_id = Column(Integer, ForeignKey("semoviente.id"), nullable=True)
    madre_id = Column(Integer, ForeignKey("semoviente.id"), nullable=True)
    finca_id = Column(Integer, ForeignKey("finca.id"), nullable=False)

    # Relaciones
    finca = relationship("Finca", backref="semovientes")
    padre = relationship("Semoviente", remote_side=[id], foreign_keys=[padre_id])
    madre = relationship("Semoviente", remote_side=[id], foreign_keys=[madre_id])

    def __init__(self, **kwargs):
        sexo = kwargs.get("sexo")
        tipo = kwargs.get("tipo")
        estatus = kwargs.get("estatus")
        causa = kwargs.get("causa_desincorporacion")

        if sexo and tipo and tipo not in TipoEnum.valid_for(sexo):
            raise ValueError(f"Tipo '{tipo}' no permitido para sexo '{sexo}'")

        if not DesincorporacionEnum.validar(estatus, causa):
            raise ValueError("Causa de desincorporación no válida para el estatus actual.")

        super().__init__(**kwargs)

    def __repr__(self):
        return f"<Semoviente id={self.id} nombre={self.nombre} sexo={self.sexo} tipo={self.tipo}>"
