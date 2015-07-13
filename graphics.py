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


import pygame

import game_config
import pieces


class Singleton(type):
    _instances = {}
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Singleton, self).__call__(*args, **kwargs)
        return self._instances[self]


class Graphics(object):
    """
    Render functions
    """
    __metaclass__ = Singleton
 
    def __init__(self):
        self.display_surf = pygame.display.set_mode((game_config.WINDOW_WIDTH, 
                                                     game_config.WINDOW_HEIGHT))
    
    def get_display_surf(self):
        return self.display_surf
        
    def clear_display_surf(self):
        self.get_display_surf().fill(game_config.BLACK)
        
    def update_display_surf(self):
        pygame.display.update()
    
    def make_text_obj(self, text, colour, font_size):
        """
        Render a given text into a surface. Gets the surface its rectangle
        """
        font = pygame.font.Font(None, font_size)
        surf = font.render(text, True, colour)
        return surf, surf.get_rect()

    def box_to_pixel_coord(self, box_x, box_y, pixel_offset_x, pixel_offset_y):
        """
        Gets the pixel from coordinates (x,y) and adds an offset
        """
        return (pixel_offset_x + (box_x * game_config.BOX_SIZE_IN_PIXELS),
                pixel_offset_y + (box_y * game_config.BOX_SIZE_IN_PIXELS))
 
    def draw_box_with_empty_border(self, x, y, width, height, color, border_size=3):
        """
        Draws a rectangular shape with empty border
        """
        if color and width > 1 and height > 1:
            pygame.draw.rect(self.get_display_surf(), color, (x + border_size, y + border_size, width - border_size, height - border_size))
        
    def draw_rectangle(self, pos_x, pos_y, width, height, color=game_config.GRAY, border_size=5):
        """
        Draws the rectangle of the title
        """
        pygame.draw.rect(self.get_display_surf(),
                          color, 
                          (pos_x, 
                          pos_y, 
                          width, 
                          height), 
                          border_size)
        
    def draw_board(self, board):
        """
        Draws the board
        """
        self.draw_rectangle(game_config.BOARD_PIXEL_POSX,
                            game_config.BOARD_PIXEL_POSY,
                            game_config.BOARD_BOX_COUNT_X * game_config.BOX_SIZE_IN_PIXELS,
                            game_config.BOARD_BOX_COUNT_Y * game_config.BOX_SIZE_IN_PIXELS)
        for column_x in range(board.get_width()):
            for row_y in range(board.get_height()):
                pixel_x, pixel_y = self.box_to_pixel_coord(column_x, 
                                                           row_y, 
                                                           game_config.BOARD_PIXEL_POSX, 
                                                           game_config.BOARD_PIXEL_POSY)
                self.draw_box_with_empty_border(pixel_x, 
                              pixel_y, 
                              game_config.BOX_SIZE_IN_PIXELS, 
                              game_config.BOX_SIZE_IN_PIXELS, 
                              board.get_cell(column_x, row_y))
    
    def draw_score_level_next_piece(self, score, level, piece):
        """
        Draw values of score and level info
        """
        score_surf, score_rect = self.make_text_obj('Score: %04d'  % score, 
                                                   game_config.WHITE, game_config.FONT_SIZE_BASIC)
        
        level_surf, level_rect = self.make_text_obj('Level: %03d' % level,
                                                     game_config.WHITE, game_config.FONT_SIZE_BASIC)
        next_surf, next_rect = self.make_text_obj('Next: ', 
                                                   game_config.WHITE, game_config.FONT_SIZE_BASIC)
        score_rect.left = (game_config.WINDOW_WIDTH * 1.7 - score_rect.width) / 2       
        text_block_height = score_rect.height + level_rect.height + next_rect.height + pieces.Piece.TEMPLATE_HEIGHT + \
            3 * game_config.TEXT_LINE_SPACING

        score_rect.top = (game_config.WINDOW_HEIGHT - text_block_height) / 2
        
        self.get_display_surf().blit(score_surf, score_rect)

        level_rect.left = (game_config.WINDOW_WIDTH * 1.7 - level_rect.width) / 2 
        level_rect.top = score_rect.top + game_config.TEXT_LINE_SPACING
        
        self.get_display_surf().blit(level_surf, level_rect)
        
        next_rect.left = (game_config.WINDOW_WIDTH * 1.7 - next_rect.width) / 2 
        next_rect.top = level_rect.top + game_config.TEXT_LINE_SPACING
        
        self.get_display_surf().blit(next_surf, next_rect)
        
        self.draw_piece(piece, (game_config.WINDOW_WIDTH * 1.4 - pieces.Piece.TEMPLATE_WIDTH) / 2,
                        next_rect.top + pieces.Piece.TEMPLATE_HEIGHT)

    def draw_piece(self, piece, offset_x, offset_y):
        """
        Draws the piece in the board
        """
        shape_to_draw = piece.get_template()
        for x in range(pieces.Piece.TEMPLATE_WIDTH):
            for y in range(pieces.Piece.TEMPLATE_HEIGHT):
                if shape_to_draw[y][x]:
                    pixel_x, pixel_y = self.box_to_pixel_coord(piece.get_pos_x() + x, piece.get_pos_y() + y, 
                                                               offset_x, offset_y)
                    self.draw_box_with_empty_border(pixel_x, pixel_y, game_config.BOX_SIZE_IN_PIXELS, 
                                  game_config.BOX_SIZE_IN_PIXELS, piece.color)


    def draw_statistics(self, count_stats, type_font):
        """
        Draws game statistics
        """ 
        font = pygame.font.Font(None, type_font)
        statictics_surf = font.render('Statistics: ', True, game_config.WHITE)
        statistics_rect = statictics_surf.get_rect()
        
        statistics_rect.left = (game_config.WINDOW_WIDTH * 0.2 - statistics_rect.width) / 2
        text_block_height = statistics_rect.height + pieces.Piece.TEMPLATE_HEIGHT * 7 + game_config.TEXT_LINE_SPACING * 7 
        statistics_rect.top = (game_config.WINDOW_HEIGHT - text_block_height) / 2
        self.get_display_surf().blit(statictics_surf, statistics_rect)
        i = 1
        for piece in pieces.PieceSelector.piece_types:
            instance_p = piece(0, 0)
            count_surf = font.render("%03d" % (count_stats.get(piece, 0)), True, game_config.WHITE)
            count_rect = count_surf.get_rect()
                  
            text_block_width = pieces.Piece.TEMPLATE_WIDTH + count_rect.width + game_config.TEXT_LINE_HORIZONTAL_SPACING
            self.draw_piece(instance_p, (game_config.WINDOW_WIDTH * 0.2 - text_block_width ) / 2, 
                           statistics_rect.top + (game_config.TEXT_LINE_SPACING)*i)
            
            count_rect.left = game_config.WINDOW_WIDTH * 0.2 - text_block_width + game_config.TEXT_LINE_HORIZONTAL_SPACING
            count_rect.top = statistics_rect.top + (game_config.TEXT_LINE_SPACING)*i + 15
             
            self.get_display_surf().blit(count_surf, count_rect)
            
            i += 1             
                        