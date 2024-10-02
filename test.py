import requests


def buscar_imagenes_murcielagos():
    query = "murcielagos"
    url = f"https://api.unsplash.com/search/photos/?query={query}&per_page=5"
    headers = {
        "Accept-Version": "v1",
        "Authorization": "Client-ID YOUR_ACCESS_KEY"  # Reemplazar YOUR_ACCESS_KEY con tu Access Key de Unsplash
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    images = data["results"]
    for image in images:
        print(image["urls"]["regular"])


# Mostrar imágenes de murciélagos
buscar_imagenes_murcielagos()