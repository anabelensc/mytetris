'''
  Copyright (C) Ana Belen Sarabia Cobo <belensarabia@gmail.com>

  This program is free software; you can redistribute it and/or 
  modify it under the terms of the GNU General Public License
  Version 3 as published by the Free Software Foundation

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  
  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor,
  Boston, MA 02110-1301, USA.
'''


import game_config


class Board:
    """
    Manages the game board, which is a matrix of colors.
    """
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = []         
        
    def clear(self):
        """
        Initializes the board with blank cells.
        """
        for i in range(self.get_width()):
            self.grid.append([None] * self.get_height())
        return self.grid
    
    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width
    
    def is_complete_row(self, row):
        """
        Checks if the row is complete.
        """
        for column in range(self.get_width()):
            if not self.get_cell(column, row):
                return False
        return True
   
    def remove_complete_rows(self):
        """
        Remove complete rows in the board and packs non-empty cells at the bottom of the board.
        """
        lines_removed = 0
        row = self.get_height() - 1
        while row >= 0:
            if self.is_complete_row(row):
                for pull_down in range(row, 0, -1):
                    for column in range(self.get_width()):
                        self.set_cell(column, pull_down, None)
                    for column in range(self.get_width()):
                        self.set_cell(column, pull_down, self.get_cell(column, pull_down - 1))
                    for column in range(self.get_width()):
                        self.set_cell(column, 0, None)
                lines_removed += 1
            else:
                row -= 1
        return lines_removed
    
    def get_cell(self, column, row): 
        return self.grid[column][row]
    
    def set_cell(self, column, row, value):
        self.grid[column][row]= value
    
