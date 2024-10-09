import pytest
from app.extractors.name_extractor import NombreExtractor

@pytest.fixture
def nombre_extractor():
    return NombreExtractor()

def test_extraer_nombre_me_llamo(nombre_extractor):
    texto = "Me llamo Juan"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Juan"

def test_extraer_nombre_mi_nombre_es(nombre_extractor):
    texto = "Mi nombre es Pedro"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Pedro"

def test_extraer_nombre_puedes_llamarme(nombre_extractor):
    texto = "Puedes llamarme Ana"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Ana"

def test_extraer_nombre_soy(nombre_extractor):
    texto = "Soy Carlos"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Carlos"

def test_extraer_nombre_nombre(nombre_extractor):
    texto = "Nombre: Maria"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Maria"

def test_extraer_nombre_me_dicen(nombre_extractor):
    texto = "Me dicen Luis"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Luis"

def test_extraer_nombre_mis_amigos_me_llaman(nombre_extractor):
    texto = "Mis amigos me llaman Sofia"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Sofia"

def test_extraer_nombre_llamame(nombre_extractor):
    texto = "Llámame Roberto"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Roberto"

def test_extraer_nombre_dime(nombre_extractor):
    texto = "Dime Elena"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Elena"

def test_extraer_nombre_yo_soy(nombre_extractor):
    texto = "Yo soy Pablo"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Pablo"

def test_extraer_nombre_es(nombre_extractor):
    texto = "Es Juan"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Juan"

def test_extraer_nombre_soy_el_la(nombre_extractor):
    texto = "Soy el Juan"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Juan"

def test_extraer_nombre_por_favor_llamame(nombre_extractor):
    texto = "Por favor, llámame Ana"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Ana"

def test_extraer_nombre_hola(nombre_extractor):
    texto = "Hola, Juan"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Juan"

def test_extraer_nombre_hola_me_llamo(nombre_extractor):
    texto = "Hola, me llamo Pedro"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Pedro"

def test_extraer_nombre_hola_mi_nombre_es(nombre_extractor):
    texto = "Hola, mi nombre es Ana"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Ana"

def test_extraer_nombre_hola_puedes_llamarme(nombre_extractor):
    texto = "Hola, puedes llamarme Luis"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Luis"

def test_extraer_nombre_hola_soy(nombre_extractor):
    texto = "Hola, soy Carlos"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Carlos"

def test_extraer_nombre_hola_me_dicen(nombre_extractor):
    texto = "Hola, me dicen Sofia"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Sofia"

def test_extraer_nombre_hola_mis_amigos_me_llaman(nombre_extractor):
    texto = "Hola, mis amigos me llaman Roberto"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Roberto"

def test_extraer_nombre_hola_llamame(nombre_extractor):
    texto = "Hola, llámame Elena"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Elena"

def test_extraer_nombre_hola_dime(nombre_extractor):
    texto = "Hola, dime Pablo"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Pablo"

def test_extraer_nombre_hola_yo_soy(nombre_extractor):
    texto = "Hola, yo soy Juan"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Juan"

def test_extraer_nombre_hola_es(nombre_extractor):
    texto = "Hola, es Ana"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Ana"

def test_extraer_nombre_hola_soy_el_la(nombre_extractor):
    texto = "Hola, soy el Juan"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Juan"

def test_extraer_nombre_hola_por_favor_llamame(nombre_extractor):
    texto = "Hola, por favor, llámame Luis"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre == "Luis"

def test_extraer_nombre_sin_nombre(nombre_extractor):
    texto = "Hola, ¿cómo estás?"
    nombre = nombre_extractor.extraer_nombre(texto)
    assert nombre is None