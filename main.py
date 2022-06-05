from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import cv2
import scorer
import difficulty
import render_opengl
from square import Square

starting_point_y = -10
square_spawn_timer = 2000
square_speed = 10
game_time_limit = 60
power_up_time_limit = 15
power_up_flag = False
is_game_over = False
ans = ""
current_game_score = 0

score_square = Square([0.05*render_opengl.width,0.96*render_opengl.height], 30,20,"0 ")
timer_square = Square([0.95*render_opengl.width,0.96*render_opengl.height], 30,20,"60 ")


#this isn't working
def generate_square():
    render_opengl.rung.append(Square([render_opengl.center_x, starting_point_y], 40, 20,difficulty.generate_linear_equation(2)[2]))
def generate_square_timer(value):
    glutTimerFunc(square_spawn_timer,generate_square_timer,value)
    generate_square()
def update_time(value):
    global power_up_time_limit, game_time_limit, power_up_flag, is_game_over
    
    if(power_up_time_limit <= 0):
        power_up_time_limit = 15
        power_up_flag = False
    if(game_time_limit <= 0):
        game_time_limit = 60
        is_game_over = True
    if(not power_up_flag):
        glutTimerFunc(1000,update_time,value)
        game_time_limit -= 1
    else:
        glutTimerFunc(1000,update_time,value)
        power_up_time_limit -= 1
def rung_rectangles_update(value):
    glutTimerFunc(square_speed,rung_rectangles_update,value)
    # test_square.update(global_x_offset_increment)
    for square in render_opengl.rung:
        square.update(render_opengl.global_y_offset_increment)
        square.render
    glutPostRedisplay()
def resize_objects():
    if(render_opengl.init_points()):
        print("resizing_object")
        for square in [timer_square, score_square, *render_opengl.rung]:
            square.scale_x(render_opengl.scale_factor_x)
            square.scale_y(render_opengl.scale_factor_y)
def showScreen():
    # render_opengl.init_points()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    render_opengl.iterate()
    glColor3f(1.0, 0.0, 3.0)
    render_opengl.render_rung()
    resize_objects()
    render_opengl.render_rung_squares()
    score_square.equation = str(current_game_score)
    score_square.render()
    score_square.render_text()
    
    timer_square.equation = str(game_time_limit)
    timer_square.render()
    timer_square.render_text()
    # test_square.render()
    # test_square.render_text()
    glutSwapBuffers()

#useless in this object
def validate_solutions(solution):
    global current_game_score
    for square in render_opengl.rung:
        if(square.validate_answer(solution)):
            current_game_score += 1
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

def render_window():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(render_opengl.width, render_opengl.height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("OpenGL Coding Practice")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutKeyboardFunc(NumKeyboard)
    # glutSpecialFunc(specialKey)
    rung_rectangles_update(0)
    generate_square_timer(0)
    update_time(0)
    glutMainLoop()
    

def main():
    render_window()
    

# generate_squares()
if __name__ == "__main__":
    main()