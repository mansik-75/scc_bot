import io
import json
import math
import os
import random

import boto3
from dotenv import load_dotenv
from matplotlib import pyplot as plt


load_dotenv()


boto_session = boto3.session.Session(
    aws_access_key_id=os.environ.get('KEY_ID'),
    aws_secret_access_key=os.environ.get('SECRET')
)
s3 = boto_session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net',
    region_name='ru-central1',
)
s3_bucket = os.environ.get('S3_BUCKET')

messages = [msg['Key'] for msg in s3.list_objects(Bucket=s3_bucket)['Contents']]
file = messages[random.randint(0, len(messages) - 1)]
print(f"File: {file}")
parsed = json.loads(s3.get_object(Bucket=s3_bucket, Key=file)['Body'].read())


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
    return parsed[str(random.randint(0, len(parsed.keys()) - 1))]


if __name__ == '__main__':
    quote = get_quote()
    print(quote)
