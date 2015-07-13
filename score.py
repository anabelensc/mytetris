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


class Score:
    """
    Manages the score of the game.    
    """
    def __init__(self):
        self.score_value = 0 
        self.level_lines = 0 
        self.total_lines = 0
        self.level = 1 
        self.level_fall_factor = 0
    
    def reset(self):
        self.score_value = 0 
        self.level_lines = 0 
        self.total_lines = 0
        self.level = 1 
        self.level_fall_factor = 0
    
    def update_level_by_score(self):
        """
        Determines the current level and the fall factor by the score
        """
        self.level = int(self.total_lines / game_config.LEVEL_UP_LINE_COUNT) + 1
        self.level_fall_factor = (self.level - 1) * game_config.LEVEL_UP_FALL_FACTOR

    def get_level(self):
        return self.level

    def get_fall_factor(self):
        return self.level_fall_factor
    
    def update_score(self, new_lines):
        """
        Calculates and updates the score depending on the number of lines cleared so far
        """
        self.level_lines += new_lines
        self.total_lines += new_lines
        
        if self.level_lines <= 1:
            self.score_value += 40 * self.level
        elif self.level_lines == 2:
            self.score_value += 100 * self.level
        elif self.level_lines == 3:
            self.score_value += 300 * self.level  
        elif self.level_lines >= 4:
            self.score_value += 1200 * self.level 
        
        level_before_update = self.level

        self.update_level_by_score()

        if self.level != level_before_update:
            self.level_lines = 0
            

