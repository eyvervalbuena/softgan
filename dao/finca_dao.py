from modelo.finca import Finca               # Importa el modelo Finca
from config import SessionLocal              # Usa la sesión de conexión a MySQL

class FincaDao:
    def insert(self, finca: Finca) -> int:
        """
        Inserta una nueva finca en la base de datos y retorna su ID.
        """
        with SessionLocal() as session:
            session.add(finca)              # Agrega el objeto a la sesión
            session.commit()                # Guarda los cambios
            session.refresh(finca)          # Actualiza el objeto con el ID generado
            return finca.id

    def find_by_id(self, finca_id: int) -> Finca | None:
        """
        Busca una finca por su ID. Retorna el objeto Finca o None si no existe.
        """
        with SessionLocal() as session:
            return session.get(Finca, finca_id)

    def update(self, finca: Finca) -> None:
        """
        Actualiza los datos de una finca.
        """
        with SessionLocal() as session:
            session.merge(finca)            # Actualiza si existe, inserta si no
            session.commit()

    def delete(self, finca_id: int) -> bool:
        """
        Elimina una finca por su ID. Retorna True si la eliminó, False si no la encontró.
        """
        with SessionLocal() as session:
            obj = session.get(Finca, finca_id)
            if obj:
                session.delete(obj)
                session.commit()
                return True
            return False
