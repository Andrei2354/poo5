class Tarea:
    def __init__(self, id:int, tarea:str, estado:bool) -> None:
        self.id     = id
        self.tarea  = tarea
        self.estado = estado

    #Métodos CRUD
    def read(self):
        print(f"La tarea {self.tarea} con el id {self.id} esta {self.estado}.")

    def update(self, u_id:int, u_tarea:str, u_estado:bool):
        self.id     = u_id
        self.tarea  = u_tarea
        self.estado = u_estado

    def delete(self)-> None:
        self.id = None
        self.tarea = None
        self.estado = None
