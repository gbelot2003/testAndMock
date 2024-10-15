from unittest.mock import MagicMock, patch
from app.services.action_handler import ActionHandleService
from app.actions.verify_contact_action import VerifyContactAction

@patch('app.services.action_handler.VerifyContactAction')
def test_handle_action_verificar_contacto(mock_verify_contact_action):
    # Crear un mock para la sesión de la base de datos
    mock_db_session = MagicMock()
    
    # Crear un mock para la acción de verificar contacto
    mock_verify_contact_action.return_value = MagicMock()
    mock_verify_contact_action.return_value.verificar_contacto.return_value = {
        'id': 1,
        'nombre': 'Carlos Sanchez',
        'telefono': '1122334455'
    }
    
    # Crear una instancia del servicio pasando mock_db_session
    action_handler = ActionHandleService(mock_db_session)
    
    # Ejecutar la acción y verificar el resultado
    resultado = action_handler.handle_action("verificar_contacto", {"telefono": "1122334455"})
    
    # Validar que se haya retornado el resultado esperado
    assert resultado == {
        'id': 1,
        'nombre': 'Carlos Sanchez',
        'telefono': '1122334455'
    }

@patch('app.services.action_handler.VerifyContactAction')
def test_handle_action_crear_contacto(mock_verify_contact_action):
    # Crear un mock para la sesión de la base de datos
    mock_db_session = MagicMock()
    
    # Simular la creación de un nuevo contacto
    mock_verify_contact_action.return_value = MagicMock()
    mock_verify_contact_action.return_value.verificar_contacto.return_value = {
        'id': 2,
        'nombre': 'Ana Lopez',
        'telefono': '2233445566'
    }
    
    # Crear una instancia del servicio pasando mock_db_session
    action_handler = ActionHandleService(mock_db_session)
    
    # Ejecutar la acción y verificar el resultado
    resultado = action_handler.handle_action("crear_contacto", {"telefono": "2233445566", "nombre": "Ana Lopez"})
    
    # Validar que se haya retornado el contacto creado correctamente
    assert resultado == {
        'id': 2,
        'nombre': 'Ana Lopez',
        'telefono': '2233445566'
    }
