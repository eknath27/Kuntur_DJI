from unittest.mock import MagicMock
from djitellopy import Tello
import time

# Simulación de la clase Tello
tello_mock = MagicMock()

# Simula los métodos que el dron normalmente tendría
tello_mock.move_to = MagicMock()
tello_mock.takeoff = MagicMock()
tello_mock.land = MagicMock()
tello_mock.streamon = MagicMock()
tello_mock.streamoff = MagicMock()
tello_mock.get_frame_read = MagicMock(return_value="Simulando video")

# Definir la ruta con coordenadas de ejemplo
ruta = [
    (40.748817, -73.985428),  # Ejemplo: Coordenadas de la primera ubicación
    (40.748820, -73.985400),  # Coordenadas de la segunda ubicación
    (40.748835, -73.985380)   # Coordenadas de la tercera ubicación
]

# Función para simular el vuelo de la ruta
def simular_ruta():
    tello_mock.takeoff()  # Simula el despegue
    print("Despegando...")

    # Iterar sobre la ruta y simular el movimiento
    for lat, lon in ruta:
        tello_mock.move_to(lat, lon)  # Simula el movimiento a la coordenada
        print(f"Simulando movimiento a: Lat={lat}, Lon={lon}")
        time.sleep(2)  # Pausa para simular el tiempo entre movimientos
    
    tello_mock.land()  # Simula el aterrizaje
    print("Aterrizando...")

# Inicia la simulación de la ruta
simular_ruta()

# Simulamos que el dron está transmitiendo video
print(tello_mock.get_frame_read())  # Esto simula el video
