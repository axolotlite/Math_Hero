from glob import glob
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import scorer
import difficulty
import colors
import sys
import inflect


window={}
p = inflect.engine()
# import render_opengl
from square import Square, ImageSquare
import pyautogui
width, height = 500,500
color_channels = 3 #no alpha channel for transparency

game_title = "Math Hero: Ascension"
page=0
# Change SPEED to make the game go faster
playing = True
write_flag = True
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


menuSquare={}
menuX,menuY=250,450
menuStr=[game_title,"PLAY","SCORES","QUIT"]

for i in range(4):
    menuSquare[i]=Square([menuX,menuY],70,20,menuStr[i])
    menuY-=100
menuSquare[0].x=245
menuSquare[0].color=colors.black

# test_square = Square([center_x, center_y], 40, 20,"1+1+2=")

rung = []
highscore_square = []
score_diplay_num = 5
def init_scoreboard():
    scorer.readHighscores()
    high_scores = scorer.highscores_array[:score_diplay_num]
    high_scores = high_scores[::-1]
    highscore_square.append(Square([center_x,0.9*height], 0.1*width,0.2*height,"Highscores "))
    highscore_square[-1].color = colors.black
    print(high_scores)
    i = 0
    counter = 6
    for score in high_scores:
        i+=1
        counter -= 1
        highscore_square.append(Square([0.5*center_x,0.15*i*height], 0.1*width,0.2*height,str(counter) + ") " + str(score)))
        highscore_square[-1].color = colors.black
# init_scoreboard()
def drawText(x,y,word):
    glColor3f(0,1,0)
    glRasterPos2d(x,y)
    for c in word:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))

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
        print(new_width)
        print(new_height)
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
#game variables
starting_point_y = -10
square_spawn_timer = 2000
abdo_glide_speed = 30
square_speed = 10
#resetable
game_time_limit = 60
power_up_time_limit = 15
abdo_appearance_time = random.randint(20,50)
power_up_flag = False
is_game_over = False
ans = ""
current_game_score = 0

score_square = Square([0.05*width,0.96*height], 30,20,"0 ")
timer_square = Square([0.95*width,0.96*height], 30,20,"60 ")
abdo_square = ImageSquare([center_x + 20,center_y - 40],40,40,"abdo_stare.png")

def reset_game_parameters():
    global rung, game_time_limit, power_up_time_limit, abdo_appearance_time, power_up_flag, is_game_over, ans, current_game_score, write_flag
    write_flag = True
    rung.clear()
    game_time_limit = 60
    power_up_time_limit = 15
    abdo_appearance_time = random.randint(20,50)
    abdo_square.render_flag = False
    power_up_flag = False
    is_game_over = False
    ans = ""
    current_game_score = 0
    playing = True
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
    global power_up_time_limit, game_time_limit, power_up_flag, is_game_over, score_increment,page
    #print(game_time_limit)
    if(abdo_appearance_time == game_time_limit):
        print("godddamn it")
        abdo_square.render_flag = True
    if(power_up_time_limit <= 0):
        power_up_time_limit = 15
        power_up_flag = False
    if(game_time_limit <= 0):
        game_time_limit = 60
        is_game_over = True
        page=4
    if(not power_up_flag):
        # print("normal time")
        score_increment = 1
        glutTimerFunc(1000,update_time,value)
        game_time_limit -= 1
    else:
        # print("Za Waruudoo")
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
        for square in [timer_square, score_square, abdo_square, *rung,menuSquare[0],menuSquare[1],menuSquare[2],menuSquare[3]]:
            square.scale_x(scale_factor_x)
            square.scale_y(scale_factor_y)


def mainMenu():
    global menuSquare
    for i in range(4):
        menuSquare[i].render()
        menuSquare[i].render_text()
    drawText(20,65,"F1: Restart")
    drawText(20,35,"F2: Menu")



def showScreen():
    global ans, write_flag
    # init_points()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    resize_objects()
    
    if (page==0):
        mainMenu()

    elif(page==1):
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
        drawText(20,45,"Answer: "+ans)
        abdo_square.display_image()
        abdo_square.render()
    elif(page == 2):
        for square in highscore_square:
            # print('render deez')
            square.render()
            square.render_text()
            
        
    elif(page==4):
        scoreStr=score_square.equation
        if(write_flag):
            write_flag = False
            scorer.readHighscores()
            scorer.addScore(int(scoreStr))
            print(scorer.highscores_array)
            scorer.writeHighscore()
        drawText(150,350,"Your Score: "+scoreStr)
        drawText(150,250,"You Ranked: "+ p.ordinal(scorer.highscores_array.index(int(scoreStr))+1))

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
    global page

    if(key== GLUT_KEY_F1):
        reset_game_parameters()

    if(key== GLUT_KEY_F2):
        reset_game_parameters()
        highscore_square.clear()
        page=0
    
    glutPostRedisplay();


def click_abdo(btn,state,x,y):
    global power_up_flag,page, write_flag,window
    mouseX,mouseY=0,0
    if(btn==GLUT_LEFT_BUTTON and state==GLUT_DOWN):
        mouseX=x; mouseX= 0.5 + 1.0 *mouseX 
        mouseY=height-y; mouseY= 0.5 + 1.0 *mouseY *1
    
        if(menuSquare[1].check_click(mouseX,mouseY) and page == 0):
            page=1
            glutKeyboardFunc(NumKeyboard)
            
            reset_game_parameters()

        if(menuSquare[2].check_click(mouseX,mouseY) and page == 0):
            page = 2
            init_scoreboard()
        if(menuSquare[3].check_click(mouseX,mouseY) and page == 0):
            write_flag = True
            #glutDestroyWindow(window)
            glutLeaveMainLoop()
            #exit()

        if(abdo_square.check_collision(mouseX,mouseY)):
            abdo_square.render_flag = False
            power_up_flag=True
    
    glutPostRedisplay()
        


def render_window():
    global window
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    window=glutCreateWindow("OpenGL Coding Practice")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutSpecialFunc(specialKey)
    rung_rectangles_update(0)
    generate_square_timer(0)
    abdo_glide_timer(0)
    update_time(0)
    glutMouseFunc(click_abdo)
    
    

    glutMainLoop()
    

def main():
    
    render_window()
    

# generate_squares()
if __name__ == "__main__":
    main()