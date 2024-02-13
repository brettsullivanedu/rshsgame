import pygame
import time
from dungeon import Dungeon
from utils import Button

class State:
    def handle_input(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

class IntroState(State):
    def __init__(self):
        self.start_time = time.time()

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE):
            return MainMenuState()

    def update(self):
        if time.time() - self.start_time > 3:  # 3 seconds have passed
            return MainMenuState()

class MainMenuState(State):
    def __init__(self):
        self.buttons = [
            Button("New Game", 100, 200, 200, 50, (0, 200, 0), (0, 255, 0)),
            Button("Options", 100, 300, 200, 50, (0, 200, 0), (0, 255, 0)),
            Button("Quit", 100, 400, 200, 50, (0, 200, 0), (0, 255, 0))
        ]

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                return NewGameState()
            elif event.key == pygame.K_2:
                return OptionsState()
            elif event.key == pygame.K_3:
                return QuitState()
            
    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen, pygame.mouse.get_pos())

class NewGameState(State):
    def __init__(self):
        self.dungeon = Dungeon(5)
        self.player_position = (0, 0)

    def handle_input(self, event):
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
        # Clear the screen
        screen.fill((0, 0, 0))

        # Get the current room
        current_room = self.dungeon.rooms[self.player_position[0]][self.player_position[1]]

        # Draw the room
        screen.blit(current_room.image, (0, 0))

        # Draw the room description
        font = pygame.font.Font(None, 36)
        text = font.render(current_room.description, True, (255, 255, 255))
        screen.blit(text, (100, 100))

        # Draw the room event
        text = font.render('Event: ' + current_room.event, True, (255, 255, 255))
        screen.blit(text, (100, 200))

        # Update the display
        pygame.display.flip()


class OptionsState(State):
    pass

class QuitState(State):
    def update(self):
        pygame.quit()
        quit()
