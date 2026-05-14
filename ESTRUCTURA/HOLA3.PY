class Animal:
    def hablar(self):
        print("Este animal emite un sonido")

class gato(Animal):
    def maullar(self):
        print("¡miau! ¡miau!")

class comida(Animal):
    def comer(self):
        print("Este animal está comiendo")

class caminar(Animal):
    def caminar(self):
        print("Este animal está caminando")        
mi_gato = gato()
mi_gato.hablar()
mi_gato.maullar()
mi_gato_come = comida()
mi_gato_come.comer()
mi_gato_caminar = caminar()
mi_gato_caminar.caminar()
