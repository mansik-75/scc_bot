import re


def read_gpx(file: str) -> tuple[list[float], list[float]]:
    latitude_r = re.compile(r'lat=\"(\d+\.\d+)\"')
    longitude_r = re.compile(r'lon=\"(\d+\.\d+)\"')
    lat = list()
    lon = list()
    for line in file.split('\n'):
        if "<trkpt" in line:
            lat.append(float(latitude_r.findall(line)[0]))
            lon.append(float(longitude_r.findall(line)[0]))

    return lat, lon
