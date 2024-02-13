import pygame
from states import IntroState, MainMenuState
from utils import image_loader

class MightAndMagic:
    def __init__(self):
        # Initialize pygame and create a display surface
        self._init_pygame()
        self.screen = pygame.display.set_mode((800,800))
        self.background = image_loader("backgrounds/title.jpg", False)
        self.state = IntroState()

    def main_loop(self):
        # Main game loop which will run indefinitely
        while True:
            # Handle user input
            self._handle_input()
            # Process game logic
            self._process_game_logic()
            # Draw the current state of the game to the screen
            self._draw()

    def _init_pygame(self):
        # Initialize all imported pygame modules
        pygame.init()
        # Set the caption for the window
        pygame.display.set_caption("Might and Magic v0.1")

    def _handle_input(self):
        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            # Update the current state based on user input
            new_state = self.state.handle_input(event)
            if new_state is not None:
                self.state = new_state

    def _process_game_logic(self):
        # Process game logic
        new_state = self.state.update()
        if new_state is not None:
            self.state = new_state

    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        # Draw the current state to the screen
        self.state.draw(self.screen)
        # Update the full display surface to the screen
        pygame.display.flip()

if __name__ == "__main__":
    game = MightAndMagic()
    game.main_loop()
