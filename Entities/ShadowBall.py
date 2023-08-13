from .Ball import Ball
from random import randint

class ShadowBall(Ball):
    
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)
        self.COLOR = (randint(200,255), randint(0,100), randint(0, 100))

    def draw(self, screen, pygame):
        return super().draw(screen, pygame)