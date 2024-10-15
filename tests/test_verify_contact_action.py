from unittest.mock import MagicMock, patch
from app.models import Contact
from app.actions.verify_contact_action import VerifyContactAction

@patch('app.actions.verify_contact_action.ContactRepo')
def test_verificar_contacto_retorno_despues_de_crear(mock_contact_repo):
    # Crear un mock para la sesión de la base de datos
    mock_db_session = MagicMock()

    # Simular que no existe un contacto con el número de teléfono
    mock_contact_repo.obtener_contacto_por_telefono.return_value = None

    # Simular la creación de un nuevo contacto
    mock_contacto_creado = Contact(id=3, nombre="Carlos Sanchez", telefono="1122334455", direccion="Calle Nueva 456", email="carlos.sanchez@example.com")
    mock_contact_repo.crear_contacto.return_value = mock_contacto_creado

    # Ejecutar la acción de verificar contacto con un número no existente y pasar mock_db_session
    resultado = VerifyContactAction(mock_db_session).verificar_contacto("1122334455")

    # Validar que se haya retornado el contacto creado correctamente
    assert resultado == mock_contacto_creado

@patch('app.actions.verify_contact_action.ContactRepo')
def test_verificar_contacto_existente(mock_contact_repo):
    # Crear un mock para la sesión de la base de datos
    mock_db_session = MagicMock()
    
    # Simular un contacto existente en la base de datos
    contacto_existente = Contact(id=1, nombre="Juan Perez", telefono="1122334455", direccion="Calle Vieja 123", email="juan.perez@example.com")
    mock_contact_repo.obtener_contacto_por_telefono.return_value = contacto_existente

    # Verificar el contacto existente pasando mock_db_session
    resultado = VerifyContactAction(mock_db_session).verificar_contacto("1122334455")
    assert resultado == contacto_existente

@patch('app.actions.verify_contact_action.ContactRepo')
def test_crear_contacto_si_no_existe(mock_contact_repo):
    # Crear un mock para la sesión de la base de datos
    mock_db_session = MagicMock()
    
    # Simular que no existe un contacto con el número de teléfono
    mock_contact_repo.obtener_contacto_por_telefono.return_value = None

    # Simular la creación de un nuevo contacto
    mock_contacto_creado = Contact(id=2, nombre="Ana Lopez", telefono="2233445566", direccion="Avenida Central 789", email="ana.lopez@example.com")
    mock_contact_repo.crear_contacto.return_value = mock_contacto_creado

    # Ejecutar la acción de verificar contacto y pasar mock_db_session
    resultado = VerifyContactAction(mock_db_session).verificar_contacto("2233445566")
    assert resultado == mock_contacto_creado

