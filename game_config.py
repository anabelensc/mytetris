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


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)
RED = (155, 0, 0)
MAGENTA = (255, 0 , 255)
GREEN = (18 , 173 , 42)
BROWN = (255, 222 , 173)
CYAN = (0, 255, 255)
BLUE = (0, 191, 255)
GRAY = (136, 136, 136)
    
TITLE_COLOR = WHITE

BOARD_BOX_COUNT_X = 15
BOARD_BOX_COUNT_Y = 30
BOX_SIZE_IN_PIXELS = 16

# Position of the board in the screen
BOARD_PIXEL_POSX = (WINDOW_WIDTH - BOARD_BOX_COUNT_X * BOX_SIZE_IN_PIXELS) / 2
BOARD_PIXEL_POSY = (WINDOW_HEIGHT - BOARD_BOX_COUNT_Y * BOX_SIZE_IN_PIXELS) / 2

TEXT_LINE_SPACING = 50  # Vertical space between lines of text.
TEXT_LINE_HORIZONTAL_SPACING = 50  # Horizontal space between lines of text.
FONT_SIZE_BASIC = 25
FONT_SIZE_BIG = 100

NEXT_PIECE_POSX = 5
NEXT_PIECE_POSY = 0

NORMAL_FALL_TIME = 1000 # ms
FAST_FALL_TIME = 33 # ms
STEP_TIME = 50 # ms
MAX_FPS = 1000 / STEP_TIME + 1 # Add +1 in case the division is not exact

LEVEL_UP_LINE_COUNT = 10 # Number of lines to level up.
LEVEL_UP_FALL_FACTOR = 0.1 # Factor at which the fall time is increased at level up.
    
