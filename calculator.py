import operator
def calculator():
    print("welcome to calcultor")
    input1 = int(input("enter the first number: "))
    print(input1)
     
    input2 = int(input("enter the second number: ")) 
    print(input2)

    operator = input("enter the operator: ")
   
    while True:
        
        if operator == "+":
            print(input1 + input2)
            break
        elif operator == "-":
            print(input1 - input2)
            break
        elif operator == "*":
            print(input1 * input2)
            break
        elif operator == "/":
            print(input1/input2)
            break
        else:
            print("invalid operator")
            exit()
calculator()
