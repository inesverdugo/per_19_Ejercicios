class Persona(FechaNacimiento):
    def __init__(self, fechaNacimiento):
        self.fechaNacimiento = fechaNacimiento
    def get_cumple(self):
        return self.fechaNacimiento
class Fecha():
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
    def dame_info(self):
        return self.dia, self.mes, self.año
    def comprobar(self):
        if (1< self.dia<31) and (1<self.mes<= 12):
            return ("Dia correcto")
        else:
            return ("Día incorrecto")
    def cambio(self):
        self.dia = self.dia +1
        return self.dia, self.mes, self.año
class FechaNacimiento(Fecha):
    def __init__(self, dia, mes ,año):
        super().__init__(dia,mes,año)
        self.dia = dia
        self.mes = mes
        self.año = año
    def get_cumple(self):
        return self.dia, self.mes, self.año
        
a = FechaNacimiento(17, 2, 7)
print(a.comprobar())
b = Persona(a)
print(b.get_cumple().get_cumple())

