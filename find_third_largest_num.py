
def third_larg_num(num1,num2,num3,num4):
    
    
    #first step
    if num1>=num2 and num1>=num3 and num1>=num4:
        if num2>=num3 and num2>=num4:
            if num3>=num4:
                third_largest=num3
            else:
                third_largest=num4
        elif num3>=num2 and num3>=num4:
            if num2>=num4:
                third_largest=num2
            else:
                third_largest=num4
        else:
            
                if num2>=num3:
                    third_largest=num2
                else:
                    third_largest=num3  
                    
                    
                    
    #second step          
                      
    elif num2>=num1 and num2>=num3 and num2>=num4:
        if num1>=num3 and num1>=num4:
            if num3>=num4:
                third_largest=num3
            else:
                third_largest=num4
        elif num3>=num1 and num3>=num4:
            if num1>=num4:
                third_largest=num1
            else:
                third_largest=num4 
        else:
             
             if num1>=num3:
                 third_largest=num1
             else:
                 third_largest=num3  
            
    #third step
    elif num3>=num1 and num3>=num2 and num3>=num4:
        if num1>=num2 and num1>=num4:
            if num2>=num4:
                third_largest=num2
            else:
                third_largest=num4      
        elif num2>=num1 and num2>=num4:
            if num1>=num4:
                third_largets=num1
            else:
                third_largest=num4
            
        else:
            if num1>=num2:
                third_largest=num1
            else:
                third_largest=num2
                
                
    #final step
                     
    else:
        if num1>=num2 and num1>=num3:
            if num2>=num3:
                third_largest=num2
            else:
                third_largest=num3
        elif num2>=num1 and num2>=num3:
            if num1>=num3:
                third_largest=num1
            else:
                third_largest=num3
        else:    
            
            if num1>=num2:
                third_largest=num1
            else:
                third_largest=num2
    return third_largest


print(third_larg_num(33,220,62,30))
