# Get to find out the max number from three numbers
def max_three(num1, num2, num3):
    #use the flow statement to find out
    if num1 > num2 and num1 > num3:
        #return num1
        print(num1)
    elif num2 > num3:
        #return num2
        print(num2)
    else:
        #return num3
        print(num3)

max_three(23,500,300)
max_three(1000,13, 40)
max_three(500,800,32)
