from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import pyautogui
from square import Square
width, height = 500,500
color_channels = 3 #no alpha channel for transparency

game_title = "Math Hero: Ascension"
# Change SPEED to make the game go faster
playing = True
SPEED = 10
scale_factor_x = 1
scale_factor_y = 1

global_x_offset = 0
global_y_offset = 0

global_x_offset_increment = 1
global_y_offset_increment = 1

center_x = int(width/2)
center_y = int(height/2)


# test_square = Square([center_x, center_y], 40, 20,"1+1+2=")

rung = []

def iterate():
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glClearColor(0,0,0,0.0)
    gluOrtho2D(0.0, width, 0.0, height)
    glMatrixMode (GL_MODELVIEW)
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glLoadIdentity()
    
def init_points():
    global width, height, center_x, center_y, scale_factor_x, scale_factor_y
    new_width = glutGet(GLUT_WINDOW_WIDTH)
    new_height= glutGet(GLUT_WINDOW_HEIGHT)
    #check if window size has changed
    if((new_height != height) or (new_width != width)):
        scale_factor_x = new_width/width
        scale_factor_y = new_height/height
        width = new_width
        height = new_height
        center_x = width/2
        center_y = height/2
        return True
    scale_factor_x = 1
    scale_factor_y = 1
    return False
        
def render_rung():
    rung_thickness = int(width/100)/2
    glBegin(GL_QUADS)
    glVertex2f(center_x - rung_thickness, 0 )
    glVertex2f(center_x + rung_thickness, 0)
    glVertex2f(center_x + rung_thickness, height)
    glVertex2f(center_x - rung_thickness, height)
    glEnd()
    
def render_rung_squares():
    for square in rung:
        square.render()
        square.render_text()
        #once it gets out of bound
        if not square.check_bounds():
            print('removing square')
            rung.remove(square)
