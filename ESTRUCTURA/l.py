class veterinaria:
    # Agregamos 'self' para que sea un método correcto de clase
    def tipo_animal(self):
        global especie, peso, problema
        especie = str(input("Ingrese el tipo de animal (perro/gato): ")).strip().lower()
        peso = str(input("Ingrese el peso del animal: "))
        problema = str(input("¿Qué problema tiene? Eliga cuales de estos problemas tiene:"))
        print(problema)
class gato(veterinaria):
    def mostrar_gato(self):    
        print("--- Ficha del Animal ---")
        print(especie)
        print(peso)
        print(problema)

class cobro_veterinaria(veterinaria):
    def cobrar(self):
        print("La consulta sale $20.000")

# --- AQUÍ EMPIEZA LA EJECUCIÓN DEL PROGRAMA ---

# 1. Creamos una instancia de la veterinaria para poder usar su método
mi_veterinaria = veterinaria()

# 2. LLAMAMOS a la función para que el usuario ingrese los datos y se cree 'especie'
mi_veterinaria.tipo_animal()

# 3. Ahora que las variables globales existen, hacemos las comparaciones
if especie == "perro":
    # Creamos el objeto perro y llamamos a su función
    perro_actual = perro()
    perro_actual.mostrar_perro()
    
    # Creamos el objeto cobro y llamamos a su función
    cobro = cobro_veterinaria()
    cobro.cobrar()

elif especie == "gato":
    # Creamos el objeto gato y llamamos a su función
    gato_actual = gato()
    gato_actual.mostrar_gato()
    
    cobro = cobro_veterinaria()
    cobro.cobrar()

else:
    print("Tipo de animal no reconocido.")