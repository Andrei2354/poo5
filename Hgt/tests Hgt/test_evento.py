import pytest 
from Hgt.evento import Evento

@pytest.fixture
def evento1():
    return Evento(1, 3, 2, 7)

def test_reade(evento1):
    assert evento1.read() == (f"La tarea {1} empieza a {2} el {3} y acaba a las {4} el {7}.")

def test_updatee(evento1):
    evento1.update(2, 2, 2, 2)

    assert evento1.read() == (f"La tarea {2} empieza a {2} el {2} y acaba a las {2} el {2}.")

def test_deletee(evento1):
    assert evento1.delete() == (None, None, None, None)