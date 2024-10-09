import pytest
from unittest.mock import patch, MagicMock
from app.actions.verify_contact_action import VerifyContactAction
from app.models.contact_model import Contact as Contacto
from app.repos.contact_repo import ContactRepo

# Mock de la clase Contact
class MockContact:
    def __init__(self, id, telefono):
        self.id = id
        self.telefono = telefono

@pytest.fixture
def mock_contacto():
    return MockContact(id=1, telefono="1234567890")

@patch('app.repos.contact_repo.ContactRepo.obtener_contacto_por_telefono')
@patch('app.repos.contact_repo.ContactRepo.crear_contacto')
def test_verificar_contacto_existente(mock_crear_contacto, mock_obtener_contacto_por_telefono, mock_contacto):
    # Configurar el mock para que devuelva un contacto existente
    mock_obtener_contacto_por_telefono.return_value = mock_contacto

    # Llamar al método a probar
    contacto = VerifyContactAction.verificar_contacto("1234567890")

    # Verificar que se llamó a obtener_contacto_por_telefono
    mock_obtener_contacto_por_telefono.assert_called_once_with("1234567890")

    # Verificar que no se llamó a crear_contacto
    mock_crear_contacto.assert_not_called()

    # Verificar que se devolvió el contacto existente
    assert contacto == mock_contacto

@patch('app.repos.contact_repo.ContactRepo.obtener_contacto_por_telefono')
@patch('app.repos.contact_repo.ContactRepo.crear_contacto')
def test_verificar_contacto_nuevo(mock_crear_contacto, mock_obtener_contacto_por_telefono, mock_contacto):
    # Configurar el mock para que devuelva None (no existe el contacto)
    mock_obtener_contacto_por_telefono.return_value = None

    # Configurar el mock para que devuelva un nuevo contacto
    mock_crear_contacto.return_value = mock_contacto

    # Llamar al método a probar
    contacto = VerifyContactAction.verificar_contacto("1234567890")

    # Verificar que se llamó a obtener_contacto_por_telefono
    mock_obtener_contacto_por_telefono.assert_called_once_with("1234567890")

    # Verificar que se llamó a crear_contacto
    mock_crear_contacto.assert_called_once_with(telefono="1234567890")

    # Verificar que se devolvió el nuevo contacto
    assert contacto == mock_contacto