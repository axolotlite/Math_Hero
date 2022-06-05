
#testing import
def hello():
    print("Hello world from function") 

# highscores_dict = {}
highscores_array = []
# def writeHighscore():
#     highscores = open("highscores.txt",'w')
#     for username in highscores_dict:
#         #creates a string seperating each array element with a comma
#         print(highscores_dict[username])
#         if(len(highscores_dict[username]) > 1):
#             scores = ','.join(highscores_dict[username])
#         else:
#             scores = str(highscores_dict[username][0])
#         highscores.write(username + ':' + scores + '\n')
#     highscores.close()
def writeHighscore():
    highscores = open("highscores.txt",'w')
    for score in list(dict.fromkeys(highscores_array)):
        highscores.write(str(score) + '\n')
    highscores.close()
# def readHighscores():
#     highscores = open('highscores.txt', 'r')
#     for line in highscores:
#         username, scores = line.split(':')
#         #return an array of scores in case we want to keep multiple player scores
#         scores = scores.split(',')
#         #remove the linebreak from the last element in the array
#         scores[-1] = scores[-1].strip()
#         #convert string into int inside the array
#         scores = [int(score) for score in scores]
#         highscores_dict[username] = scores
#     highscores.close()
def readHighscores():
    global highscores_array
    highscores = open('highscores.txt', 'r')
    local_highscores_array = []
    for line in highscores:
        val = line.strip()
        local_highscores_array.append(int(val))
    
    local_highscores_array.sort(reverse=True)
    highscores_array = list(dict.fromkeys(local_highscores_array))
    highscores.close()
# def get_sorted_highscores():
#     #returns an array with the username then array of scores
#     return sorted(highscores_dict.items(), key=lambda y: y[1], reverse=False)
    
# def addScore(username, score):
#     if(username in highscores_dict):
#         #addes the user score to the highscore dictionary
#         if(score not in highscores_dict[username]):
#             highscores_dict[username].append(score)
#             #sort in descending order
#             highscores_dict[username].sort(reverse=True)
#     else:
#         highscores_dict[username] = [score]
#     print(highscores_dict)
def addScore(score):
    if(score not in highscores_array):
        highscores_array.append(score)
        highscores_array.sort(reverse=True)