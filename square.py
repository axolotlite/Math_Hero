from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import colors
class Square:
    def __init__(self,center_point,width,height, equation):
        self.x = center_point[0]
        self.y = center_point[1]
        self.half_width = width
        self.half_height = height
        self.text_point_x =  center_point[0]  - 0.5 * width - 2.4*len(equation)
        self.text_point_y =  center_point[1] - 0.5 * height
        self.equation = equation
        self.render_flag = True
        self.color = colors.red
        self.answer = eval(equation[:-1])
        print(self.equation)
        print(self.answer)
    def render_text(self):
        if(self.check_bounds()):
            glColor3f(*colors.white)
            glRasterPos2d(self.text_point_x,self.text_point_y)
            for c in self.equation:
                glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))
            glFlush()
    def validate_answer(answer):
        if(answer == self.answer):
            self.color = colors.green
            return True
        return False
    
    def check_bounds(self):
        if(self.y - self.half_height - 5 > glutGet(GLUT_WINDOW_HEIGHT)):
            return False
        return True
    
    def render(self):
        if (self.check_bounds()):
            glBegin(GL_QUADS)
            glColor3f(*self.color)
            glVertex2f(self.x - self.half_width, self.y - self.half_height)
            glVertex2f(self.x + self.half_width, self.y - self.half_height)
            glVertex2f(self.x + self.half_width, self.y + self.half_height)
            glVertex2f(self.x - self.half_width, self.y + self.half_height)
            glEnd()
    def update(self, y_offset):
        # self.x += x_offset
        self.y += y_offset
        self.text_point_y += y_offset