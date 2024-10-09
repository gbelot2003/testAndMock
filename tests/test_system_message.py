import pytest
from unittest.mock import patch, MagicMock
from app.services.system_message import SystemMessage
from app.services.action_handler import ActionHandleService

@patch('app.services.system_message.ActionHandleService')
@patch('app.services.system_message.client.chat.completions.create')
def test_handle_request(mock_create, mock_action_handle_service):
    # Configurar el mock para que devuelva un mensaje de acción
    mock_action_handle_service_instance = mock_action_handle_service.return_value
    mock_action_handle_service_instance.handle_actions.return_value = [
        {"role": "assistant", "content": "El usuario se llama y llamalo Juan."}
    ]

    # Configurar el mock para que devuelva una respuesta de OpenAI
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "Hola, Juan. ¿En qué puedo ayudarte hoy?"
    mock_create.return_value = mock_response

    # Crear una instancia de SystemMessage
    system_message = SystemMessage()

    # Llamar al método a probar
    respuesta = system_message.handle_request(prompt="Hola, mi nombre es Juan", user_id="1234567890")

    # Verificar que se llamó a handle_actions
    mock_action_handle_service_instance.handle_actions.assert_called_once()

    # Verificar que se llamó a la API de OpenAI
    mock_create.assert_called_once_with(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": "El usuario se llama y llamalo Juan."},
            {"role": "user", "content": "Hola, mi nombre es Juan"}
        ],
        max_tokens=550,
        temperature=0.1
    )

    # Verificar que se devolvió la respuesta esperada
    assert respuesta == "Hola, Juan. ¿En qué puedo ayudarte hoy?"

@patch('app.services.system_message.ActionHandleService')
@patch('app.services.system_message.client.chat.completions.create')
def test_handle_request_exception(mock_create, mock_action_handle_service):
    # Configurar el mock para que devuelva un mensaje de acción
    mock_action_handle_service_instance = mock_action_handle_service.return_value
    mock_action_handle_service_instance.handle_actions.return_value = [
        {"role": "assistant", "content": "El usuario se llama y llamalo Juan."}
    ]

    # Configurar el mock para que levante una excepción
    mock_create.side_effect = Exception("Error en la API de OpenAI")

    # Crear una instancia de SystemMessage
    system_message = SystemMessage()

    # Llamar al método a probar
    with pytest.raises(Exception) as exc_info:
        system_message.handle_request(prompt="Hola, mi nombre es Juan", user_id="1234567890")

    # Verificar que se llamó a handle_actions
    mock_action_handle_service_instance.handle_actions.assert_called_once()

    # Verificar que se llamó a la API de OpenAI
    mock_create.assert_called_once_with(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": "El usuario se llama y llamalo Juan."},
            {"role": "user", "content": "Hola, mi nombre es Juan"}
        ],
        max_tokens=550,
        temperature=0.1
    )

    # Verificar que se levantó la excepción
    assert str(exc_info.value) == "Error en la API de OpenAI: Error en la API de OpenAI"