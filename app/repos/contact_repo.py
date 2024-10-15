from sqlalchemy.orm import Session
from ..models.contact_model import Contact

class ContactRepo:
    @staticmethod
    def crear_contacto(db_session: Session, telefono, nombre=None, direccion=None, email=None):
        nuevo_contacto = Contact(nombre=nombre, telefono=telefono, direccion=direccion, email=email)
        db_session.add(nuevo_contacto)
        db_session.commit()
        return nuevo_contacto

    @staticmethod
    def obtener_contacto_por_telefono(db_session: Session, telefono):
        return db_session.query(Contact).filter_by(telefono=telefono).first()

    @staticmethod
    def obtener_todos_contactos(db_session: Session):
        return db_session.query(Contact).all()

    @staticmethod
    def actualizar_contacto(db_session: Session, contacto_id, nombre=None, telefono=None, direccion=None, email=None):
        contacto = db_session.query(Contact).filter_by(id=contacto_id).first()
        if contacto:
            if nombre:
                contacto.nombre = nombre
            if telefono:
                contacto.telefono = telefono
            if direccion:
                contacto.direccion = direccion
            if email:
                contacto.email = email
            db_session.commit()
        return contacto

    @staticmethod
    def agregar_direccion(db_session: Session, contact_id, direccion):
        """
        Agrega una nueva dirección asociada a un contacto en la base de datos.
        """
        contacto = db_session.query(Contact).filter_by(id=contact_id).first()
        if contacto:
            contacto.direccion = direccion
            db_session.commit()
        return contacto
