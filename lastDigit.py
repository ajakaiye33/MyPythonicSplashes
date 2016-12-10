# Using the flow statement to check the last digit of the two numbers
def lastDigit(num1, num2):
    # convert the integer to string
    convert_num1_str = str(num1)
    convert_num2_str = str(num2)
    #compare the last digit in each numbers
    if convert_num1_str[-1] == convert_num2_str[-1]:
        #return True
        print(True)
    else:
        #return False
        print(False)

lastDigit(234, 299)
lastDigit(856, 986)

