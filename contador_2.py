class Contador():
    def __init__(self, numero=10):
        self.numero = numero
    def incrementar(self):
        return (self.numero +1)
    def disminuir(self):
        return (self.numero -1)
    def get_numero(self):
        return self.numero
    def set_numero(self, numero):
        self.numero= numero
       
g = Contador(2)
print(g.get_numero())
print(g.disminuir())
g.set_numero(2)
print(g.get_numero())
