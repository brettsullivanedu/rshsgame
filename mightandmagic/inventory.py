class Item:
    """
    The Item class is an abstract representation of an item in the game.
    """
    def __init__(self, name, description, item_type):
        """
        The constructor initializes the item's attributes.
        """
        self.name = name  # The item's name
        self.description = description  # The item's description
        self.type = item_type  # The item's type

class Weapon(Item):
    """
    The Weapon class is a specific type of item that adds damage to player's attacks.
    """
    def __init__(self, name, description, damage):
        """
        The constructor initializes the weapon's attributes.
        """
        super().__init__(name, description, 'weapon')
        self.damage = damage  # The weapon's damage

class Consumable(Item):
    """
    The Consumable class is a specific type of item that has an effect when used.
    """
    def __init__(self, name, description, effect):
        """
        The constructor initializes the consumable's attributes.
        """
        super().__init__(name, description, 'consumable')
        self.effect = effect  # The consumable's effect

class Gold(Item):
    """
    The Gold class is a specific type of item used for transactions.
    """
    def __init__(self, amount):
        """
        The constructor initializes the gold's attributes.
        """
        super().__init__('Gold', f'{amount} gold coins', 'gold')
        self.amount = amount  # The gold's amount

class Inventory:
    """
    The Inventory class holds player's items.
    """
    def __init__(self):
        """
        The constructor initializes the inventory's attributes.
        """
        self.items = {}  # The inventory's items

    def add_item(self, item):
        """
        This method allows to add an item to the inventory.
        """
        if item.name in self.items:
            self.items[item.name] += 1
        else:
            self.items[item.name] = 1

    def remove_item(self, item):
        """
        This method allows to remove an item from the inventory.
        """
        if item.name in self.items:
            self.items[item.name] -= 1
            if self.items[item.name] == 0:
                del self.items[item.name]

    def has_item(self, item):
        """
        This method checks if an item is in the inventory.
        """
        return item.name in self.items

    def use_item(self, item, player):
        """
        This method allows to use an item, applying its effect or equipping it.
        """
        if self.has_item(item):
            if item.type == 'consumable':
                item.effect(player)
                self.remove_item(item)
            elif item.type == 'weapon':
                player.equip_weapon(item)

    def get_all_items(self):
        """
        This method gets a list of all items in the inventory.
        """
        return self.items
