import pygame
from lattice import *

class TestState(GameState):
    def __init__(self, engine: Engine, game: any):
        super().__init__(engine, game)
    
    def process_event(self, event: pygame.event.Event) -> None:
        return super().process_event(event)
    
    def update(self, delta_time: float) -> None:
        return super().update(delta_time)
    
    def render(self, surface: pygame.Surface) -> None:
        return super().render(surface)

engine = Engine(
    EngineConfig(800, 600, 'Teste', None, 60)
)
game_logic = GameLogic()

engine.push(TestState(engine, game_logic))
engine.run()
