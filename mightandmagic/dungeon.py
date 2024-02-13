import random
from room import Room

class Dungeon:
    """
    The Dungeon class represents the entire dungeon.
    Each dungeon is a square grid of rooms, with the size provided upon initialization.
    """
    def __init__(self, size):
        """
        Initialize a new Dungeon instance.

        Args:
            size (int): The width and height of the dungeon in rooms.
        """
        self.size = size
        self.rooms = [[None for _ in range(size)] for _ in range(size)]
        self.generate_rooms()

    def generate_rooms(self):
        """
        Generate the rooms in the dungeon.
        Each room is assigned a description, an event, and directions to adjacent rooms.
        The bottom right room is always set as the 'exit'.
        """
        for i in range(self.size):
            for j in range(self.size):
                description = 'This is a room.'
                event = self.select_event(i, j)
                directions = self.generate_directions(i, j)
                self.rooms[i][j] = Room(description, event, directions)
        # Make the bottom right room an 'exit'
        self.rooms[-1][-1].event = 'exit'

    def select_event(self, i, j):
        """
        Select an event for a room based on its position in the dungeon.

        Args:
            i (int): The row index of the room in the dungeon.
            j (int): The column index of the room in the dungeon.

        Returns:
            str: The event for the room. If the room is at the bottom right of the dungeon, the event is 'exit'.
                 Otherwise, the event is randomly chosen from 'trap', 'encounter', 'treasure', 'empty', and 'npc'.
        """
        if i == j == self.size - 1:
            return 'exit'
        else:
            return random.choice(['trap', 'encounter', 'treasure', 'empty', 'npc'])

    def generate_directions(self, i, j):
        """
        Generate the directions from a room to its adjacent rooms.

        Args:
            i (int): The row index of the room in the dungeon.
            j (int): The column index of the room in the dungeon.

        Returns:
            dict: A dictionary where the keys are the directions ('north', 'south', 'west', 'east') and the values are
                  the coordinates (row, column) of the adjacent room in that direction. If there is no room in a
                  direction, that direction is not included in the dictionary.
        """
        directions = {}
        if i > 0: directions['north'] = (i-1, j)
        if i < self.size - 1: directions['south'] = (i+1, j)
        if j > 0: directions['west'] = (i, j-1)
        if j < self.size - 1: directions['east'] = (i, j+1)
        return directions

    def print_dungeon(self):
        """
        Print the layout of the dungeon in the command line.
        Each room is represented by the first letter of its event, in uppercase.
        """
        for i in range(self.size):
            for j in range(self.size):
                print(self.rooms[i][j].event[0].upper(), end=' ')
            print()
