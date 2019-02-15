class Libro():
    def __init__(self, nombre, prestamo, devolucion):
        self.nombre = nombre
        self.prestamo = prestamo
        self.devolucion = devolucion
    def get_prestamo(self):
        return self.prestamo
    def get_devolucion(self):
        return self.devolucion
    def dame_info(self):
        return ("El libro: ", self.nombre,"prestado el día: ", self.devolucion, "debe ser devuelto el día: ", self.prestamo)
a = Libro("La sirenita", "14/2/2019", "15/3/2019")
print(a.dame_info())
