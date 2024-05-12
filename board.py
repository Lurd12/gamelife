from cell import Cell

class Board():
    def __init__(self, cols: int, rows: int):
        self.table: list = []

        cell = Cell(0,0)

        #Width and height of the cells
        width = cell.rect.width
        height = cell.rect.height
        
        self.mouse_pressed= False
        self.game_active = False
    
        #Add the cells tp the board
        for i in range(rows):
            self.table.append([])
            for j in range(cols):
                self.table[i].append(Cell(i*(height+2), j*(width+2)))

                
    #Calculate the number of neighbors of each cell
    def set_number_of_neighbors(self):
        for array in self.table:
            for cell in array:
                cell.neighbors = 0
        
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                #If the cell is alive we sum one to the number of neighbors of each cell
                if self.table[i][j].is_alive:
                        for k in range(-1,2):
                            if j+k>=0 and j+k < len(self.table[i]):
                                #Top
                                if i-1 >= 0:
                                    self.table[i-1][j+k].neighbors += 1
                                #Bottom
                                if i+1 < len(self.table):
                                    self.table[i+1][j+k].neighbors += 1
                                if k!=0:
                                    #Right and left
                                    self.table[i][j+k].neighbors += 1                        
    
    #Determine which cell is alive or dead
    def update_lifes(self):
        for array in self.table:
            for cell in array:
                if cell.neighbors == 3:
                    cell.is_alive = True
                elif cell.neighbors>3 or cell.neighbors <= 1:
                    cell.is_alive = False
                
    
    

    def draw(self, screen):
        for array in self.table:
            for cell in array:
                cell.draw(screen)

    #Reset all the cell to initial state
    def reset(self):
        for array in self.table:
            for cell in array:
                cell.is_alive = False
        

