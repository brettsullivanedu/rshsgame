import random
from room import Room

class Dungeon:
    # The Dungeon class represents the entire dungeon.
    def __init__(self, size):
        self.size = size
        self.rooms = [[None for _ in range(size)] for _ in range(size)]
        self.generate_rooms()

    def generate_rooms(self):
        # This method generates the rooms in the dungeon.
        for i in range(self.size):
            for j in range(self.size):
                description = 'This is a room.'
                event = self.select_event(i, j)
                directions = self.generate_directions(i, j)
                self.rooms[i][j] = Room(description, event, directions)
        # Make the bottom right room an 'exit'
        self.rooms[-1][-1].event = 'exit'

    def select_event(self, i, j):
        # This method selects an event based on the room's position.
        if i == j == self.size - 1:
            return 'exit'
        else:
            return random.choice(['trap', 'encounter', 'treasure', 'empty', 'npc'])

    def generate_directions(self, i, j):
        # This method generates the directions for each room.
        directions = {}
        if i > 0: directions['north'] = (i-1, j)
        if i < self.size - 1: directions['south'] = (i+1, j)
        if j > 0: directions['west'] = (i, j-1)
        if j < self.size - 1: directions['east'] = (i, j+1)
        return directions

    def print_dungeon(self):
        # This method prints the dungeon layout in the command line.
        for i in range(self.size):
            for j in range(self.size):
                print(self.rooms[i][j].event[0].upper(), end=' ')
            print()
