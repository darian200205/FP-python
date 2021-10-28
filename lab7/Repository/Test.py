import json

dictionary = {
    "Darian": "Smecher",
    "Emilia": 1,
    "Bejan": "nebunu"
}

ans = {}


def dump_json():
    file = open("test.json", 'w')
    json.dump(dictionary, file)
    file.close()


def load_json():
    file = open("test.json", 'r')
    ans = json.loads(file)
    print(ans["Darian"])
    file.close()

