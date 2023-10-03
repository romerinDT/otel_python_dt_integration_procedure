import requests
import time
import random

def send_get_request(ip_address):
    url = f"http://{ip_address}:8080/data"
    response = requests.get(url)
    print(f"GET Response: {response.status_code}")

def send_post_request(ip_address):
    url = f"http://{ip_address}:8080/data"
    data_value = random.randint(42, 1997)
    data = {"key": data_value}  # Generar un número al azar entre 42 y 1997
    response = requests.post(url, json=data)
    print(f"POST Response: {response.status_code}, Message: {response.json()['message']}")

if __name__ == "__main__":
    ip_address = input("Ingrese la IP: ")

    try:
        while True:
            # Hacer una llamada GET cada 5 segundos
            send_get_request(ip_address)
            time.sleep(5)

            # Hacer una llamada POST cada minuto (60 segundos)
            send_post_request(ip_address)
            time.sleep(55)  # Ya hemos esperado 5 segundos después de la llamada GET

    except KeyboardInterrupt:
        print("Terminando el script...")
