class Nif():
    def __init__(self, numero):
        self.DNI = numero
    def get_letra(self):
        letras="TRWAGMYFPDXBNJZSQVHLCKEO"
        valor=int(self.DNI /23)
        valor*=23
        valor= self.DNI -valor;
        return letras[valor]

mio = Nif(int(6294962))
print(mio.get_letra())
