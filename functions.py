import sys
import pygame


def check_events(board):
    for event in pygame.event.get():
        #Event to exit
        if event.type == pygame.QUIT:
            sys.exit()
            
       #Mouse event to check  
        elif event.type == pygame.MOUSEBUTTONDOWN :
            mouse_button_down_event(board)
       
        
        elif event.type == pygame.MOUSEBUTTONUP:
            board.mouse_pressed = False
            
        elif board.mouse_pressed and event.type == pygame.MOUSEMOTION:
            mouse_motion_pressed_event(board)
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                board.game_active = not board.game_active
            if event.key == pygame.K_r:
                board.reset()
                board.game_active = False

def mouse_button_down_event(board):
    pos = pygame.mouse.get_pos()
        
    for array in board.table:
        for cell in array:
            if cell.rect.collidepoint(pos):
                cell.is_alive = True
                break
    board.mouse_pressed= True 


def mouse_motion_pressed_event(board):
    pos = pygame.mouse.get_pos()
    for array in board.table:
        for cell in array:
            if cell.rect.collidepoint(pos):
                cell.is_alive = True
                break
