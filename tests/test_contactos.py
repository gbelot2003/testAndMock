import pytest
from app import create_app, db
from app.models.contact_model import Contact

# Configuración de la aplicación de pruebas
@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Base de datos en memoria para pruebas

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()  # Crear las tablas en la base de datos en memoria para pruebas
        yield testing_client  # Esto es lo que se pasa a cada test

    # Eliminar las tablas y la base de datos después de las pruebas
    with flask_app.app_context():
        db.drop_all()

# Prueba para crear un nuevo contacto
def test_crear_contacto(test_client):
    # Datos del contacto a crear
    contacto_data = {
        "nombre": "Juan Perez",
        "telefono": "123456789",
        "direccion": "Calle Falsa 123",
        "email": "juan.perez@example.com"
    }

    response = test_client.post('/api/contactos', json=contacto_data)
    assert response.status_code == 201
    data = response.get_json()
    assert data['nombre'] == contacto_data['nombre']
    assert data['telefono'] == contacto_data['telefono']
    assert data['direccion'] == contacto_data['direccion']
    assert data['email'] == contacto_data['email']

# Prueba para obtener un contacto por su número de teléfono
def test_obtener_contacto(test_client):
    # Crear contacto inicial
    contacto = Contact(nombre="Maria Lopez", telefono="987654321", direccion="Avenida Siempre Viva 456", email="maria.lopez@example.com")
    db.session.add(contacto)
    db.session.commit()

    response = test_client.get(f'/api/contactos/{contacto.telefono}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['nombre'] == contacto.nombre
    assert data['telefono'] == contacto.telefono
    assert data['direccion'] == contacto.direccion
    assert data['email'] == contacto.email

# Prueba para obtener todos los contactos
def test_obtener_todos_contactos(test_client):
    response = test_client.get('/api/contactos')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)  # Verificar que el resultado es una lista

# Prueba para actualizar un contacto (actualizar solo el nombre)
def test_actualizar_contacto_nombre(test_client):
    # Crear contacto inicial
    contacto = Contact(nombre="Carlos Mendoza", telefono="1122334455", direccion="Calle Principal 789", email="carlos.mendoza@example.com")
    db.session.add(contacto)
    db.session.commit()

    # Actualizar el nombre del contacto
    nuevo_nombre = {"nombre": "Carlos M."}
    response = test_client.put(f'/api/contactos/{contacto.id}', json=nuevo_nombre)
    assert response.status_code == 200
    data = response.get_json()
    assert data['nombre'] == nuevo_nombre['nombre']

# Prueba para actualizar la dirección del contacto
def test_actualizar_direccion_contacto(test_client):
    # Crear contacto inicial
    contacto = Contact(nombre="Ana Torres", telefono="5544332211", direccion="Calle Secundaria 999", email="ana.torres@example.com")
    db.session.add(contacto)
    db.session.commit()

    # Actualizar la dirección del contacto
    nueva_direccion = {"direccion": "Calle Nueva 123"}
    response = test_client.put(f'/api/contactos/{contacto.id}/direccion', json=nueva_direccion)
    assert response.status_code == 200
    data = response.get_json()
    assert data['direccion'] == nueva_direccion['direccion']

# Prueba para verificar la actualización de contacto no encontrado
def test_actualizar_contacto_no_encontrado(test_client):
    # Intentar actualizar un contacto con ID inexistente
    contacto_id_inexistente = 999
    nuevo_nombre = {"nombre": "Nombre No Encontrado"}
    response = test_client.put(f'/api/contactos/{contacto_id_inexistente}', json=nuevo_nombre)
    assert response.status_code == 404
    data = response.get_json()
    assert "Contacto no encontrado" in data['error']

# Prueba para verificar la obtención de un contacto no encontrado
def test_obtener_contacto_no_encontrado(test_client):
    response = test_client.get('/api/contactos/999999999')  # Un número de teléfono no registrado
    assert response.status_code == 404
    data = response.get_json()
    assert "Contacto no encontrado" in data['error']
