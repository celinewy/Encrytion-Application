# calculator.py
# Celine Yeung, ENDG 233 F21
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.

#Prompt user to enter in their inputs
first_value = int(input('Enter the first integer value: '))         #Prompt user for first integer value
first_op = input('Enter the first operator: ')                      #Prompt user for first operator
second_value = int(input('Enter the second integer value: '))       #Prompt user for second integer value
second_op = input('Enter the second operator: ')                    #Prompt user for second operator
third_value = int(input('Enter the third integer value: '))         #Prompt user for third integer value

#Print users inputs as an expression in the order it is was entered to display what is going to be solved for
print('Entered expression:', first_value, first_op, second_value, second_op, third_value)

#Calculations of input values in accordance to BEDMAS order of operations and working left to right of the expression: 
                              
if first_op == '/':                                #If first operator is division                          
    second_value = first_value // second_value     #Due to BEDMAS, division must be done first on the first two values

#All possible second operators that will be applied between the second & third value after the division of the first & second value
    if second_op == '/':                             
        third_value = second_value // third_value         
    elif second_op == '*':                               
        third_value = second_value * third_value        
    elif second_op == '+':                                  
        third_value = second_value + third_value          
    elif second_op == '-':                               
        third_value = second_value - third_value    
                  
    print('Your final answer =', third_value)      #Print answer       

if first_op == '*':                                #If first operator is multipulcation               
    second_value = first_value * second_value      #Due to BEDMAS, multipulcation must be done first on the first two values

#All possible second operators that will be applied between the second & third value after the multipulcation of the first & second value
    if second_op == '/':                               
        third_value = second_value // third_value    
    elif second_op == '*':                         
        third_value = second_value * third_value           
    elif second_op == '+':                          
        third_value = second_value + third_value            
    elif second_op == '-':                          
        third_value = second_value - third_value    

    print('Your final answer =', third_value)       #Print answer                

#If first operator is addition examine the second operator to make sure division/multipulcation is done first due to BEDMAS:
if first_op == '+':                                                
   
    if second_op == '/':                            #If second operator is division 
        second_value = second_value // third_value  #Due to BEDMAS, division of the last two values must be done first
        third_value = first_value + second_value    #Due to BEDMAS, after division add from left to right of the expression                
    
    elif second_op == '*':                          #If second operator is mutlipulcation
        second_value = second_value * third_value   #Due to BEDMAS, multipulcation of the last two values must be done first
        third_value = first_value + second_value    #Due to BEDMAS, after multipulcation add from left to right of the expression   
    
    elif second_op == '+':                                      #If second operator is addition
       third_value = first_value + second_value + third_value   #Add from the left to the right of the expression
    
    elif second_op == '-':                                      #If second operator is subtraction
        third_value = first_value + second_value - third_value  #Working left to right of the expression, first add then subtract

    print('Your final answer =', third_value)                   #Print answer

#If first operator is subtraction examine the second operator to make sure division/multipulcation is done first due to BEDMAS:
if first_op == '-':
   
    if second_op == '/':                            #If second operator is division           
        second_value = second_value // third_value  #Due to BEDMAS, division of the last two values must be done first
        third_value = first_value - second_value    #Due to BEDMAS, after division subtract from left to right of the expression  
    
    elif second_op == '*':                          #If second operator is multipulcation
        second_value = second_value * third_value   #Due to BEDMAS, multipulcation of the last two values must be done first
        third_value = first_value - second_value    #Due to BEDMAS, after multipulcation subtract from left to right of the expression

    elif second_op == '+':                                       #If second operator is addition
       third_value = first_value - second_value + third_value    #Working left to right of the expression, first subtract then add

    elif second_op == '-':                                       #If second operator is subtraction
        third_value = first_value -  second_value - third_value  #Subtract from left to right of the expression
    
    print('Your final answer =', third_value)                    #Print answer