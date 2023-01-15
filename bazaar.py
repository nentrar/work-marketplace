import json
from mtgsdk import Card


class Bazaar:
    def __init__(self):
        with open('items.json') as self.items:
            self.data = json.load(self.items)

    def read_all_data(self):
        return self.data

    def add_new_item(self, category, card_name, set_name, price):
        current_count = len(self.data) + 1
        new_item = {
            f"{current_count}": {
                "Cat": category,
                "Card": card_name,
                "Image": self.get_card_image(card_name, set_name),
                "Price": price
            }
        }
        current_data = self.data
        current_data.update(new_item)
        with open('items.json', 'w') as self.items:
            json.dump(current_data, self.items)

    @staticmethod
    def get_card_image(card_name, set_name):
        card_data = Card.where(name=card_name).where(set_name=set_name).all()
        return card_data[0].image_url

    def delete_item(self, item_id):
        current_data = self.data
        del current_data[item_id]
        with open('items.json', 'w') as self.items:
            json.dump(current_data, self.items)
