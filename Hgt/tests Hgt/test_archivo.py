from Hgt.listatareas import ListaTareas
from Hgt.archivo import Archivo
import pytest
import os

NombreArchivo = 'lista.dat'
DATA    = 'Tarea1' + ListaTareas.LIMITCHAR + 'Tarea2'

@pytest.fixture
def archivo():
    return Archivo(NombreArchivo)

def test_archivoLeer(archivo):
    os.remove(NombreArchivo)
    assert archivo.leer() == ''

def test_archivoEscribir(archivo):
    assert archivo.escribir(DATA) == True

def test_archivoLeer2(archivo):
    assert archivo.leer() == DATA

def test_archivoListaTareas(archivo):
    lista = ListaTareas()
    lista.load(archivo.leer())
    assert lista.read() == DATA