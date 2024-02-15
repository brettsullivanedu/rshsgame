import pygame
import random
from constants import ROOM_IMAGES
from utils import image_loader

class Room:
    """
    The Room class represents a room in the dungeon.
    """
    def __init__(self, description, event, directions):
        """
        Constructor for the Room class.
        Initializes the room's description, event, directions, and image.
        """
        self.description = description  # The room's description
        self.event = event  # The room's event
        self.directions = directions  # The room's directions
        self.image = self.bg_loader()  # The room's image

    def bg_loader(self):
        """
        Loads an image of the room based on its event.
        """
        return image_loader(random.choice(ROOM_IMAGES[self.event]), with_alpha=False)

    def display(self, screen):
        """
        Displays the room on the screen.
        Draws the room image and room description.
        """
        self.draw_room_image(screen)
        self.draw_room_description(screen)

    def draw_room_image(self, screen):
        """
        Draws the room image on the screen.
        """
        screen.blit(pygame.transform.scale(self.image, (800, 600)), (0, 0))

    def draw_room_description(self, screen):
        """
        Draws the room description on a piece of paper and displays it on the screen.
        """
        font = pygame.font.Font(None, 36)  # Font for the room description
        paper = pygame.image.load("assets/backgrounds/empty4.jpg")  # Image of the paper
        text = font.render(self.description, True, (0, 0, 0))  # Rendered text of the room description
        paper.blit(text, (50, 50))  # Blit the text onto the paper
        screen.blit(pygame.transform.scale(paper, (300, 200)), (250, 200))  # Scale the paper and blit it onto the screen
