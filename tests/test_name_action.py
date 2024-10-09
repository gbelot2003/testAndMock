import pytest
from unittest.mock import patch, MagicMock
from app.actions.name_action import NameAction
from app.models.contact_model import Contact
from app.extractors.name_extractor import NombreExtractor
from app.repos.contact_repo import ContactRepo

# Mock de la clase Contact
class MockContact:
    def __init__(self, id, nombre=None):
        self.id = id
        self.nombre = nombre

# Mock de la función extraer_nombre
def mock_extraer_nombre(prompt):
    if "mi nombre es" in prompt.lower():
        return prompt.split("mi nombre es")[1].strip()
    return None

@pytest.fixture
def mock_contacto():
    return MockContact(id=1, nombre=None)

@pytest.fixture
def mock_contacto_con_nombre():
    return MockContact(id=2, nombre="Juan")

@patch('app.extractors.name_extractor.NombreExtractor.extraer_nombre', side_effect=mock_extraer_nombre)
@patch('app.repos.contact_repo.ContactRepo.actualizar_contacto')
def test_process_name_sin_nombre(mock_actualizar_contacto, mock_extraer_nombre, mock_contacto):
    name_action = NameAction(mock_contacto, "mi nombre es Pedro")
    message = name_action.process_name()
    assert message == {"role": "assistant", "content": "El usuario se llama y llamalo Pedro."}
    mock_actualizar_contacto.assert_called_once_with(mock_contacto.id, nombre="Pedro")

@patch('app.extractors.name_extractor.NombreExtractor.extraer_nombre', side_effect=mock_extraer_nombre)
@patch('app.repos.contact_repo.ContactRepo.actualizar_contacto')
def test_process_name_con_nombre(mock_actualizar_contacto, mock_extraer_nombre, mock_contacto_con_nombre):
    name_action = NameAction(mock_contacto_con_nombre, "mi nombre es Pedro")
    message = name_action.process_name()
    assert message == {"role": "assistant", "content": "El usuario se llama y llamalo Juan."}
    mock_actualizar_contacto.assert_not_called()

@patch('app.extractors.name_extractor.NombreExtractor.extraer_nombre', side_effect=mock_extraer_nombre)
@patch('app.repos.contact_repo.ContactRepo.actualizar_contacto')
def test_process_name_sin_extraer_nombre(mock_actualizar_contacto, mock_extraer_nombre, mock_contacto):
    name_action = NameAction(mock_contacto, "Hola, ¿cómo estás?")
    message = name_action.process_name()
    assert message == {"role": "system", "content": "pregunte al usuario en que le podemos ayudar y cual es su nombre para mejor servicio."}
    mock_actualizar_contacto.assert_not_called()