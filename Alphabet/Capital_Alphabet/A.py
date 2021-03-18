def while_A():
    """
    By using While Loop A Pattern  
    
    """
    i=0
    while i<7:
        j=0
        while j<5:
            if ((j==0 or j==4) and i!=0) or (j>0 and j<4) and (i==0 or i==3):
                print("*",end=" ")
            else:
                print(end="  ")
            j+=1
        i+=1 
        print()
while_A()



def for_A():

  """ Pattern by Using for loop"""
  result_str="";    
  for row in range(0,7):
     for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
