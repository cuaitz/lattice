from dataclasses import dataclass

import pygame

from .game_state import GameState

@dataclass
class EngineConfig:
    width: int
    height: int
    title: str | None = None
    icon_path: str | None = None
    target_fps: int = 60

class Engine:
    def __init__(self, config: EngineConfig):
        self.config: EngineConfig = config
        self.stack: list[GameState] = []

    def push(self, state: GameState) -> None:
        """
        Pushes a new GameState into the stack.

        Args:
            state (GameState): The GameState object being pushed.
        """
        
        self.stack.append(state)
        state.on_start()
    
    def pop(self) -> None:
        """Pops the current GameState from the stack."""
        
        if self.stack:
            self.stack[-1].on_stop()
            self.stack.pop()
    
    def peek(self) -> GameState | None:
        """
        Returns the top GameState from the stack, if any.

        Returns:
            GameState | None: Current GameState object or None if the stack is empty.
        """
        
        if self.stack:
            return self.stack[-1]
        else:
            return None
    
    def pop_and_push(self, state: GameState) -> None:
        """
        Pops the current GameState and pushes a new one.

        Args:
            state (GameState): The GameState object being pushed.
        """
        
        self.pop()
        self.push(state)
    
    def clear_and_push(self, state: GameState) -> None:
        """
        Clears the stack of GameStates and pushes a new one.

        Args:
            state (GameState): The GameState object being pushed.
        """
        
        self.clear()
        self.push(state)
    
    def clear(self) -> None:
        """Clears the stack by popping all GameStates."""
        
        while self.stack:
            self.pop()
    
    def initialize(self) -> None:
        """Initializes pygame."""
        pygame.init()
        
        pygame.display.set_mode((self.config.width, self.config.height))
        
        if self.config.title is not None:
            pygame.display.set_caption(self.config.title)
        
        if self.config.icon_path is not None:
            pygame.display.set_icon(pygame.image.load(self.config.icon_path))
    
    def run(self) -> None:
        """Runs the game."""
        
        if not pygame.display.get_init():
            self.initialize()
        
        display = pygame.display.get_surface()
        
        clock = pygame.time.Clock()
        
        while self.stack:
            state = self.stack[-1]
            
            # Input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.clear()
                elif event.type == pygame.WINDOWRESIZED:
                    self.config.width = event.w
                    self.config.height = event.h
                    display = pygame.display.set_mode((self.config.width, self.config.height))
                else:
                    state.process_event(event)
            
            # Processing
            delta_time = clock.tick(self.config.target_fps) / 1000
            state.update(delta_time)
            
            # Rendering
            display.fill("#000000")
            state.render(display)
            
            pygame.display.update()
        
        pygame.quit()
