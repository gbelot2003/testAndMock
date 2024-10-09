import pytest
from unittest.mock import patch, MagicMock
from app.services.action_handler import ActionHandleService
from app.actions.name_action import NameAction
from app.actions.verify_contact_action import VerifyContactAction
from app.models.contact_model import Contact as Contacto

# Mock de la clase Contact
class MockContact:
    def __init__(self, id, telefono, nombre=None):
        self.id = id
        self.telefono = telefono
        self.nombre = nombre

@pytest.fixture
def mock_contacto():
    return MockContact(id=1, telefono="1234567890", nombre="Juan")

@patch('app.actions.verify_contact_action.VerifyContactAction.verificar_contacto')
@patch('app.actions.name_action.NameAction.process_name')
def test_handle_action_with_existing_contact(mock_process_name, mock_verificar_contacto, mock_contacto):
    # Configurar el mock para que devuelva un contacto existente
    mock_verificar_contacto.return_value = mock_contacto

    # Configurar el mock para que devuelva un mensaje de nombre
    mock_process_name.return_value = {"role": "assistant", "content": "El usuario se llama y llamalo Juan."}

    # Crear una sesión de base de datos simulada
    db_session = MagicMock()

    # Crear una instancia de ActionHandleService
    action_handler = ActionHandleService(user_id="1234567890", prompt="Hola, mi nombre es Juan", db_session=db_session)

    # Llamar al método a probar
    messages = action_handler.handle_action()

    # Verificar que se llamó a verificar_contacto
    mock_verificar_contacto.assert_called_once_with("1234567890")

    # Verificar que se llamó a process_name
    mock_process_name.assert_called_once()

    # Verificar que se devolvió el mensaje esperado
    assert messages == [{"role": "assistant", "content": "El usuario se llama y llamalo Juan."}]

@patch('app.actions.verify_contact_action.VerifyContactAction.verificar_contacto')
@patch('app.actions.name_action.NameAction.process_name')
def test_handle_action_with_new_contact(mock_process_name, mock_verificar_contacto, mock_contacto):
    # Configurar el mock para que devuelva un contacto nuevo
    mock_verificar_contacto.return_value = MockContact(id=2, telefono="0987654321")

    # Configurar el mock para que devuelva un mensaje de nombre
    mock_process_name.return_value = {"role": "assistant", "content": "El usuario se llama y llamalo Pedro."}

    # Crear una sesión de base de datos simulada
    db_session = MagicMock()

    # Crear una instancia de ActionHandleService
    action_handler = ActionHandleService(user_id="0987654321", prompt="Hola, mi nombre es Pedro", db_session=db_session)

    # Llamar al método a probar
    messages = action_handler.handle_action()

    # Verificar que se llamó a verificar_contacto
    mock_verificar_contacto.assert_called_once_with("0987654321")

    # Verificar que se llamó a process_name
    mock_process_name.assert_called_once()

    # Verificar que se devolvió el mensaje esperado
    assert messages == [{"role": "assistant", "content": "El usuario se llama y llamalo Pedro."}]