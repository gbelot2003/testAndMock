import pytest
from unittest.mock import patch, MagicMock
from app.services.action_handler import ActionHandleService
from app.actions.verify_contact_action import VerifyContactAction

# Prueba para verificar que el método `verificar_contacto` de `VerifyContactAction` es llamado correctamente
@patch('app.actions.verify_contact_action.VerifyContactAction.verificar_contacto')
def test_handle_action_verificar_contacto(mock_verificar_contacto):
    # Configurar el mock para retornar un contacto simulado
    mock_contacto = MagicMock()
    mock_verificar_contacto.return_value = mock_contacto

    # Crear una instancia de `ActionHandleService`
    prompt = "Hola, quiero verificar mi contacto."
    from_number = "123456789"
    action_service = ActionHandleService(prompt, from_number)

    # Llamar al método `handle_action`
    messages = action_service.handle_action()

    # Verificar que `verificar_contacto` se llamó con el número de teléfono correcto
    mock_verificar_contacto.assert_called_once_with(from_number)

    # Verificar que `handle_action` retorne la estructura correcta de `messages`
    assert isinstance(messages, list)
