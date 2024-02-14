# Import necessary modules
import pygame
from constants import INTRO_BG_IMAGE_PATH
from states import IntroState, MainMenuState
from utils import image_loader

class MightAndMagic:
    def __init__(self):
        """
        Constructor for the MightAndMagic class.
        Initializes pygame, sets up the display surface, and sets the initial game state.
        """
        self._init_pygame()
        self.screen = pygame.display.set_mode((800,800))  # Create a display surface
        self.background = image_loader(INTRO_BG_IMAGE_PATH,folder="backgrounds", with_alpha=False, scale=True)  # Load the background image
        self.state = IntroState()  # Set the initial game state

    def main_loop(self):
        """
        Main game loop which will run indefinitely.
        Handles user input, processes game logic, and draws the current state of the game to the screen.
        """
        while True:
            self._handle_input()  # Handle user input
            self._process_game_logic()  # Process game logic
            self._draw()  # Draw the current state of the game to the screen

    def _init_pygame(self):
        """
        Initialize all imported pygame modules and set the caption for the window.
        """
        pygame.init()
        pygame.display.set_caption("Might and Magic v0.1")

    def _handle_input(self):
        """
        Handle user input.
        Iterates over each event in the pygame event queue.
        If the event type is QUIT, then it exits the game.
        Otherwise, it updates the current state based on user input.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            new_state = self.state.handle_input(event)
            if new_state is not None:
                self.state = new_state

    def _process_game_logic(self):
        """
        Process game logic.
        Updates the current state based on the game's logic.
        """
        new_state = self.state.update()
        if new_state is not None:
            self.state = new_state

    def _draw(self):
        """
        Draw the current state of the game to the screen.
        Blits the background image to the screen, draws the current state, and updates the display surface.
        """
        self.screen.blit(self.background, (0, 0))
        self.state.draw(self.screen)
        pygame.display.flip()  # Update the full display surface to the screen

