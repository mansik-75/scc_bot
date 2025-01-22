import io
import math

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
