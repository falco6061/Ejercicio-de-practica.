class veterinaria:
    def tipo_animal():
        especie = input("Ingrese el tipo de animal")
        peso = input("Ingrese el peso del animal")
        problema = input("¿Que problema tiene?")

class perro(veterinaria):
    print("Es un perro")
    print("5kg")
    print("Se que quebro la pata")

class gato(veterinaria):
    print("Es un Gato")
    print("6kg")
    print("se esta quedando ciego")

class cobro_veterinaria(veterinaria):
    def cobrar(self):
        print("la consulta sale 20.000")
    
