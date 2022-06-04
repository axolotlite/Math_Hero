import random
#difficulty should correspond to the generated equations and its parameters
#modifies global difficulty variables

#the limit for random
limit = 10
score = 0
operator_array = ['-','+','*','/']
#contains all equations 
rung = []

def set_difficulty(difficulty):
    #switch cases are only supported in python 3.10
    match difficulty:
        case "easy":
            print("easy diffculty")
            limit = 10
        case "medium":
            print("medium diffculty")
            limit = 100
        case "hard":
            limit = 1000
            print("hard diffculty")
        case default:
            print("default difficulty is easy")


#functionality can expand with the expansion of difficulty variables
def generate_linear_equation(variable_number):
    if(variable_number > 4):
        print("the current limit for linear equations is 4 variables")
        return
    #array containing the numbers
    variable_array = []
    #array contains the operators
    local_operator_array = []
    #string contains the entire equation
    linear_equation_string = ""
    for variable in range(variable_number):
        #the number will be between 1 and the limit, to prevent zero division error
        num = random.randint(1,limit)
        operator = random.choice(operator_array)
        
        variable_array.append(num)
        local_operator_array.append(operator)
        
        linear_equation_string += str(num) + operator
    #turn the last operator into '=' in the equation
    #could remove the '=' sign, since it's useless
    linear_equation_string = linear_equation_string[:-1] + '='
    #turn the last operator into '=' operator
    local_operator_array[-1] = '='
    return [variable_array, local_operator_array, linear_equation_string]

#depricated

# def populate_rung(equation_number):
#     for equation in range(equation_number):
#         #populate the rung with the equation string 
#         rung.append(generate_linear_equation(2)[2])
#     print(rung)
# def append_rung():
#     rung.append(generate_linear_equation(2)[2])
    
#depricated

# def validate_solution(solution,rung_square=-1):
#     #check if the answer is for all the rung values
#     if(rung_square == -1):
#         #iterators through each equation
#         for equation in rung:
#             #prepares the answer
#             answer = eval(equation[:-1])
#             # print(answer)
#             #if the answer is similar to the solution it prints so
#             if(answer == solution):
#                 print(equation + " " + str(solution) + " is correct")
#                 return True
#         #if the answer is not present in the rung array, then it's wrong
#         print("wrong")
#         return False
#     else:
#         answer = eval(rung[rung_square][:-1])
#         print(answer)
#     # if(answer == solution )

#useless in this object
def validate_solutions(solution):
    if(rung_square == -1):
        #iterators through each equation
        for square in rung:
                if(square.validate_answer(solution)):
                    score += 1