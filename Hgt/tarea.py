class Tarea:
    def __init__(self, id:int, tarea:str, estado:bool) -> None:
        self.id     = id
        self.tarea  = tarea
        self.estado = estado

    #Métodos CRUD
    def read(self):
        print (f"La tarea {self.tarea} con el id {self.id} esta {self.estado}.")
        return (f"La tarea {self.tarea} con el id {self.id} esta {self.estado}.")

    def update(self, id, tarea, estado):
        self.id = id
        self.tarea  = tarea
        self.estado = estado

    def delete(self)-> None:
        self.id = None
        self.tarea = None
        self.estado = None
        return self.id, self.tarea, self.estado
