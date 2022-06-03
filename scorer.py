
#testing import
def hello():
    print("Hello world from function") 

highscores_dict = {}
   
def writeHighscore():
    highscores = open("highscores_test.txt",'w')
    for username in highscores_dict:
        #creates a string seperating each array element with a comma
        scores = ','.join(highscores_dict[username])
        highscores.write(username + ':' + scores + '\n')
    highscores.close()

#depricated  
def appendHighscore(username, highscore):
    highscores = open("highscores.txt",'a')
    #new line break before writing
    highscores.write('\n')
    highscores.write(username +" : "+highscore)
    highscores.close()

def readHighscores():
    highscores = open('highscores.txt', 'r')
    for line in highscores:
        username, scores = line.split(':')
        #return an array of scores in case we want to keep multiple player scores
        scores = scores.split(',')
        #remove the linebreak from the last element in the array
        scores[-1] = scores[-1].strip()
        #convert string into int inside the array
        scores = [int(score) for score in scores]
        highscores_dict[username] = scores
    highscores.close()

def get_sorted_highscores():
    #returns an array with the username then array of scores
    return sorted(highscores_dict.items(), key=lambda y: y[1], reverse=True)
    # print(sorted_highscores_dict)
    
def addScore(username, score):
    if(username in highscores_dict):
        #addes the user score to the highscore dictionary
        highscores_dict[username].append(score)
        #sort in descending order
        highscores_dict[username].sort(reverse=True)
    else:
        highscores_dict[username] = [score]
    print(highscores_dict)