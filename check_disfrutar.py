import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Configuración de tu bot de Telegram
bot_token = "8169262271:AAF2moqkb5FBGjVsKjSAsIOfU_fbJjFmius"  # Cambia esto por el token de tu bot
chat_id = "7045047535"  # Cambia esto por tu chat ID

# Función para enviar el mensaje a través de Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
    }
    try:
        response = requests.post(url, data=payload)
        print(f"Respuesta de Telegram: {response.text}")
        if response.status_code == 200:
            print(f"Mensaje enviado a Telegram: {message}")
        else:
            print(f"Error al enviar mensaje: {response.status_code}")
    except Exception as e:
        print(f"Error al enviar mensaje a Telegram: {e}")

# Función para verificar las reservas
def check_reservations():
    try:
        print(f"{datetime.now()}: Comprobando disponibilidad de reservas...")  # Añadimos un print al inicio para saber si el script corre

        url = "https://www.disfrutarbarcelona.com/reservas"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        response = requests.get(url, headers=headers)

        # Comprobar si la respuesta es válida
        if response.status_code == 200:
            print(f"{datetime.now()}: Acceso exitoso a la página. Analizando contenido...")  # Confirmamos que la página fue cargada correctamente
            soup = BeautifulSoup(response.text, 'html.parser')

            # Buscar disponibilidad usando 'string' en vez de 'text'
            availability = soup.find_all(string="Disponible")  # Usamos 'string' en vez de 'text'

            if availability:
                message = f"{datetime.now()}: ¡Hay reservas disponibles!"
            else:
                message = f"{datetime.now()}: No hay reservas disponibles."

            print(message)  # Imprimir en la pantalla
            send_telegram_message(message)  # Enviar a Telegram

        else:
            print(f"{datetime.now()}: Error al acceder a la página. Código de estado: {response.status_code}")
            send_telegram_message(f"{datetime.now()}: Error al acceder a la página. Código de estado: {response.status_code}")  # Enviar error al Telegram

    except Exception as e:
        print(f"{datetime.now()}: Error al comprobar reservas: {e}")
        send_telegram_message(f"{datetime.now()}: Error al comprobar reservas: {e}")  # Enviar error al Telegram

# Ejecución principal
if __name__ == "__main__":
    check_reservations()
    
