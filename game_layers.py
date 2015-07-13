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
import time

import game_config
from graphics import Graphics
import utils
import score
import board
import pieces
import inputs


graphics = Graphics() 

class InitLayer:
    """
    Represent the initial game menu
    
    """
     
    def __init__(self, owner):
        self.owner = owner
        self.text_menu = 'MENU: '
        self.text_enter = 'Press ENTER to play '   
        self.text_esc = 'Press ESC to exit'
        self.fps_clock = pygame.time.Clock()
        
    def initialize(self, previous_layer):
         
        self.title_surf_menu, self.title_rect_menu = graphics.make_text_obj(self.text_menu, 
                                                                           game_config.TITLE_COLOR,
                                                                           game_config.FONT_SIZE_BASIC)
        self.title_surf_enter, self.title_rect_enter = graphics.make_text_obj(self.text_enter, 
                                                                             game_config.TITLE_COLOR, 
                                                                             game_config.FONT_SIZE_BASIC)
        self.title_surf_esc, self.title_rect_esc = graphics.make_text_obj(self.text_esc, 
                                                                         game_config.TITLE_COLOR, 
                                                                         game_config.FONT_SIZE_BASIC) 

        self.title_rect_menu.left = (game_config.WINDOW_WIDTH - self.title_rect_menu.width) / 2
        self.title_rect_enter.left = (game_config.WINDOW_WIDTH - self.title_rect_enter.width) / 2
        self.title_rect_esc.left = (game_config.WINDOW_WIDTH - self.title_rect_esc.width) / 2
        
        text_block_height = self.title_rect_menu.height + self.title_rect_enter.height + self.title_rect_esc.height + \
            2 * game_config.TEXT_LINE_SPACING

        self.title_rect_menu.top = (game_config.WINDOW_HEIGHT - text_block_height) / 2
        self.title_rect_enter.top = self.title_rect_menu.top + game_config.TEXT_LINE_SPACING
        self.title_rect_esc.top =  self.title_rect_enter.top + game_config.TEXT_LINE_SPACING
 
        
    def run(self):
        """
        Waits for the user to either press the exit key or any other key to start the game
        
        """
        while inputs.check_for_key_press() == None:
            graphics.clear_display_surf()
            graphics.get_display_surf().blit(self.title_surf_menu, self.title_rect_menu)
            graphics.get_display_surf().blit(self.title_surf_enter, self.title_rect_enter)
            graphics.get_display_surf().blit(self.title_surf_esc, self.title_rect_esc)
            graphics.update_display_surf() 
            self.fps_clock.tick(4)
        inputs.clear_event_queue()

    def at_exit(self):
        self.owner.set_layer(self.owner.GAME_LAYER)

class GameLayer:
    """
    Processes the main game logic
    """   
    def __init__(self, owner):
        self.owner = owner
        self.score = score.Score()
        
        self.exit_signal = False
        self.normal_fall_time = game_config.NORMAL_FALL_TIME
        self.fall_time = self.normal_fall_time
        
        self.moving_right = False
        self.moving_left = False
        self.rotate = False

        self.accum_move_sideways_time = 0
        self.accum_fall_time = 0

        self.fall_time = game_config.NORMAL_FALL_TIME
        self.fall_time_changed = False
        
        self.signal_pause = False
        
        self.piece_type_count = {}

        self.fps_clock = pygame.time.Clock()

    def initialize(self, previous_layer):
        self.board = board.Board(game_config.BOARD_BOX_COUNT_Y, game_config.BOARD_BOX_COUNT_X)
        self.board.clear()
        
        self.moving_right = False
        self.moving_left = False
        self.rotate = False
        
        self.exit_signal = False
        
        self.accum_move_sideways_time = 0
        self.accum_fall_time = 0

        self.piece_type_count = {}
         
        self.set_falling_piece(self.new_piece())
        self.next_piece = self.new_piece()
        
        self.signal_pause = False

        if previous_layer == self.owner.GAME_LAYER:
            self.score.reset()

        self.update_normal_fall_time()
        self.fall_time = self.normal_fall_time
        self.fall_time_changed = False
 
    def set_falling_piece(self, piece):
        """
        Changes the type of falling piece and updates the piece usage stats
        """
        self.falling_piece = piece
        self.piece_type_count[type(piece)] = self.piece_type_count.get(type(piece), 0) + 1

    def new_piece(self):
        """
        Gets a random piece
        """
        piece_type = pieces.PieceSelector.select_random_piece()
        return piece_type(game_config.NEXT_PIECE_POSX, game_config.NEXT_PIECE_POSY)
    
    def can_rotate(self, current_piece):
        """
        Checks if the piece can rotate within the board
        """
        rotated_shape = current_piece.template[current_piece.next_rotation()]       
        for x in range(pieces.Piece.TEMPLATE_WIDTH):
            for y in range(pieces.Piece.TEMPLATE_HEIGHT):
                board_x = current_piece.get_pos_x() + x
                board_y = current_piece.get_pos_y() + y            
                if board_x < 0 and rotated_shape[y][x]:
                    return False
                if board_y < 0 and rotated_shape[y][x]:
                    return False
                if board_x >= game_config.BOARD_BOX_COUNT_X:
                    return False
                if board_y >= game_config.BOARD_BOX_COUNT_Y:
                    return False
                if  self.board.get_cell(board_x, board_y) and rotated_shape[y][x]:
                    return False
        return True
    def is_valid_position(self, current_piece, offset_x = 0, offset_y = 0):
        """
        Checks if the piece is in a valid position within the board      
        """
        for x in range(pieces.Piece.TEMPLATE_WIDTH):
            pos_x = current_piece.get_pos_x() + x + offset_x
            for y in range(pieces.Piece.TEMPLATE_HEIGHT):
                pos_y = current_piece.get_pos_y() + y + offset_y
                if current_piece.get_template()[y][x]:
                    if not utils.contains(0, 0, game_config.BOARD_BOX_COUNT_X, game_config.BOARD_BOX_COUNT_Y, pos_x, pos_y, 1, 1):
                        return False
                    if self.board.get_cell(pos_x, pos_y):
                        return False
        return True 
        
    def add_to_board(self, piece):
        """
        Adds the piece to the board, changing the color of the cells corresponding to 
        the piece.
        """
        for x in range(pieces.Piece.TEMPLATE_WIDTH):
            for y in range(pieces.Piece.TEMPLATE_HEIGHT):
                if piece.get_template()[y][x]:     
                    if piece.get_pos_x() + x < game_config.BOARD_BOX_COUNT_X and piece.get_pos_y() + y < game_config.BOARD_BOX_COUNT_Y:
                        self.board.set_cell(x + piece.get_pos_x(), y + piece.get_pos_y(), piece.get_piece_color())
    
    def update_normal_fall_time(self):
        self.normal_fall_time = max(game_config.FAST_FALL_TIME, game_config.NORMAL_FALL_TIME - game_config.NORMAL_FALL_TIME * self.score.get_fall_factor())

    def update(self, stepTime):
        """
        Updates the piece position in the board, always keeping the piece in a valid position.
        """
        if self.fall_time_changed:
            self.accum_fall_time = 0
            self.fall_time_changed = False
        if self.rotate:
            if self.can_rotate(self.falling_piece):
                self.falling_piece.change_shape_rotation()
            self.rotate = False
        if self.moving_left and self.is_valid_position(self.falling_piece, offset_x=-1):
            self.falling_piece.set_pos_x(-1) 
            self.moving_left = False
        if self.moving_right and self.is_valid_position(self.falling_piece, offset_x=1):
            self.falling_piece.set_pos_x(1)
            self.moving_right = False
        
        self.accum_fall_time += stepTime

        while self.accum_fall_time >= self.fall_time:
            if self.is_valid_position(self.falling_piece, offset_y=1):
                self.falling_piece.set_pos_y(1)
            else:
                self.add_to_board(self.falling_piece)
                rows_cleared = self.board.remove_complete_rows()
                self.score.update_score(rows_cleared)
                self.update_normal_fall_time()
                self.fall_time = self.normal_fall_time
    
                self.set_falling_piece(self.next_piece)
                self.next_piece = self.new_piece()
                self.accum_move_sideways_time = 0

                if not self.is_valid_position(self.falling_piece):
                    self.exit_signal = True

            self.accum_fall_time = max(self.accum_fall_time - self.fall_time, 0)
        
    def run(self):
        """
        Main game loop: processes inputs, updates the game status and renders the game scene
        """
        last_update_time = pygame.time.get_ticks()
        while not self.exit_signal:
            #Process inputs       
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    utils.terminate()             
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.is_valid_position(self.falling_piece, offset_x=-1):
                        self.moving_left = True
                        self.moving_right = False
                    elif event.key == pygame.K_RIGHT and self.is_valid_position(self.falling_piece, offset_x=1):
                        self.moving_right = True
                        self.moving_left = False
                    elif event.key == pygame.K_UP:
                        self.rotate = True                       
                    elif event.key == pygame.K_DOWN:
                        self.fall_time = game_config.FAST_FALL_TIME
                        self.fall_time_changed = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.fall_time = self.normal_fall_time
                        self.fall_time_changed = True
                    if event.key == pygame.K_ESCAPE:
                        utils.terminate()
                    if event.key == pygame.K_p: 
                        self.signal_pause = True
                  
            time = pygame.time.get_ticks()    
            delta_time = time - last_update_time
            
            while delta_time > 0:
                sim_step_time = game_config.STEP_TIME
                if delta_time - game_config.STEP_TIME < 0:
                    sim_step_time = delta_time

                self.update(sim_step_time)
                delta_time -= sim_step_time
                
                if self.exit_signal:
                    break
                if self.signal_pause:
                    self.exit_signal = True
                    break

            last_update_time = time
            
            #Draw the board
            graphics.clear_display_surf()
            graphics.draw_board(self.board)
            graphics.draw_score_level_next_piece(self.score.score_value, self.score.get_level(), self.next_piece)
            graphics.draw_statistics(self.piece_type_count, game_config.FONT_SIZE_BASIC)
            if self.falling_piece:
                graphics.draw_piece(self.falling_piece, game_config.BOARD_PIXEL_POSX, game_config.BOARD_PIXEL_POSY)
            graphics.update_display_surf()

            self.fps_clock.tick(game_config.MAX_FPS)
            
    def at_exit(self):
        """
        Sets the next layer to execute: GameOverLayer or PauseLayer     
        """
        if self.signal_pause:
            self.owner.set_layer(self.owner.PAUSE_LAYER)
            self.signal_pause = False
            self.exit_signal = False        
        else:
            self.owner.set_layer(self.owner.GAME_OVER_LAYER)
   
    def signal_exit(self):
        self.exit_signal = True


class  GameOverLayer:
    """
    Displays the game over screen.
    """
    def __init__(self, owner):
        self.owner = owner
        self.text = 'Game Over'
        self.fps_clock = pygame.time.Clock()
        
    def initialize(self, previous_layer):
        self.title_over_surf, self.title_over_rect = graphics.make_text_obj(self.text, game_config.TITLE_COLOR,
                                                                           game_config.FONT_SIZE_BIG)
        self.title_over_rect.left = (game_config.WINDOW_WIDTH - self.title_over_rect.width) / 2
        self.title_over_rect.top = (game_config.WINDOW_HEIGHT - self.title_over_rect.height ) / 2
    
    
    def run(self):  
        """
        Waits for the user input.
        """           
        while inputs.check_for_key_press() == None:
            graphics.clear_display_surf()
            graphics.get_display_surf().blit(self.title_over_surf, self.title_over_rect)
            graphics.update_display_surf()
            self.fps_clock.tick(4)
        inputs.clear_event_queue()          
        
    def at_exit(self):
        """
        Sets the next layer to execute: InitLayer.
        """
        self.owner.set_layer(self.owner.INIT_LAYER)


class  PauseLayer:
    """
    Shows the pause screen.
    """
    def __init__(self, owner):
        self.owner = owner
        self.text = 'Pause'
        self.fps_clock = pygame.time.Clock()
        
    def initialize(self, previous_layer):
        self.title_pause_surf, self.title_pause_rect = graphics.make_text_obj(self.text, game_config.TITLE_COLOR,
                                                                           game_config.FONT_SIZE_BIG)
        self.title_pause_rect.left = (game_config.WINDOW_WIDTH - self.title_pause_rect.width) / 2
        self.title_pause_rect.top = (game_config.WINDOW_HEIGHT - self.title_pause_rect.height) / 2
    
    def run(self):
        """
        Waits for the user input.
        """
        while inputs.check_for_key_press() == None:
            graphics.clear_display_surf()
            graphics.get_display_surf().blit(self.title_pause_surf, self.title_pause_rect)
            graphics.update_display_surf()           
            self.fps_clock.tick(4)
        inputs.clear_event_queue()            
        
    def at_exit(self):
        """
        Goes back to GameLayer.
        """
        self.owner.set_layer(self.owner.GAME_LAYER)
        self.owner.current_layer.run()
        self.owner.current_layer.at_exit()
