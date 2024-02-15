import pygame
import time
from constants import (
    CHARACTER_SELECT_BG,
    MAIN_MENU_BG,
    NEW_GAME_BUTTON_IMAGE_PATH,
    OPTIONS_BUTTON_IMAGE_PATH,
    QUIT_BUTTON_IMAGE_PATH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from dungeon import Dungeon
from player import Rogue, Warrior, Wizard
from utils import BottomUI, Button, image_loader


class State:
    """
    Abstract base class for all game states.
    """

    def __init__(self, screen=None):
        """
        Initializes the screen.
        """
        self.screen = screen

    def handle_input(self, event):
        """
        Method to handle user input. To be implemented in subclasses.
        """
        pass

    def update(self):
        """
        Method to update the game state. To be implemented in subclasses.
        """
        pass

    def draw(self, screen):
        """
        Method to draw the game state to the screen. To be implemented in subclasses.
        """
        pass


class IntroState(State):
    """
    Represents the introductory state of the game.
    """

    def __init__(self, screen):
        """
        Initializes the start time of the intro state.
        """
        super().__init__(screen)
        self.start_time = time.time()

    def handle_input(self, event):
        """
        Handles user input in the intro state. If the user presses return or escape, transition to the main menu state.
        """
        if event.type == pygame.KEYDOWN and (
            event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE
        ):
            return MainMenuState()

    def update(self):
        """
        Updates the intro state. If 3 seconds have passed, transition to the main menu state.
        """
        if time.time() - self.start_time > 3:  # 3 seconds have passed
            return MainMenuState(self.screen)


class MainMenuState(State):
    """
    Represents the main menu state of the game.
    """

    def __init__(self, screen):
        """
        Initializes the buttons and background image in the main menu state.
        """
        super().__init__(screen)
        self.background_image = image_loader(MAIN_MENU_BG, with_alpha=False, scale=True)
        self.buttons = [
            Button(
                NEW_GAME_BUTTON_IMAGE_PATH, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100
            ),
            Button(OPTIONS_BUTTON_IMAGE_PATH, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
            Button(QUIT_BUTTON_IMAGE_PATH, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100),
        ]

        # Load images for all buttons
        for button in self.buttons:
            button.load_image()

    def handle_input(self, event):
        """
        Handles user input in the main menu state. Depending on the button clicked, transition to the appropriate state.
        """
        for button in self.buttons:
            if button.is_clicked(event):
                if button.image_path == NEW_GAME_BUTTON_IMAGE_PATH:
                    return CharacterSelectState(self.screen)
                elif button.image_path == OPTIONS_BUTTON_IMAGE_PATH:
                    return OptionsState()
                elif button.image_path == QUIT_BUTTON_IMAGE_PATH:
                    return QuitState()

    def draw(self, screen):
        """
        Draws the main menu state to the screen.
        """
        # Draw the background image
        screen.blit(self.background_image, (0, 0))

        # Draw the buttons
        for button in self.buttons:
            button.draw(screen)


class CharacterSelectState(State):
    """
    Represents the character selection state of the game.
    """

    def __init__(self, screen):
        """
        Initializes the background image and buttons in the character selection state.
        """
        super().__init__(screen)
        self.background_image = image_loader(
            CHARACTER_SELECT_BG, with_alpha=False, scale=True
        )
        self.buttons = [
            Button(NEW_GAME_BUTTON_IMAGE_PATH, SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2),
            Button(OPTIONS_BUTTON_IMAGE_PATH, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
            Button(QUIT_BUTTON_IMAGE_PATH, SCREEN_WIDTH * 3 / 4, SCREEN_HEIGHT / 2),
        ]
        self.selected_player = None  # Attribute to store the selected player character

        # Load images for all buttons
        for button in self.buttons:
            button.load_image()

    def handle_input(self, event):
        """
        Handles user input in the character selection state. Depending on the button clicked, transition to the new game state.
        """
        for button in self.buttons:
            if button.is_clicked(event):

                # Create a Player object based on the selected character
                if button.image_path == NEW_GAME_BUTTON_IMAGE_PATH:
                    self.selected_player = Rogue("Rogue")  # Create a Rogue player
                elif button.image_path == OPTIONS_BUTTON_IMAGE_PATH:
                    self.selected_player = Wizard("Wizard")  # Create a Wizard player
                elif button.image_path == QUIT_BUTTON_IMAGE_PATH:
                    self.selected_player = Warrior("Warrior")  # Create a Warrior player
                return NewGameState(self.screen, self.selected_player)


    def draw(self, screen):
        """
        Draws the character selection state to the screen.
        """
        # Draw the background image
        screen.blit(self.background_image, (0, 0))

        # Draw the buttons
        for button in self.buttons:
            button.draw(screen)


class NewGameState(State):
    """
    Represents the new game state of the game.
    """
    def __init__(self, screen, character):
        """
        Initializes the dungeon, player position, and bottom UI in the new game state.
        """
        super().__init__(screen)
        self.dungeon = Dungeon(6)
        self.player_position = (0, 0)
        self.character = character
        self.bottom_ui = BottomUI(screen)  # Pass the screen to the BottomUI constructor
        self.update_bottom_ui()  # Update the bottom UI initially

    def update_bottom_ui(self):
        """
        Updates the bottom UI based on the current room's information.
        """
        current_room = self.dungeon.rooms[self.player_position[0]][self.player_position[1]]
        self.bottom_ui.set_room_description(current_room.description)
        self.bottom_ui.set_button_texts(["North", "South", "West", "East"])  # Example directional buttons

    def handle_input(self, event):
        """
        Handles user input in the new game state. Depending on the key pressed, move the player in the appropriate direction.
        """
        if event.type == pygame.KEYDOWN:
            direction = None
            if event.key == pygame.K_w:
                direction = 'north'
            elif event.key == pygame.K_s:
                direction = 'south'
            elif event.key == pygame.K_a:
                direction = 'west'
            elif event.key == pygame.K_d:
                direction = 'east'
            if direction:
                current_room = self.dungeon.rooms[self.player_position[0]][self.player_position[1]]
                if direction in current_room.directions:
                    next_position = current_room.directions[direction]
                    if 0 <= next_position[0] < self.dungeon.size and 0 <= next_position[1] < self.dungeon.size:
                        self.player_position = next_position
                    else:
                        print('You cannot go in that direction.')
                else:
                    print('Invalid direction.')
            print(self.dungeon.print_dungeon())

    def draw(self, screen):
        """
        Draws the new game state to the screen.
        """
        # Clear the screen
        screen.fill((0, 0, 0))

        # Get the current room
        current_room = self.dungeon.rooms[self.player_position[0]][self.player_position[1]]

        # Draw the room
        current_room.display(screen)

        # Update the bottom UI
        self.update_bottom_ui()

        # Draw bottom UI
        self.bottom_ui.draw()

        # Update the display
        pygame.display.flip()


class OptionsState(State):
    """
    Represents the options state of the game. To be implemented.
    """

    pass


class QuitState(State):
    """
    Represents the quit state of the game.
    """

    def update(self):
        """
        Quits the game when this state is updated.
        """
        pygame.quit()
        quit()
