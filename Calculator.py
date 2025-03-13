#Here I will make a simple calculator that will be able to
#add, subtract, divide, and multiply

#Addition Function
def add(num1, num2):
    return(f'{num1} + {num2} = {num1+num2}')

#Subtraction Function
def sub(num1, num2):
    return(f'{num1} - {num2} = {num1-num2}')

#Multiplication Function
def mult(num1, num2):
    return(f'{num1} * {num2} = {num1*num2}')

#Division Function
def div(num1, num2):
    if(num2 == 0):
        return "Error: Division by 0 is undefined. Please restart."
    return(f'{num1} / {num2} = {num1/num2}')

#Opperation Symbol Validator
def get_opp():
    valid_opps=('+','-', '*', '/')
    while True: 
        opp = input("What is the Opperation(+, -, *, /): ")

        if opp in valid_opps:
            return opp
        else: 
            print("Invalid!! Please input a valid operator.")




#Getting the users input
num1 = float(input("What is your first number: "))
opp = get_opp()
num2 = float(input("What is your second number: "))
    

 


#Conditional statement to determine which function to use and print result

if(opp=="+"):
    print(add(num1, num2))

elif(opp=='-'):
    print(sub(num1, num2))

elif(opp=='*'):
    print(mult(num1, num2))

elif(opp=='/'):
    print(div(num1, num2))
