import json


class FakeResponse:
    def json(self):
        with open('../resources/data.json', 'r') as file:
            return json.loads(file.read())
