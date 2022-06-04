from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import scorer
import difficulty
import render_opengl
from square import Square

starting_point_y = -10
square_spawn_timer = 1000
square_speed = 10

#this isn't working
def generate_square():
    render_opengl.rung.append(Square([render_opengl.center_y, starting_point_y], 40, 20,difficulty.generate_linear_equation(2)[2]))
def generate_square_timer(value):
    glutTimerFunc(square_spawn_timer,generate_square_timer,value)
    generate_square()
    
def rung_rectangles_update(value):
    glutTimerFunc(square_speed,rung_rectangles_update,value)
    # test_square.update(global_x_offset_increment)
    for square in render_opengl.rung:
        square.update(render_opengl.global_y_offset_increment)
        square.render
    glutPostRedisplay()
    
def showScreen():
    # render_opengl.init_points()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    render_opengl.iterate()
    glColor3f(1.0, 0.0, 3.0)
    render_opengl.render_rung()
    render_opengl.render_rung_squares()
    # test_square.render()
    # test_square.render_text()
    glutSwapBuffers()

def render_window():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("OpenGL Coding Practice")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    rung_rectangles_update(0)
    generate_square_timer(0)
    glutMainLoop()
    

def main():
    render_window()


# generate_squares()
if __name__ == "__main__":
    main()