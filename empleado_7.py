class Empleado():
    def __init__(self, nombre, sueldo, horas):
        self.nombre = nombre
        self.sueldo = sueldo
        self.horas = horas
    def get_sueldo(self):
        return self.sueldo
    def preciohora(self):
        return (self.sueldo/ self.horas)
a = Empleado("Inés", 200, 24)
print(a.preciohora())
print(a.get_sueldo())
