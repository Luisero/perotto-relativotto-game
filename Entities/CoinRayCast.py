from math import sqrt
class CoinRayCast:
    COLOR = (0,255,0)
    line_size = 0

    def __init__(self,x1, y1, x2,y2) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def get_line_size(self):
        return self.line_size

    def draw(self, screen, pygame):
        self.line_size = sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        pygame.draw.line(screen, self.COLOR, (self.x1, self.y1), (self.x2, self.y2), 2)