from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from .engine import Engine

class GameState(ABC):
    def __init__(self, engine: 'Engine', game: any):
        self.engine: 'Engine' = engine
        self.game: any = game
        pass
    
    def on_start(self) -> None:
        """Optional callback called when the state is added to the stack."""
        pass
    
    @abstractmethod
    def process_event(self, event: pygame.event.Event) -> None:
        """
        Process an incoming pygame event.

        Args:
            event (pygame.event.Event): The pygame event to be processed.
        """
        pass
    
    @abstractmethod
    def update(self, delta_time: float) -> None:
        """
        A method called every frame to update this GameState.

        Args:
            delta_time (float): Time elapsed since the last frame, in seconds.
        """
        pass
    
    @abstractmethod
    def render(self, surface: pygame.Surface) -> None:
        """
        A method called every frame to draw this GameState on the given surface.

        Args:
            surface (pygame.Surface): The surface to render into.
        """
        pass
    
    def on_stop(self) -> None:
        """Optional callback called when the state is removed from the stack."""
        pass
