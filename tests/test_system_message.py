import pytest
from unittest.mock import patch, MagicMock
from app.services.system_message import SystemMessage

# Simulación de la estructura de respuesta de OpenAI con objetos y atributos en lugar de diccionarios
class MockChoice:
    def __init__(self, message_content):
        self.message = MockMessage(message_content)

class MockMessage:
    def __init__(self, content):
        self.content = content

class MockResponse:
    def __init__(self, choices):
        self.choices = choices

# Método para simular la respuesta de OpenAI usando la estructura correcta
def mock_openai_response(model, messages, max_tokens, temperature):
    return MockResponse(choices=[
        MockChoice(message_content="Respuesta simulada del modelo")
    ])

@pytest.fixture
def system_message():
    return SystemMessage()

# Mock de ActionHandleService para evitar errores en el flujo
@patch('app.services.system_message.ActionHandleService')
# Actualizar el patch para que coincida con la ruta del cliente OpenAI utilizado en `system_message.py`
@patch('app.services.system_message.client.chat.completions.create', side_effect=mock_openai_response)
def test_handle_request(mock_create, mock_action_service, system_message):
    # Simular que handle_action retorna un mensaje inicial vacío o con estructura esperada
    mock_action_service_instance = MagicMock()
    mock_action_service.return_value = mock_action_service_instance
    mock_action_service_instance.handle_action.return_value = [{"role": "system", "content": "Mensaje inicial"}]

    # Definir el prompt de prueba
    prompt = "Hola, ¿cómo estás?"

    # Definir un número de teléfono simulado para from_number
    from_number = "123456789"

    # Imprimir el estado inicial antes de llamar a handle_request
    print(f"Estado inicial de mock_action_service_instance.handle_action.call_count: {mock_action_service_instance.handle_action.call_count}")

    # Ejecutar la función handle_request con prompt y from_number
    response = system_message.handle_request(prompt, from_number)

    # Imprimir el valor de messages después de llamar a handle_action
    print(f"Mensajes en handle_request: {mock_create.call_args.kwargs['messages']}")

    # Verificar el estado del llamado después de ejecutar handle_request
    print(f"Estado final de mock_action_service_instance.handle_action.call_count: {mock_action_service_instance.handle_action.call_count}")

    # Verificar que la respuesta del método sea la esperada
    assert response == "Respuesta simulada del modelo"

    # Verificar que ActionHandleService.handle_action haya sido llamado
    mock_action_service_instance.handle_action.assert_called_once_with(from_number)

    # Verificar que la función `client.chat.completions.create` se haya llamado con los argumentos esperados
    expected_messages = [
        {"role": "system", "content": "Mensaje inicial"},  # Mensaje inicial retornado por handle_action
        {"role": "user", "content": prompt}                # Mensaje del usuario
    ]
    mock_create.assert_called_once_with(
        model="gpt-3.5-turbo",
        messages=expected_messages,
        max_tokens=550,
        temperature=0.1
    )