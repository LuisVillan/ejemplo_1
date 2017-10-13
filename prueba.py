class Persona:
    def __init__(self, nom, apePat, apeMat):
        self.nombre=nom
        self.apellidoPa=apePat
        self.apellidoMa=apeMat

    def mostrarApellidos(self):
        return '{} {}'.format(self.apellidoPa, self.apellidoMa)


def main():
    luis=Persona("Luis","Villanueva","Arrisueño")
    print('Mis apellidos son: ' + luis.mostrarApellidos())

if __name__=='__main__':
    main()
