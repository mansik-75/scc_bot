import json


def parse_json(user_from: str, result):
    data = json.load(open(result, 'r'))
    answer = []
    for message in data['messages']:
        if message['type'] == 'message' and message['from_id'] == user_from and message['text'] and type(message['text']) == str:
            answer.append(message['text'])

    return answer


if __name__ == "__main__":
    user = 'user113627063'
    # file = 'bicyclesausages_result.json'
    file = 'scc_result.json'
    ans = parse_json(user, file)
    print(ans)

    total_msg = {i: ans[i] for i in range(len(ans))}

    json.dump(total_msg, open(f"./messages/msg_{file.split('.')[0]}.json", 'w', encoding='utf8'))
