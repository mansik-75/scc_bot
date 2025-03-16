import io
import json
import math
import os
import random

from matplotlib import pyplot as plt


def to_decart(latitude: list[float], longitude: list[float], zoom: float, mid: int) -> tuple[list[float], list[float]]:
    decart_latitude, decart_longitude = list(), list()
    for lat in latitude:
        decart_latitude.append(math.radians(lat) * zoom * math.log(math.tan(math.pi / 4 + math.radians(lat) / 2), math.e))
    for lon in longitude:
        decart_longitude.append(math.radians(lon) * zoom + mid)

    return decart_latitude, decart_longitude


def save_file(latitude: list[float], longitude: list[float]):
    y, x = to_decart(latitude, longitude, 0.3, 10)

    plt.plot(x, y, color='black', linewidth=3)
    plt.axis('off')
    plt.axis('equal')

    file = io.BytesIO()

    plt.savefig(file, format='png')
    file.seek(0)

    return file

def get_quote():
    msg_path = os.path.join(os.getcwd(), 'messages')
    messages = os.listdir(msg_path)
    file = messages[random.randint(0, len(messages) - 1)]
    parsed = json.load(open(os.path.join(msg_path, file), 'r'))

    quote = parsed[str(random.randint(0, len(parsed.keys()) - 1))]
    print(quote)

    return quote


if __name__ == '__main__':
    quote = get_quote()
    print(quote)
