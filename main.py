import pygame
from cell import Cell
from board import Board
import pygame.color 
import functions


###GAME LIFE WITH PYGAME###
# Press "p" to start and pause the game
# Press "r" to restart the game
# Use the mouse to revive the cells 

def start():
    pygame.init()
    
    screen = pygame.display.set_mode((600,800))
    pygame.display.set_caption("Game of life")
    
    celula = Cell(0,0)
    
    #Calculate the rows and cols
    rows = int(screen.get_width()/(celula.rect.width + 2))
    cols = int(screen.get_height()/(celula.rect.height + 2))
    
    board: Board = Board(cols, rows)
    
    clock = pygame.time.Clock()
    while True:
        
        functions.check_events(board)
        screen.fill((0,0,0))
       #If the game is active(press "p" to active) and the mouse is not being pressed, the game run 
        if board.game_active and not board.mouse_pressed:
            board.set_number_of_neighbors()
            board.update_lifes()
            clock.tick(30)
            
        board.draw(screen)
        pygame.display.flip()
        
start()