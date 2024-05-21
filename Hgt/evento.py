from tarea import Tarea

class Evento(Tarea):
    def __init__(self, fechaInicio, horaInicio, fechaFin, horaFin):
        self.fechaInicio = fechaInicio
        self.horaInicio  = horaInicio
        self.fechaFin    = fechaFin
        self.horaFin     = horaFin
    #Métodos CRUD
    def read(self):
        print(f"La tarea {self.tarea} empieza a {self.horaInicio} el {self.fechaInicio} y acaba a las {self.horaFin} el {self.fechaFin}.")

    def update(self, u_fechaInicio, u_horaInicio, u_fechaFin, u_horaFin):
        self.fechaInicio = u_fechaInicio
        self.horaInicio  = u_horaInicio
        self.fechaFin    = u_fechaFin
        self.horaFin     = u_horaFin

    def delete(self) -> None:
        self.fechaInicio = None
        self.horaInicio = None
        self.fechaFin = None
        self.horaFin = None