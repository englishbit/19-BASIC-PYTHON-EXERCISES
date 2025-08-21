#logic for finding maximum
def max_of_three(num1,num2,num3,num4):
    
    if num1>num2 and num1>num3 and num1>num4:
        return num1
    elif num2>num1 and num2>num3 and num2>num4:
        return num2
    elif num3>num1 and num3>num2 and num3>num4:
        return num3
    else:
        return num4

print(max_of_three(2,10,5,7))    
    
    
        
        
        

