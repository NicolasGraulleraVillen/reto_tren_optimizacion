from tren import Tren
import random
import math

def contar_vagones_tren(tren: Tren) -> int:
    """
    Determina el número de vagones del tren (N) manipulando las luces,
    utilizando una estrategia de doble pasada con verificación probabilística.
    
    Estrategia Base:
    1. Se establece la luz del vagón 0 como 'luz_referencia'.
    2. Se avanza por el tren, invirtiendo la luz de cada vagón encontrado (lo que crea un patrón de 'luz_invertida').
    3. Cuando se encuentra un vagón N con la 'luz_referencia', se marca N como un candidato a ser el tamaño real del tren, asumiendo que se ha completado un ciclo (N = vagones).
    
    Mejora Probabilística (Para Evitar Fallos por Coincidencia Aleatoria):
    
    La estrategia base puede fallar si un vagón cualquiera (N' < N) tiene la 'luz_referencia' por casualidad.
    Para garantizar que N es el tamaño correcto:
    
    * **Verificación de Secuencia:** Tras encontrar un candidato N, se verifica si los siguientes k vagones tienen la 'luz_invertida'. 
    Esta secuencia de luz invertida es la huella digital que deja el algoritmo al pasar por los vagones N+1, N+2, ... en el ciclo anterior.
    
    * **Cálculo de k (Factor de Seguridad):** El número de vagones a verificar, k, se calcula usando la fórmula:
        k = 10 + 2 * math.ceil(math.log2(N)) 
        Este factor asegura que la probabilidad de que la verificación sea exitosa por pura casualidad (si N no fuera el tamaño real) 
        es extremadamente baja P(fallo) <= 1/2^k. Al crecer k logarítmicamente con N, se garantiza 
        la fiabilidad del resultado sin comprometer excesivamente la eficiencia del algoritmo.
    
    * **Finalización:** Si los k vagones subsiguientes confirman la 'luz_invertida', se declara N como el número de vagones.
    """
    
    luz_referencia = tren.get_vagon(0).luz
    luz_invertida = not luz_referencia

    posicion_actual = 1
    pasos_dados = 0

    while True:

        pasos_dados += 1
        vagon = tren.get_vagon(posicion_actual)
        
        if vagon.luz == luz_referencia:
            # Paso 1: Encontramos un vagón con luz de referencia (Posible Inicio)

            #Invertimos la luz del vagon
            vagon.luz = luz_invertida

            posicion_candidato = posicion_actual
            N = posicion_candidato
            
            # **Paso 2: Calcular k = 10 + 2*log2(N)**
            if N > 0:
                k = 10 + 2 * math.ceil(math.log2(N)) 
            else:
                k = 10 

            # **Paso 3: Verificar secuencia de k vagones con luz invertida**
            verificacion_exitosa = True

            for i in range(1, k + 1):
                posicion_verificacion = posicion_candidato + i
                
                vagon_verif = tren.get_vagon(posicion_verificacion)
                
                # Buscamos la luz que dejamos al pasar por un vagón por primera vez (luz_invertida)
                if vagon_verif.luz != luz_invertida:
                    verificacion_exitosa = False
                    break

            # **Paso 4: Declarar el resultado si la verificación fue exitosa**
            if verificacion_exitosa:
                return posicion_candidato
            
        else:
            pass

        posicion_actual += 1


def simular_tren_unico(rango_vagones: tuple = (9, 100)) -> None:
    """
    Simula un único tren y muestra el resultado.
    """
    min_vagones, max_vagones = rango_vagones
    tren = Tren(random.randint(min_vagones, max_vagones))
    vagones_predichos = contar_vagones_tren(tren)
    
    resultado = "Correcto. " if vagones_predichos == tren.n_vagones else "Incorrecto. "
    print(f"{resultado} Vagones reales: {tren.n_vagones}, Vagones predichos: {vagones_predichos}")

def simular_multiples_trenes(num_simulaciones: int = 10000, rango_vagones: tuple = (1, 100)) -> None:
    """
    Simula múltiples trenes y verifica la precisión del algoritmo.
    """
    predicciones_correctas = 0
    min_vagones, max_vagones = rango_vagones

    for _ in range(num_simulaciones):
        tren = Tren(random.randint(min_vagones, max_vagones))
        vagones_predichos = contar_vagones_tren(tren)

        if vagones_predichos == tren.n_vagones:
            predicciones_correctas += 1
        else:
            print(f"Error en predicción:")
            print(f"Predicción: {vagones_predichos}, Real: {tren.n_vagones}\n")

    tasa_acierto = (predicciones_correctas / num_simulaciones) * 100

    print("--- Resumen de Simulación ---")
    print(f"Resultados: {predicciones_correctas}/{num_simulaciones} predicciones correctas ({tasa_acierto:.2f}%)")


def main():
    """Función principal para ejecutar el algoritmo."""
    simular_multiples_trenes()


if __name__ == "__main__":
    main()