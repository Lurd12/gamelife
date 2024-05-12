import pygame
from pygame.sprite import Sprite

class Cell(Sprite):
    def __init__(self, x, y):
        super(Cell, self).__init__()
        self.rect = pygame.Rect(x,y, 15,15)
        
        
        self.is_alive: bool = False
        self.neighbors: int = 0
        self.color = (0,0,0)
        
        
    def draw(self, screen: pygame.Surface):
        if self.is_alive:
            self.color = (255,255,255)
        else:
            self.color = (20,20,20)
        pygame.draw.rect(screen, self.color, self.rect)
        