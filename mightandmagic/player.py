from inventory import Gold, Inventory

class Player:
    """
    The Player class is an abstract representation of a player in the game.
    """
    def __init__(self, name, health, defense, dodge):
        """
        Constructor for the Player class.
        Initializes the player's attributes.
        """
        self.name = name  # The player's name
        self.health = health  # The player's health
        self.defense = defense  # The player's defense
        self.dodge = dodge  # The player's dodge
        self.inventory = Inventory()  # The player's inventory
        self.level = 1  # The player's level
        self.exp = 0  # The player's experience
        self.weapon = None  # The player's weapon

    def take_damage(self, damage):
        """
        Allows the player to take damage.
        If the player doesn't dodge the attack, they take damage.
        """
        if not self.dodge_attack():
            self.health -= max(0, damage - self.defense)
            return True
        return False

    def dodge_attack(self):
        """
        Allows the player to dodge an attack.
        To be implemented in subclasses.
        """
        pass

    def level_up(self):
        """
        Allows the player to level up.
        To be implemented in subclasses.
        """
        pass

    def use_item(self, item):
        """
        Allows the player to use an item from their inventory.
        """
        self.inventory.use_item(item, self)

    def equip_weapon(self, weapon):
        """
        Allows the player to equip a weapon from their inventory.
        """
        if self.inventory.has_item(weapon) and weapon.type == 'weapon':
            self.weapon = weapon

    def transact(self, npc, amount):
        """
        Allows the player to transact with an NPC using gold.
        """
        gold = Gold(amount)
        if self.inventory.has_item(gold):
            npc.receive_payment(gold)
            self.inventory.remove_item(gold)

class Rogue(Player):
    """
    The Rogue class is a specific type of player with unique attributes.
    """
    def __init__(self, name):
        """
        Constructor for the Rogue class.
        Initializes the rogue's attributes.
        """
        super().__init__(name, health=100, defense=10, dodge=20)
        self.stealth = 10  # The rogue's stealth

class Wizard(Player):
    """
    The Wizard class is a specific type of player with unique attributes.
    """
    def __init__(self, name):
        """
        Constructor for the Wizard class.
        Initializes the wizard's attributes.
        """
        super().__init__(name, health=80, defense=10, dodge=10)
        self.magic = 10  # The wizard's magic

class Warrior(Player):
    """
    The Warrior class is a specific type of player with unique attributes.
    """
    def __init__(self, name):
        """
        Constructor for the Warrior class.
        Initializes the warrior's attributes.
        """
        super().__init__(name, health=120, defense=20, dodge=5)
        self.strength = 10  # The warrior's strength
