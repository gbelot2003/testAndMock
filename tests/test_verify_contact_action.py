import pytest
from unittest.mock import patch, MagicMock
from app.actions.verify_contact_action import VerifyContactAction
from app.models.contact_model import Contact

# Prueba para verificar un contacto existente
@patch('app.actions.verify_contact_action.ContactRepo')
def test_verificar_contacto_existente(mock_contact_repo):
    # Simular un contacto existente
    mock_contacto = Contact(id=1, nombre="Juan Perez", telefono="123456789", direccion="Calle Falsa 123", email="juan.perez@example.com")
    mock_contact_repo.obtener_contacto_por_telefono.return_value = mock_contacto

    # Ejecutar la acción de verificar contacto
    resultado = VerifyContactAction.verificar_contacto("123456789")

    # Verificar que la función retorne el contacto correcto
    mock_contact_repo.obtener_contacto_por_telefono.assert_called_once_with("123456789")
    assert resultado == mock_contacto

# Prueba para crear un nuevo contacto si no existe
@patch('app.actions.verify_contact_action.ContactRepo')
def test_crear_contacto_si_no_existe(mock_contact_repo):
    # Simular que no existe un contacto con el número de teléfono
    mock_contact_repo.obtener_contacto_por_telefono.return_value = None

    # Simular la creación de un nuevo contacto
    mock_contacto_creado = Contact(id=2, nombre=None, telefono="987654321", direccion=None, email=None)
    mock_contact_repo.crear_contacto.return_value = mock_contacto_creado

    # Ejecutar la acción de verificar contacto con un número no existente
    resultado = VerifyContactAction.verificar_contacto("987654321")

    # Verificar que se intentó crear un nuevo contacto
    mock_contact_repo.crear_contacto.assert_called_once_with(telefono="987654321")

    # Verificar que el resultado es el contacto recién creado
    assert resultado == mock_contacto_creado

# Prueba para asegurar que el contacto se retorne después de crearlo
@patch('app.actions.verify_contact_action.ContactRepo')
def test_verificar_contacto_retorno_despues_de_crear(mock_contact_repo):
    # Simular que no existe un contacto con el número de teléfono
    mock_contact_repo.obtener_contacto_por_telefono.return_value = None

    # Simular la creación de un nuevo contacto
    mock_contacto_creado = Contact(id=3, nombre="Carlos Sanchez", telefono="1122334455", direccion="Calle Nueva 456", email="carlos.sanchez@example.com")
    mock_contact_repo.crear_contacto.return_value = mock_contacto_creado

    # Ejecutar la acción de verificar contacto con un número no existente
    resultado = VerifyContactAction.verificar_contacto("1122334455")

    # Verificar que se intentó crear un nuevo contacto
    mock_contact_repo.crear_contacto.assert_called_once_with(telefono="1122334455")

    # Verificar que el resultado es el contacto recién creado
    assert resultado == mock_contacto_creado
