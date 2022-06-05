from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import choice,randint
import cv2
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
        
        self.color = colors.red
        self.answer = eval(equation[:-1])
    def render_text(self):
        if(self.check_bounds()):
            glColor3f(*colors.white)
            glRasterPos2d(self.text_point_x,self.text_point_y)
            for c in self.equation:
                glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))
            #bug fixed by commenting this out
            # glFlush()
    def validate_answer(self,answer):
        if(answer == self.answer):
            print("4atteeeer!")
            self.color = colors.green
            return True
        return False
    def check_bounds(self):
        if(self.y - self.half_height - 5 > glutGet(GLUT_WINDOW_HEIGHT)):
            return False
        return True
    #needs to be removed, later
    def scale(self, scale_factor):
        self.x *= scale_factor
        self.y *= scale_factor
        self.half_width *= scale_factor
        self.half_height *= scale_factor
        self.text_point_x *=  scale_factor
        self.text_point_y *=  scale_factor
    def scale_x(self, scale_factor):
        self.x *= scale_factor
        # self.half_width *= scale_factor
        self.text_point_x =  self.x  - 0.5 * self.half_width - 2.4*len(self.equation)
    def scale_y(self, scale_factor):
        self.y *= scale_factor
        # self.half_height *= scale_factor
        self.text_point_y =  self.y  - 0.5 * self.half_height
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

class ImageSquare(Square):
    
    def __init__(self,center_point,width,height, image_location,cv2_imread_enum=cv2.IMREAD_COLOR):
        Square.__init__(self,center_point,width,height,"0 ")
        #defaults to cv2.IMREAD_IGNORE_ORIENTATION
        self.image_location = image_location
        self.cv2_imread_enum = cv2_imread_enum
        self.image = cv2.imread(image_location, cv2_imread_enum)
        # self.image = cv2.rotate(self.image,cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
        self.render_flag = True
        self.increment_x = choice([-1,1])
        self.increment_y = choice([-1,1])
    def toggle_render_flag(self):
        self.render_flag = not self.render_flag
    def display_image(self):
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 389,573,0,GL_RGB, GL_UNSIGNED_BYTE, self.image)
    def render(self):
        if(self.render_flag):
            glBegin(GL_QUADS)
            #rgb abdo
            glColor3f(* choice(colors.rgb))
            # glColor3f(*colors.teal)
            glVertex2f(self.x - self.half_width, self.y - self.half_height)
            glTexCoord2f(0.0, 0.0)
            glVertex2f(self.x + self.half_width, self.y - self.half_height)
            glTexCoord2f(0.0, 1.0)
            glVertex2f(self.x + self.half_width, self.y + self.half_height)
            glTexCoord2f(1.0, 0.0)
            glVertex2f(self.x - self.half_width, self.y + self.half_height)
            glTexCoord2f(0.0, 1.0)
            glEnd()
    def update(self, limitX, limitY):
        if(self.x >= limitX):
            self.increment_x = -0.01*limitX
            if(choice([False,True])):
                self.increment_x -= (self.increment_x)
            if(choice([False,True])):
                self.increment_y = -(self.increment_y)
        if(self.x <= 0):
            self.increment_x = +0.01*limitX
            if(choice([False,True])):
                self.increment_x += (self.increment_x)
            if(choice([False,True])):
                self.increment_y = -(self.increment_y)
        if(self.y >= limitY):
            self.increment_y = -0.01*limitY
            if(choice([False,True])):
                self.increment_y -= (self.increment_y)
            if(choice([False,True])):
                self.increment_x = -(self.increment_x)
        if(self.y <= 0):
            self.increment_y = +0.01*limitY
            if(choice([False,True])):
                self.increment_y = -(self.increment_y)
            if(choice([False,True])):
                self.increment_x = -(self.increment_x)
        self.x += self.increment_x
        self.y += self.increment_y
    def check_collision(self, x, y):
        min_x,max_x = self.x - self.half_width, self.x + self.half_width
        min_y,max_y = self.y - self.half_height, self.y + self.half_height
        if(min_x <= x <= max_x) and (min_y <= y <= max_y):
            return True
        return False
        
        