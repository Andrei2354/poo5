import pytest 
from Hgt.tarea import Tarea

@pytest.fixture
def tarea1():
    return Tarea(1, "nada", False)

def test_read(tarea1):
    assert tarea1.read() == (f"La tarea {"nada"} con el id {1} esta {False}.")

def test_update(tarea1):
    tarea1.update(1, "algo", True)

    assert tarea1.read() == (f"La tarea {"algo"} con el id {1} esta {True}.")

def test_delete(tarea1):
    assert tarea1.delete() == (None, None, None)