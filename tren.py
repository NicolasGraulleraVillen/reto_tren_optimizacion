import random

class Tren:

    def __init__(self, n_vagones):
        
        #Atributos de instancia
        self.n_vagones = n_vagones
        self.vagones = []

        for i in range(n_vagones):
            self.vagones.append(Vagon())
    
    def __str__(self):
        descripcion_tren = []

        for i in range(self.n_vagones):
            estado_luz = "Encendida" if self.vagones[i].luz else "Apagada"

            descripcion_tren.append(f"Posicion: {i}, Luz: {estado_luz}")

        return "\n".join(descripcion_tren)
    
    def get_vagon(self, indice):

        indice_circular = indice % self.n_vagones
        return self.vagones[indice_circular]


class Vagon:

    def __init__(self):

        n = random.randint(0,1)
        self.luz = (n == 1) 