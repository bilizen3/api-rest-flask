class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def year(self):
        print("year: "+str(self.age))

class Ingeniero(Person):
    def programar(self,programa):
        print("se programar en "+programa)

class Medico(Person):
    def curar(self,enfermedad):
        print("Esta es una enfermedad "+enfermedad)
