import random
#difficulty should correspond to the generated equations and its parameters
#modifies global difficulty variables

#the limit for random
limit = 10
score = 0
operator_array = ['-','+','*']
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