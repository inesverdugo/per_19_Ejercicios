class Cuenta():
    def __init__(self, saldo = 2):
        self.saldo = saldo
    def get_ingreso(self, x):
        return (self.saldo + self.x)
    def get_reintegro(self, x):
        return (self.x)
    def get_transferencia(self,x):
        return (self.saldo - self.x)


a = Cuenta()
print(a.get_ingreso())

print(a.get_reintegro())
