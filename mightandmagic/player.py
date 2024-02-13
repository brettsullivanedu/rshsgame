# Importing necessary classes from mightandmagic.inventory module
from mightandmagic.inventory import Gold, Inventory

# The Player class is an abstract representation of a player in the game.
class Player:
    # The constructor initializes the player's attributes.
    def __init__(self, name, health, defense, dodge):
        self.name = name  # Encapsulation: The player's name is private to the player.
        self.health = health  # Encapsulation: The player's health is private to the player.
        self.defense = defense  # Encapsulation: The player's defense is private to the player.
        self.dodge = dodge  # Encapsulation: The player's dodge is private to the player.
        self.inventory = Inventory()  # Encapsulation: The player's inventory is private to the player.
        self.level = 1  # Encapsulation: The player's level is private to the player.
        self.exp = 0  # Encapsulation: The player's experience is private to the player.
        self.weapon = None  # Encapsulation: The player's weapon is private to the player.

    # This method allows the player to take damage.
    def take_damage(self, damage):
        # If the player doesn't dodge the attack, they take damage.
        if not self.dodge_attack():
            self.health -= max(0, damage - self.defense)
            return True
        return False

    # This method allows the player to dodge an attack.
    def dodge_attack(self):
        # Implement dodge logic here
        pass

    # This method allows the player to level up.
    def level_up(self):
        # Implement level up logic here
        pass

    # This method allows the player to use an item from their inventory.
    def use_item(self, item):
        # Use an item from the inventory
        self.inventory.use_item(item, self)

    # This method allows the player to equip a weapon from their inventory.
    def equip_weapon(self, weapon):
        # Equip a weapon from the inventory
        if self.inventory.has_item(weapon) and weapon.type == 'weapon':
            self.weapon = weapon

    # This method allows the player to transact with an NPC using gold.
    def transact(self, npc, amount):
        # Transact with an NPC using gold
        gold = Gold(amount)
        if self.inventory.has_item(gold):
            npc.receive_payment(gold)
            self.inventory.remove_item(gold)

# The Rogue class is a specific type of player with unique attributes.
class Rogue(Player):
    # The constructor initializes the rogue's attributes.
    def __init__(self, name):
        super().__init__(name, health=100, defense=10, dodge=20)
        self.stealth = 10  # Encapsulation: The rogue's stealth is private to the rogue.

# The Wizard class is a specific type of player with unique attributes.
class Wizard(Player):
    # The constructor initializes the wizard's attributes.
    def __init__(self, name):
        super().__init__(name, health=80, defense=10, dodge=10)
        self.magic = 10  # Encapsulation: The wizard's magic is private to the wizard.

# The Warrior class is a specific type of player with unique attributes.
class Warrior(Player):
    # The constructor initializes the warrior's attributes.
    def __init__(self, name):
        super().__init__(name, health=120, defense=20, dodge=5)
        self.strength = 10  # Encapsulation: The warrior's strength is private to the warrior.
