import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Configuración de tu bot de Telegram
bot_token = "8169262271:AAF2moqkb5FBGjVsKjSAsIOfU_fbJjFmius"  
chat_id = "7045047535" 

# Función para enviar el mensaje a través de Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(f"Mensaje enviado a Telegram: {message}")
        else:
            print(f"Error al enviar mensaje: {response.status_code}")
    except Exception as e:
        print(f"Error al enviar mensaje a Telegram: {e}")

# Función para verificar las reservas
def check_reservations():
    try:
        url = "https://www.disfrutarbarcelona.com/reservas"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        response = requests.get(url, headers=headers)
        
        # Comprobar si la respuesta es válida
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Aquí buscaríamos algún texto o elemento en la página que nos indique disponibilidad
            # Por ejemplo, buscaremos un texto como "Reserva disponible" o similar
            availability = soup.find_all(text="Disponible")  # Ajusta esto según el contenido real de la página

            if availability:
                message = f"{datetime.now()}: ¡Hay reservas disponibles!"
                print(message)  # Imprimir en la pantalla
                send_telegram_message(f"¡Reserva disponible en Disfrutar! A las {datetime.now()}. ¡Date prisa!")  # Enviar a Telegram
            else:
                message = f"{datetime.now()}: No hay reservas disponibles."
                print(message)  # Imprimir en la pantalla
        else:
            print(f"Error al acceder a la página. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Error al comprobar reservas: {e}")

# Ejecución principal
if __name__ == "__main__":
    check_reservations()
