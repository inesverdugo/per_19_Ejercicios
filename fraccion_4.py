class Fraccion():
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    def suma(self):
        return (self.numero1 + self.numero2)
    def resta(self):
        return (self.numero1 - self.numero2)
    def multiplica(self):
        return (self.numero1 * self.numero2)
    def divide(self):
        return (self.numero1 / self.numero2)
a = Fraccion(1/3, 1/4)
print(a.divide())
