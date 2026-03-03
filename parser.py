import json


def parse_json(user_from: str, result):
    data = json.load(open(result, 'r'))
    answer = []
    for message in data['messages']:
        if message['type'] == 'message' and message['from_id'] == user_from and message['text'] and type(message['text']) == str:
            answer.append(message['text'])

    return answer
