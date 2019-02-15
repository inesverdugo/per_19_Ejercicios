class Alumno():
    def __init__(self, matricula, nombre, nota1, nota2, nota3):
        self.matricula = matricula
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    def dame_matricula(self):
        return self.matricula
    def dame_nombre(self):
        return self.nombre
    def dame_nota(self):
        notafinal = (self.nota1 + self.nota2 + self.nota3 )/3
        return notafinal
def Alumnos(x):
    if x.dame_nota() >= 4.8:
        datos = "El alumno:", x.dame_nombre(),"con matrícula", x.dame_matricula(), "aprobó"
        return datos
    else:
        datos = "El alumno:", x.dame_nombre(),"con matrícula", x.dame_matricula(), "suspendió"
        return datos
a = Alumno(23232, "Ines", 3,4,5)
Alumnos(a)
