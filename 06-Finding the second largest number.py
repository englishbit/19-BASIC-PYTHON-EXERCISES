#logic for finding the second largest
def find_sec_larg(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        
        if num2>=num3:
            sec_largest=num2
            thrd_largest=num3
        else:
            sec_largest=num3
            thrd_largest=num2
    elif num2>=num1 and num2>=num3:
        
        if num1>=num3:
            sec_largest=num1
            thrd_largest=num3
        else:
            sec_largest=num3
            thrd_largest=num1
    else:
        
        if num2>=num1:
            sec_largest=num2
            thrd_largest=num1
        else:
            sec_largest=num1
            thrd_largest=num2  
    return sec_largest      
                 
#logic for output
print(find_sec_larg(5,3,0))


