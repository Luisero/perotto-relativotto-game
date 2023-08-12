class Coin:
    COLOR = (255, 255, 0)

    def __init__(self, x, y, radius) -> None:
        self.x = x
        self.y = y
        self.radius = radius 
    
    def draw(self, screen, pygame):
        pygame.draw.circle(screen, self.COLOR, (self.x, self.y), self.radius)