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

import random
import game_config


class Piece(object):
    """
    Represents the pieces of the game    
    """
    TEMPLATE_WIDTH = 4
    TEMPLATE_HEIGHT = 4 
    
    def __init__(self, pos_x, pos_y):
        """
        Initialization datas of the piece   
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rotations = 4 # Each piece has four positions to rotate
        self.shape_rotation = 0 #default rotation

    def get_num_rotations(self):
        """
        Returns the number of possible rotations   
        """
        return self.rotations
    
    def get_pos_x(self):
        return self.pos_x
    
    def get_pos_y(self):
        return self.pos_y
    
    def set_pos_x(self, pos_x):
        self.pos_x += pos_x
    
    def set_pos_y(self, pos_y):
        self.pos_y += pos_y
    
    def change_shape_rotation(self):   
        self.shape_rotation = self.next_rotation()
    
    def get_shape_rotation(self):
        """
        Returns the current rotation   
        """
        return self.shape_rotation

    def get_template(self): 
        """
        Returns the template of the piece   
        """   
        return self.template[self.shape_rotation]

    def next_rotation(self):
        """
        Calculates the next possible rotation
        """
        return (self.shape_rotation + 1) % self.get_num_rotations()
    
    
class I_block(Piece):
    template = \
    [
        [
            [ 0, 0, 0, 0 ],
            [ 1, 1, 1, 1 ],
            [ 0, 0, 0, 0 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 1, 0 ],
            [ 0, 0, 1, 0 ],
            [ 0, 0, 1, 0 ],
            [ 0, 0, 1, 0 ]
         ],
        [
            [ 0, 0, 0, 0 ],
            [ 1, 1, 1, 1 ],
            [ 0, 0, 0, 0 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 1, 0 ],
            [ 0, 0, 1, 0 ],
            [ 0, 0, 1, 0 ],
            [ 0, 0, 1, 0 ]
        ]
    ]

    def __init__(self, x, y):
        super(I_block, self).__init__(x, y)
        self.color = game_config.RED
            
    def get_piece_color(self):
        return self.color


class O_block(Piece):
    template = \
    [
        [
            [ 0, 0, 0, 0 ],
            [ 0, 1, 1, 0 ],
            [ 0, 1, 1, 0 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 0, 0 ],
            [ 0, 1, 1, 0 ],
            [ 0, 1, 1, 0 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 0, 0 ],
            [ 0, 1, 1, 0 ],
            [ 0, 1, 1, 0 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 0, 0 ],
            [ 0, 1, 1, 0 ],
            [ 0, 1, 1, 0 ],
            [ 0, 0, 0, 0 ]
        ]
    ]
    
    def __init__(self, x, y):
        super(O_block, self).__init__(x, y)
        self.color = game_config.BLUE
        self.name = 'O_block'
        
    def get_piece_color(self):
        return self.color


class J_block(Piece):
    template = \
    [
        [
            [ 0, 0, 0, 0 ],
            [ 0, 1, 1, 1 ],
            [ 0, 0, 0, 1 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 1, 0 ],
            [ 0, 0, 1, 0 ],
            [ 0, 1, 1, 0 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 1, 0, 0 ],
            [ 0, 1, 1, 1 ],
            [ 0, 0, 0, 0 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 1, 1 ],
            [ 0, 0, 1, 0 ],
            [ 0, 0, 1, 0 ],
            [ 0, 0, 0, 0 ]
        ]
    ]
    
    def __init__(self, x, y):
        super(J_block, self).__init__(x, y)
        self.color = game_config.WHITE
        self.name = 'J_block'
        
    def get_piece_color(self):
        return self.color
    
    
class L_block(Piece):
    template = \
    [
        [
            [ 0, 0, 0, 0 ],
            [ 0, 1, 1, 1 ],
            [ 0, 1, 0, 0 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 1, 0 ],
            [ 0, 0, 1, 0 ],
            [ 0, 0, 1, 1 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 0, 1 ],
            [ 0, 1, 1, 1 ],
            [ 0, 0, 0, 0 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 1, 1, 0 ],
            [ 0, 0, 1, 0 ],
            [ 0, 0, 1, 0 ],
            [ 0, 0, 0, 0 ]
        ]
    ]
    
    def __init__(self, x, y):
        super(L_block, self).__init__(x, y)
        self.color = game_config.MAGENTA
        self.name = 'L_block'
    
    def get_piece_color(self):
        return self.color
    
    
class S_block(Piece):
    template = \
    [
        [
            [ 0, 0, 0, 0 ],
            [ 0, 0, 1, 1 ],
            [ 0, 1, 1, 0 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 1, 0 ],
            [ 0, 0, 1, 1 ],
            [ 0, 0, 0, 1 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 0, 0 ],
            [ 0, 0, 1, 1 ],
            [ 0, 1, 1, 0 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 1, 0 ],
            [ 0, 0, 1, 1 ],
            [ 0, 0, 0, 1 ],
            [ 0, 0, 0, 0 ]
        ]
    ]
    
    def __init__(self, x, y):
        super(S_block, self).__init__(x, y)
        self.color = game_config.GREEN
        self.name = 'S_block'
    
    def get_piece_color(self):
        return self.color


class T_block(Piece):
    template = \
    [
        [
            [ 0, 0, 0, 0 ],
            [ 0, 1, 1, 1 ],
            [ 0, 0, 1, 0 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 1, 0 ],
            [ 0, 0, 1, 1 ],
            [ 0, 0, 1, 0 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 1, 0 ],
            [ 0, 1, 1, 1 ],
            [ 0, 0, 0, 0 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 1, 0 ],
            [ 0, 1, 1, 0 ],
            [ 0, 0, 1, 0 ],
            [ 0, 0, 0, 0 ]
        ]
    ]

    def __init__(self, x, y):
        super(T_block, self).__init__(x, y)
        self.color = game_config.BROWN
        self.name = 'T_block'

    def get_piece_color(self):
        return self.color


class Z_block(Piece):
    template = \
    [
        [
            [ 0, 0, 0, 0 ],
            [ 0, 1, 1, 0 ],
            [ 0, 0, 1, 1 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 0, 1 ],
            [ 0, 0, 1, 1 ],
            [ 0, 0, 1, 0 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 0, 0 ],
            [ 0, 1, 1, 0 ],
            [ 0, 0, 1, 1 ],
            [ 0, 0, 0, 0 ]
        ],
        [
            [ 0, 0, 0, 1 ],
            [ 0, 0, 1, 1 ],
            [ 0, 0, 1, 0 ],
            [ 0, 0, 0, 0 ]
        ]
    ]
    
    def __init__(self, x, y):
        super(Z_block, self).__init__(x, y)
        self.color = game_config.CYAN
        self.name = 'z_block'

    def get_piece_color(self):
        return self.color


class PieceSelector:
    """
    Selects the next player piece
    """
    piece_types = [I_block,
                   O_block,
                   J_block,
                   L_block,
                   S_block,
                   T_block,
                   Z_block,]

    @classmethod
    def select_random_piece(self):
        index = random.randint(0, len(PieceSelector.piece_types) - 1)
        return PieceSelector.piece_types[index]
    