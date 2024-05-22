from Hgt.tarea import Tarea

class ListaTareas:
    LIMITCHAR = "|&&|"

    def __init__(self):
        self.lista = []
    
    def agregar(self, tarea:Tarea):
        self.lista.append(tarea)
    
    def read(self):
        result = ""
        for tarea in self.lista:
            result += tarea
            if tarea != self.lista[-1]:
                result += self.LIMITCHAR

        return result
    
    def load(self, data:str):
        tareas = data.split(self.LIMITCHAR)
        for tarea in tareas:
            self.lista.append(tarea)
    
    def update(self, tarea:Tarea):
        for a in self.lista:
            if a == tarea:
                a.update(tarea)
                break
    
    def delete(self, tarea:Tarea):
        for a in self.lista:
            if a == tarea:
                a.delete(tarea)
                break



    def __str__(self):
        return self.read()
    
    def __len__(self):
        return  self.lista.__len__()
    
    def __getitem__(self, index):
        return self.lista[index]
    
    def __setitem__(self, index, value):
        self.lista[index] = value

    def __delitem__(self, index):
        del self.lista[index]

    def __iter__(self):
        return self.lista.__iter__()
    
    def __next__(self):
        return self.lista.__next__()
    
    def __contains__(self, item):
        return item in self.lista
    
    def __eq__(self, other):
        return self.lista == other.lista
    
    def __ne__(self, other):
        return self.lista != other.lista