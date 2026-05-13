import requests

URL = "http://ip-api.com/json/"

try:
    print("Consultando API de geolocalización...\n")

    response = requests.get(URL, timeout=5)

    # Manejo errores HTTP
    if response.status_code == 404:
        print("ERROR 404: Recurso no encontrado")
        exit(1)

    elif response.status_code == 500:
        print("ERROR 500: Error interno servidor")
        exit(1)

    response.raise_for_status()

    data = response.json()

    # Mostrar respuesta completa
    print("Respuesta API:")
    print(data)

    # Validar respuesta
    if data.get("status") != "success":
        print("ERROR: API respondió incorrectamente")
        exit(1)

    print("\n=== GEOLOCALIZACIÓN DETECTADA ===\n")

    print(f"IP: {data.get('query')}")
    print(f"País: {data.get('country')}")
    print(f"Ciudad: {data.get('city')}")
    print(f"Región: {data.get('regionName')}")
    print(f"Latitud: {data.get('lat')}")
    print(f"Longitud: {data.get('lon')}")
    print(f"ISP: {data.get('isp')}")
    print(f"Zona Horaria: {data.get('timezone')}")

# Timeout
except requests.exceptions.Timeout:
    print("ERROR: Tiempo de espera agotado")

# Conexión
except requests.exceptions.ConnectionError:
    print("ERROR: Problema de conexión")

# HTTP
except requests.exceptions.HTTPError as e:
    print(f"ERROR HTTP: {e}")

# General requests
except requests.exceptions.RequestException as e:
    print(f"ERROR REQUEST: {e}")

# Error inesperado
except Exception as e:
    print(f"ERROR GENERAL: {e}")