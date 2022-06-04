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

global_x_offset = 0
global_y_offset = 0

global_x_offset_increment = 1
global_y_offset_increment = 1

center_x = int(width/2)
center_y = int(height/2)


# test_square = Square([center_x, center_y], 40, 20,"1+1+2=")

rung = []

def iterate():
    init_points()
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glClearColor(0,0,0,0.0)
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def init_points():
    global width, height, center_x, center_y
    width = glutGet(GLUT_WINDOW_WIDTH)
    height= glutGet(GLUT_WINDOW_HEIGHT)
    center_x = width/2
    center_y = height/2
        
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
