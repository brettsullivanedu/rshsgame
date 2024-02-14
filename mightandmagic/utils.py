# Import the load function from pygame's image module
from pygame.image import load
import pygame

# Define a function to load a sprite
def image_loader(name, with_alpha=True):
    # Construct the file path to the sprite
    path = f"assets/{name}"
    # Load the sprite from the file
    loaded_sprite = load(path)

     # Resize the sprite to 800x800 pixels
    loaded_sprite = pygame.transform.scale(loaded_sprite, (800, 800))

    # If the sprite should be loaded with alpha (transparency), convert it accordingly
    if with_alpha:
        return loaded_sprite.convert_alpha()
    # Otherwise, convert the sprite without alpha
    else:
        return loaded_sprite.convert()

class Button:
    def __init__(self, text, x, y, width, height, inactive_color, active_color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color

    def draw(self, screen, mouse_pos):
        if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
            pygame.draw.rect(screen, self.active_color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.inactive_color, (self.x, self.y, self.width, self.height))

        font = pygame.font.Font(None, 50)
        text = font.render(self.text, True, (0, 0, 0))
        screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
