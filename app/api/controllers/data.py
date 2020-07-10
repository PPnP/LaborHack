from flask.views import MethodView
import json


class DataController(MethodView):
    def get(self, type):
        with open('data/' + type + '.json', 'r', encoding='utf-8') as input:
            data = json.load(input)
        data = json.dumps(data)
        return data
