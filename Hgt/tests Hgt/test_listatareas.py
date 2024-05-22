from Hgt.listatareas import ListaTareas
import pytest

@pytest.fixture
def lista():
    return ListaTareas()

# Test de la clase ListaAlumnos
def test_listaTarea0(lista):
    assert len(lista) == 0

def test_listaTarea1(lista):
    lista.agregar('Tarea1')
    assert len(lista) == 1

def test_listaTarea2(lista):
    lista.agregar('Tarea1')
    lista.agregar('Tarea2')

    assert len(lista) == 2

    assert lista[0] == 'Tarea1'
    assert lista[1] == 'Tarea2'

def test_listaTarea3(lista):
    lista.agregar('Tarea3')
    assert lista[0] == 'Tarea3'

    del lista[0]
    assert len(lista) == 0

    assert 'Tarea1' not in lista

def test_listaTarea4(lista):
    lista.agregar('Tarea1')
    lista.agregar('Tarea2')

    assert lista.read() == 'Tarea1' + lista.LIMITCHAR + 'Tarea2'

def test_listaTarea5(lista):
    lista.load('Tarea1' + lista.LIMITCHAR + 'Tarea2')
    assert len(lista) == 2

    assert lista[0] == 'Tarea1'
    assert lista[1] == 'Tarea2'