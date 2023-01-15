import json


class Marketplace:
    def __init__(self):
        with open('items.json') as items:
            self.data = json.load(items)

    def read_all_data(self):
        return self.data
