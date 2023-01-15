import json


class Bazaar:
    def __init__(self):
        with open('items.json') as self.items:
            self.data = json.load(self.items)

    def read_all_data(self):
        return self.data

    def add_new_item(self, category, topic, img, price):
        current_count = len(self.data) + 1
        new_item = {
            f"{current_count}": {
                "Cat": category,
                "Card": topic,
                "Image": img,
                "Price": price
            }
        }
        current_data = self.data
        current_data.update(new_item)
        with open('items.json', 'w') as self.items:
            json.dump(current_data, self.items)
