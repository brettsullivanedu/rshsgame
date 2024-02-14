import pygame
from pygame.image import load

import os
import pygame

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