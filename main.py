from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import scorer
import difficulty
import render_opengl
from square import Square, ImageSquare
import pyautogui
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

score_increment = 1

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
            # print('removing square')
            rung.remove(square)
starting_point_y = -10
square_spawn_timer = 2000
abdo_glide_speed = 20
square_speed = 10
game_time_limit = 60
power_up_time_limit = 15
power_up_flag = False
is_game_over = False
ans = ""
current_game_score = 0

score_square = Square([0.05*width,0.96*height], 30,20,"0 ")
timer_square = Square([0.95*width,0.96*height], 30,20,"60 ")
abdo_square = ImageSquare([center_x + 20,center_y - 40],40,40,"abdo_stare.png")

#this isn't working
def generate_square():
    rung.append(Square([center_x, starting_point_y], 40, 20,difficulty.generate_linear_equation(2)[2]))
def generate_square_timer(value):
    glutTimerFunc(square_spawn_timer,generate_square_timer,value)
    generate_square()
def abdo_glide_timer(value):
    glutTimerFunc(abdo_glide_speed,abdo_glide_timer,value)
    abdo_square.update(width, height)
def update_time(value):
    global power_up_time_limit, game_time_limit, power_up_flag, is_game_over, score_increment
    
    if(power_up_time_limit <= 0):
        power_up_time_limit = 15
        power_up_flag = False
    if(game_time_limit <= 0):
        game_time_limit = 60
        is_game_over = True
    if(not power_up_flag):
        print("normal time")
        score_increment = 1
        glutTimerFunc(1000,update_time,value)
        game_time_limit -= 1
    else:
        print("Za Waruudoo")
        score_increment = 2
        glutTimerFunc(1000,update_time,value)
        power_up_time_limit -= 1
def rung_rectangles_update(value):
    glutTimerFunc(square_speed,rung_rectangles_update,value)
    # test_square.update(global_x_offset_increment)
    for square in rung:
        square.update(global_y_offset_increment)
        square.render
    glutPostRedisplay()
def resize_objects():
    if(init_points()):
        print("resizing_object")
        for square in [timer_square, score_square, abdo_square, *rung]:
            square.scale_x(scale_factor_x)
            square.scale_y(scale_factor_y)
def showScreen():
    # init_points()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    render_rung()
    resize_objects()
    render_rung_squares()
    score_square.equation = str(current_game_score)
    score_square.render()
    score_square.render_text()
    timer_square.equation = str(game_time_limit)
    timer_square.render()
    timer_square.render_text()
    abdo_square.display_image()
    abdo_square.render()
    # test_square.render()
    # test_square.render_text()
    glutSwapBuffers()

#useless in this object
def validate_solutions(solution):
    global current_game_score
    for square in rung:
        if(square.validate_answer(solution)):
            current_game_score += score_increment
def NumKeyboard(key, x , y):
    global ans
    key= str(key.decode(encoding='UTF-8',errors='strict'))
    if(key == '\b'):
        ans = ans[:-1]
    if(key == '-'):
        ans+= key
    if(key == "0" ):
        ans+=key
    if(key == "1" ):
        ans+=key
    if(key == "2" ):
        ans+=key
    if(key == "3" ):
        ans+=key
    if(key == "4" ):
        ans+=key
    if(key == "5" ):
        ans+=key
    if(key == "6" ):
        ans+=key
    if(key == "7" ):
        ans+=key
    if(key == "8" ):
        ans+=key
    if(key == "9" ):
        ans+=key
    if(key == "\r"):
        if(ans != ""):
            ans = int(ans)
            print(ans)
            validate_solutions(ans)
            ans = ""
        
def specialKey (key, x,y):
    if (key==GLUT_KEY_UP):
        alphaY+=5;
    if (key==GLUT_KEY_DOWN):
        alphaY-=5;
    if (key==GLUT_KEY_RIGHT):
        alphaX+=5;
    if (key==GLUT_KEY_LEFT):
        alphaX-=5;

    # if(key== GLUT_KEY_F1):
    #     # Restart

    # if(key== GLUT_KEY_F2):
        #Menu
    glutPostRedisplay();

def click_abdo(btn,state,x,y):
    global power_up_flag
    mouseX,mouseY=0,0
    if(btn==GLUT_LEFT_BUTTON and state==GLUT_DOWN):
        mouseX=x; mouseX= 0.5 + 1.0 *mouseX
        mouseY=500-y; mouseY= 0.5 + 1.0 *mouseY *1
        if(abdo_square.check_collision(mouseX,mouseY)):
            print("CLICKED ABDO NIGGA")
            abdo_square.render_flag = False
            power_up_flag=True
    
def render_window():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("OpenGL Coding Practice")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutKeyboardFunc(NumKeyboard)
    glutMouseFunc(click_abdo)
    # glutSpecialFunc(specialKey)
    rung_rectangles_update(0)
    generate_square_timer(0)
    abdo_glide_timer(0)
    update_time(0)
    glutMainLoop()
    

def main():
    render_window()
    

# generate_squares()
if __name__ == "__main__":
    main()