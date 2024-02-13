import pygame
import random
from utils import image_loader

class Room:
    # The Room class represents a room in the dungeon.
    def __init__(self, description, event, directions):
        self.description = description
        self.event = event
        self.directions = directions
        self.image = self.bg_loader()

    def bg_loader(self):
        # This method loads an image of the room based on its event.
        images = self.get_images()
        return image_loader(random.choice(images[self.event]), with_alpha=False)

    @staticmethod
    def get_images():
        # This method returns a dictionary of images for each event.
        return {
            "trap": [
                "backgrounds/trap1.jpg",
                "backgrounds/trap2.jpg",
                "backgrounds/trap3.jpg",
                "backgrounds/trap4.jpg",
                "backgrounds/trap5.jpg",
            ],
            "encounter": [
                "backgrounds/encounter1.jpg",
                "backgrounds/encounter2.jpg",
                "backgrounds/encounter3.jpg",
            ],
            "treasure": [
                "backgrounds/treasure1.jpg",
                "backgrounds/treasure2.jpg",
                "backgrounds/treasure3.jpg",
                "backgrounds/treasure4.jpg",
                "backgrounds/treasure5.jpg",
            ],
            "empty": [
                "backgrounds/empty1.jpg",
                "backgrounds/empty2.jpg",
                "backgrounds/empty3.jpg",
            ],
            "npc": [
                "backgrounds/npc1.jpg",
                "backgrounds/npc2.jpg",
                "backgrounds/npc3.jpg",
            ],
            "exit": ["backgrounds/exit.jpg"],
        }

    def display(self, screen):
        # This method displays the room on the screen.
        self.draw_room_image(screen)
        self.draw_room_description(screen)

    def draw_room_image(self, screen):
        # This method draws the room image.
        screen.blit(pygame.transform.scale(self.image, (800, 600)), (0, 0))

    def draw_room_description(self, screen):
        # This method draws the room description on a piece of paper.
        font = pygame.font.Font(None, 36)
        paper = pygame.image.load("assets/paper.jpg")
        text = font.render(self.description, True, (0, 0, 0))
        paper.blit(text, (50, 50))
        screen.blit(pygame.transform.scale(paper, (300, 200)), (250, 200))
