class Alumno:

    instancia=None

    @classmethod
    def get_instance(cls):
        if cls.instancia==None:
            cls.instancia=Alumno()
        return cls.instancia

def main():

    pepito=Alumno.get_instance()
    pepito.codigo='20188'
    pepito.ciclo=8
    Alumno.tipo='pregrado'
    print(pepito.codigo)
    raulito=Alumno.get_instance()
    print(raulito.codigo)
    raulito.ciclo=3
    print(pepito.ciclo)
    print(Alumno.tipo)


if __name__=='__main__':
    main()
        
