import pygame
from pygame.image import load

import os
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def image_loader(name, folder="backgrounds", with_alpha=True, scale=True):
    """
    Function to load an image.
    The image file is located based on the provided name and folder, loaded, resized if required, and then converted based on whether it should have alpha (transparency).
    """
    try:
        # Construct the file path to the image
        path = os.path.join("assets", folder, name)  

        # Load the image from the file
        loaded_image = pygame.image.load(path)  

        # Apply scaling for backgrounds only
        if scale:
            loaded_image = pygame.transform.scale(loaded_image, (800, 800))  

        # Convert the image based on whether it should have alpha (transparency)
        if with_alpha:
            return loaded_image.convert_alpha()
        else:
            return loaded_image.convert()
    except pygame.error as e:
        print(f"Error loading image: {e}")
        return None
class Button:
    """
    Represents a clickable button in the game.
    """
    def __init__(self, image_path, x, y, width, height, text):
        """
        Initializes the button with an image, a position, width, height, and text.
        """
        self.image_path = image_path  # Store the image path
        self.rect = pygame.Rect(x, y, width, height)  # Create a rectangle with custom width and height
        self.text = text  # Text to be displayed on the button
        self.load_image()

    def load_image(self):
        """
        Loads the button's background image.
        """
        self.image = image_loader(self.image_path, folder="backgrounds", with_alpha=True, scale=True)  # Load the image
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))  # Scale image to match custom size
        # Make white color transparent
        self.image.set_colorkey((255, 255, 255))
    def draw(self, screen):
        """
        Draws the button to the screen.
        """
        screen.blit(self.image, self.rect)  # Draw the image to the screen at the position of the rectangle
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, (50, 50, 50))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        """
        Checks if the button is clicked.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:  # If there is a mouse button down event
            if self.rect.collidepoint(event.pos):  # If the position of the mouse event is within the rectangle of the button
                return True
        return False

class BottomUI:
    def __init__(self, screen):
        """
        Initializes the bottom UI.
        """
        self.screen = screen
        self.room_description = ""
        self.buttons = []
        self.paper_image = image_loader("paper.jpg", folder="backgrounds", with_alpha=True, scale=False)

    def set_room_description(self, description):
        self.room_description = description

    def set_buttons(self):
        """
        Sets up the buttons for North, South, East, and West directions.
        """
        self.buttons = [
            Button("buttonbg.jpg", 50, SCREEN_HEIGHT - 100, 100, 50, "North"),
            Button("buttonbg.jpg", 210, SCREEN_HEIGHT - 100, 100, 50, "South"),
            Button("buttonbg.jpg", 370, SCREEN_HEIGHT - 100, 100, 50, "East"),
            Button("buttonbg.jpg", 530, SCREEN_HEIGHT - 100, 100, 50, "West")
        ]

    def draw(self):
        """
        Draws the bottom UI to the screen.
        """
        # Draw the paper image
        self.screen.blit(pygame.transform.scale(self.paper_image, (SCREEN_WIDTH, SCREEN_HEIGHT // 3)), (0, SCREEN_HEIGHT - (SCREEN_HEIGHT // 3)))

        # Draw the room description
        font = pygame.font.Font(None, 36)
        text = font.render(self.room_description, True, (0, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - (SCREEN_HEIGHT // 6)))
        self.screen.blit(text, text_rect)

        # Draw the buttons
        for button in self.buttons:
            button.draw(self.screen)
