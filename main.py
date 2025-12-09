from tren import Tren
import random

def contar_vagones_tren(tren: Tren) -> int:
    """
    Determina el número de vagones del tren manipulando las luces.
    
    Estrategia:
    1. Mantener la luz del vagón 0 como referencia
    2. Invertir las luces de todos los vagones subsiguientes
    3. Cuando encontremos un vagón con la luz original después de n inversiones,
       significa que hemos dado la vuelta completa (n = número de vagones)

    Si no se conoce el minimo de vagones el algoritmo puede fallar. Ejemplo:

    TREN = [E,A,A,E,A,A,A,A,A,E] (E = Encendido, A = Apagado)
        - Cuando llega a el vagon de la posicion 4, checkea si es el inicio o no. 
        - Como el tren se ha generado con un patron con muchos apagados seguidos, detectara incorrectamente que esa posicion 4 es el inicio y el algoritmo fallara. 

    Al utilizar el minimo de vagones como condicion, ...
    """
    MINIMO_VAGONES = 9 #Sin esta pista el algoritmo puede fallar. 
    
    luz_referencia = tren.get_vagon(0).luz
    posicion_actual = 1
    posicion_candidato = -1 #No hay
    vagones_invertidos_consecutivos = 0

    while True:
        vagon = tren.get_vagon(posicion_actual)

        if vagon.luz == luz_referencia:
            # Encontramos un vagón con luz original: invertimos y marcamos como candidato
            vagon.luz = not luz_referencia
            vagones_invertidos_consecutivos = 0
            posicion_candidato = posicion_actual
        else:
            # Vagón con luz invertida: incrementamos contador
            vagones_invertidos_consecutivos += 1

        posicion_actual += 1

        # Usar la condicion del minimo para asegurar que se han recorrido un numero de vagones minimo. 
        if posicion_candidato >= MINIMO_VAGONES:
            if vagones_invertidos_consecutivos == (posicion_candidato - 1):
                return posicion_candidato



def simular_tren_unico(rango_vagones: tuple = (9, 100)) -> None:
    """
    Simula un único tren y muestra el resultado.
    
    """
    min_vagones, max_vagones = rango_vagones
    tren = Tren(random.randint(min_vagones, max_vagones))
    vagones_predichos = contar_vagones_tren(tren)
    
    resultado = "✓" if vagones_predichos == tren.n_vagones else "✗"
    print(f"{resultado} Vagones reales: {tren.n_vagones}, Vagones predichos: {vagones_predichos}")


def main():
    """Función principal para ejecutar el algoritmo."""
    # Descomentar para ejecutar múltiples simulaciones:
    # simular_multiples_trenes(num_simulaciones=100, rango_vagones=(9, 15))
    
    # Simulación de un único tren:
    simular_tren_unico(rango_vagones=(9, 100))


if __name__ == "__main__":
    main()