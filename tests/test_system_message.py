import pytest
from unittest.mock import patch
from app.services.system_message import SystemMessage

# Crear una clase para simular la respuesta de OpenAI con atributos en lugar de diccionarios
class MockChoice:
    def __init__(self, message_content):
        self.message = MockMessage(message_content)

class MockMessage:
    def __init__(self, content):
        self.content = content

class MockResponse:
    def __init__(self, choices):
        self.choices = choices

# Crear un método que simule la respuesta de OpenAI, devolviendo la estructura correcta
def mock_openai_response(model, messages, max_tokens, temperature):
    return MockResponse(choices=[
        MockChoice(message_content="Respuesta simulada del modelo")
    ])

@pytest.fixture
def system_message():
    return SystemMessage()

@patch('app.services.system_message.client.chat.completions.create', side_effect=mock_openai_response)
def test_handle_request(mock_create, system_message):
    prompt = "Hola, ¿cómo estás?"
    response = system_message.handle_request(prompt)
    # Comparar con el resultado esperado
    assert response == "Respuesta simulada del modelo"
