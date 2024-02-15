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
    def __init__(self, image_path, x, y):
        """
        Initializes the button with an image and a position.
        """
        self.image_path = image_path  # Store the image path
        self.rect = pygame.Rect(x, y, 0, 0)  # Create an empty rectangle initially

    def load_image(self):
        """
        Loads the button's image.
        """
        self.image = image_loader(self.image_path, folder="sprites", with_alpha=False, scale=False)  # Load the image
        self.rect = self.image.get_rect(center=self.rect.center)  # Update the rectangle with the image size and position

    def draw(self, screen):
        """
        Draws the button to the screen.
        """
        screen.blit(self.image, self.rect)  # Draw the image to the screen at the position of the rectangle

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
        self.button_texts = []
        self.paper_image = pygame.image.load("assets/backgrounds/empty4.jpg")

    def set_room_description(self, description):
        self.room_description = description

    def set_button_texts(self, texts):
        self.button_texts = texts

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
        button_y = SCREEN_HEIGHT - 100
        button_x = 100
        button_width = 150
        button_height = 50
        for button_text in self.button_texts:
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            pygame.draw.rect(self.screen, (255, 0, 0), button_rect)
            button_font = pygame.font.Font(None, 24)
            button_text_surface = button_font.render(button_text, True, (255, 255, 255))
            self.screen.blit(button_text_surface, (button_x + 10, button_y + 10))
            button_x += button_width + 10
