import requests
from bs4 import BeautifulSoup
from datetime import datetime

# URL de la página de reservas
URL = "https://www.disfrutarbarcelona.com/reservas"

def check_reservations():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hora: {current_time}")

    try:
        # Hacer una petición HTTP a la página
        response = requests.get(URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Aquí analizamos el HTML para encontrar la disponibilidad
        # Nota: Reemplaza "CLASE_O_ELEMENTO" con el selector específico
        availability = soup.find_all("div", class_="CLASE_O_ELEMENTO")  # Cambia esto al selector correcto

        if availability:  # Si encuentra disponibilidad
            print("¡Hay reservas disponibles!")
        else:
            print("No hay reservas disponibles.")
    except Exception as e:
        print(f"Error al comprobar reservas: {e}")

# Ejecutar la función una vez
check_reservations()
