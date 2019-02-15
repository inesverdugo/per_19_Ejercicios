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
        self.dia +1
        return self.dia, self.mes, self.año
h = Fecha(1,4,5)
print(h.comprobar())
