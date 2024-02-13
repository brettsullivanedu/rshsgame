# The Item class is an abstract representation of an item in the game.
class Item:
    # The constructor initializes the item's attributes.
    def __init__(self, name, description, item_type):
        self.name = name  # Encapsulation: The item's name is private to the item.
        self.description = description  # Encapsulation: The item's description is private to the item.
        self.type = item_type  # Encapsulation: The item's type is private to the item.

# The Weapon class is a specific type of item that adds damage to player's attacks.
class Weapon(Item):
    # The constructor initializes the weapon's attributes.
    def __init__(self, name, description, damage):
        super().__init__(name, description, 'weapon')
        self.damage = damage  # Encapsulation: The weapon's damage is private to the weapon.

# The Consumable class is a specific type of item that has an effect when used.
class Consumable(Item):
    # The constructor initializes the consumable's attributes.
    def __init__(self, name, description, effect):
        super().__init__(name, description, 'consumable')
        self.effect = effect  # Encapsulation: The consumable's effect is private to the consumable.

# The Gold class is a specific type of item used for transactions.
class Gold(Item):
    # The constructor initializes the gold's attributes.
    def __init__(self, amount):
        super().__init__('Gold', f'{amount} gold coins', 'gold')
        self.amount = amount  # Encapsulation: The gold's amount is private to the gold.

# The Inventory class holds player's items.
class Inventory:
    # The constructor initializes the inventory's attributes.
    def __init__(self):
        self.items = {}  # Encapsulation: The inventory's items are private to the inventory.

    # This method allows to add an item to the inventory.
    def add_item(self, item):
        if item.name in self.items:
            self.items[item.name] += 1
        else:
            self.items[item.name] = 1

    # This method allows to remove an item from the inventory.
    def remove_item(self, item):
        if item.name in self.items:
            self.items[item.name] -= 1
            if self.items[item.name] == 0:
                del self.items[item.name]

    # This method checks if an item is in the inventory.
    def has_item(self, item):
        return item.name in self.items

    # This method allows to use an item, applying its effect or equipping it.
    def use_item(self, item, player):
        if self.has_item(item):
            if item.type == 'consumable':
                item.effect(player)
                self.remove_item(item)
            elif item.type == 'weapon':
                player.equip_weapon(item)

    # This method gets a list of all items in the inventory.
    def get_all_items(self):
        return self.items
