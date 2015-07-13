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


import sys
    
def terminate():
    """
    Terminates the game       
    """
    sys.exit(0)      


def contains(x0, y0, w0, h0, x1, y1, w1, h1):
    """
    Return True if the rectangle [x0, y0, w0, h0] contains [x1, y1, w1, h1]       
    """
    return x0 <= x1 and (x1 + w1) <= (x0 + w0) and \
        y0 <= y1 and (y1 + h1) <= (y0 + h0)
            
            