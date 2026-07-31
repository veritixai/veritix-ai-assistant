import os
import requests


def download_image(url, filename):

    os.makedirs("images", exist_ok=True)

    response = requests.get(url)

    if response.status_code == 200:

        path = os.path.join("images", filename)

        with open(path, "wb") as f:
            f.write(response.content)

        return path

    return None