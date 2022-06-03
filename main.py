import scorer
import difficulty
#calling an imported object method
# scorer.appendHighscore("anon","20")
# scorer.readHighscores()
#printing the highscores array is this easy
# print(scorer.get_sorted_highscores()[0])
# print(scorer.highscores_array)
# scorer.sortHighscores()
# scorer.addScore("anon",100)
# scorer.writeHighscore()
# difficulty.set_difficulty("dasea")
#depricated in favor of eval
# def calculate_solution(variables_array, operators_array):
#     right_hand_side
#     for variable, operator in zip(variables_array,operators_array):
#         match operator:
#             case '-':
#             case '+':
#             case '*':
#             case '/':
#             case '=':return right_hand_side
# variables_array, operators_array, equation = difficulty.generate_linear_equation(3)
# print(equation)
# #eval automatically allows us to output the mathematical equation of the problem
# print(eval(equation[:-1]))
difficulty.populate_rung(2)
# difficulty.validate_solution(23,1)
for equation in difficulty.rung:
    print(equation)
    #convert the string input into int
    answer = int(input("= "))
    difficulty.validate_solution(answer)
