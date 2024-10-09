import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models.contact_model import Contact as Contacto
from app.models.address_model import Address
from app.repos.contact_repo import ContactRepo
from app import db

# Configuración de la base de datos en memoria para pruebas
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@pytest.fixture(scope="module")
def db_session():
    db.create_all(bind=engine)
    session = Session()
    yield session
    session.close()
    db.drop_all(bind=engine)

def test_crear_contacto(db_session):
    contacto = ContactRepo.crear_contacto(db_session, telefono="1234567890", nombre="Juan", direccion="Calle 123", email="juan@example.com")
    assert contacto.id is not None
    assert contacto.nombre == "Juan"
    assert contacto.telefono == "1234567890"
    assert contacto.direccion == "Calle 123"
    assert contacto.email == "juan@example.com"

def test_obtener_contacto_por_telefono(db_session):
    contacto = ContactRepo.crear_contacto(db_session, telefono="1234567890", nombre="Juan", direccion="Calle 123", email="juan@example.com")
    contacto_obtenido = ContactRepo.obtener_contacto_por_telefono(db_session, telefono="1234567890")
    assert contacto_obtenido.id == contacto.id
    assert contacto_obtenido.nombre == "Juan"
    assert contacto_obtenido.telefono == "1234567890"
    assert contacto_obtenido.direccion == "Calle 123"
    assert contacto_obtenido.email == "juan@example.com"

def test_obtener_todos_contactos(db_session):
    ContactRepo.crear_contacto(db_session, telefono="1234567890", nombre="Juan", direccion="Calle 123", email="juan@example.com")
    ContactRepo.crear_contacto(db_session, telefono="0987654321", nombre="Pedro", direccion="Avenida 456", email="pedro@example.com")
    contactos = ContactRepo.obtener_todos_contactos(db_session)
    assert len(contactos) == 2

def test_actualizar_contacto(db_session):
    contacto = ContactRepo.crear_contacto(db_session, telefono="1234567890", nombre="Juan", direccion="Calle 123", email="juan@example.com")
    contacto_actualizado = ContactRepo.actualizar_contacto(db_session, contacto.id, nombre="Juan Pérez", telefono="1111111111", direccion="Calle 456", email="juan.perez@example.com")
    assert contacto_actualizado.nombre == "Juan Pérez"
    assert contacto_actualizado.telefono == "1111111111"
    assert contacto_actualizado.direccion == "Calle 456"
    assert contacto_actualizado.email == "juan.perez@example.com"

def test_eliminar_contacto(db_session):
    contacto = ContactRepo.crear_contacto(db_session, telefono="1234567890", nombre="Juan", direccion="Calle 123", email="juan@example.com")
    contacto_eliminado = ContactRepo.eliminar_contacto(db_session, contacto.id)
    assert contacto_eliminado.id == contacto.id
    contacto_obtenido = ContactRepo.obtener_contacto_por_telefono(db_session, telefono="1234567890")
    assert contacto_obtenido is None

def test_agregar_direccion(db_session):
    contacto = ContactRepo.crear_contacto(db_session, telefono="1234567890", nombre="Juan", direccion="Calle 123", email="juan@example.com")
    direccion = Address(contact_id=contacto.id, type="principal", address_line="Calle 456", latitude=12.34, longitude=56.78, is_primary=True)
    direccion_agregada = ContactRepo.agregar_direccion(db_session, direccion)
    assert direccion_agregada.id is not None
    assert direccion_agregada.contact_id == contacto.id
    assert direccion_agregada.type == "principal"
    assert direccion_agregada.address_line == "Calle 456"
    assert direccion_agregada.latitude == 12.34
    assert direccion_agregada.longitude == 56.78
    assert direccion_agregada.is_primary is True

def test_actualizar_direccion(db_session):
    contacto = ContactRepo.crear_contacto(db_session, telefono="1234567890", nombre="Juan", direccion="Calle 123", email="juan@example.com")
    direccion_actualizada = ContactRepo.actualizar_direccion(db_session, contacto.id, direccion="Calle 456")
    assert direccion_actualizada.direccion == "Calle 456"