# Challenge 
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

import os 

def main():
    # state objective of application

   os.system("cls")
   def checkValidity(testnum,numcounter):
        #while(run):
            try:
                return int(testnum)
            except:
                numberholder = checkValidity(input("Enter number" + str(i + 1)  + " for inclusion in the set\n"), i + 1)
                return int(checkValidity(numberholder,numcounter))
 
   def checkConstant(testnum):
        try:
            return int(testnum)
        except:
            numberholder = checkConstant(input("Enter number for addition check of the set"))
            return int(checkConstant(numberholder))
 
   print(
    """
    
    +======================================================+
    | Welcome to this application. It works in four steps  |
    | 1. A set of numbers in a list                        |
    | 2. The list is passed to the a function that checks  | 
    |    if any two numbers adds up to 17 or k             |
    | 3. Bonus: Part 2 Include an input that               |
    |    asks for list and constant k                      |
    +======================================================+
    
    """
    )
    
    # 1.  create an empty list and using a loop obtain the 4 numbers

   numcounter, num_const, sumrange = 1, 0 ,[]
   numberLIST = []
   indicator = False
    
   for i in range(4):
        numberholder = checkValidity(input("Enter number" + str(i + 1)  + " for inclusion in the set\n"), i + 1)
        numberLIST.append(numberholder)
        i += 1
   

    # 2.  collect the number k
   num_const = checkConstant(input("Enter number for addition check of the set\n"))
   
   for i in range(4):
        for j in range (4):
            dynamicrange = []
            if (i == j):
                continue
            else:
                dynamicrange.append(numberLIST[i])
                dynamicrange.append(numberLIST[j])
                dynamicrange.append(numberLIST[i] + numberLIST[j])
                sumrange.append(dynamicrange)
        j += 1
        
   i +=1

   for i in range(len(sumrange)):
       if sumrange[i][2]== num_const:
            print("The {} is valid as two of the numbers within the set add to {}, the numbers are {} and {}".format(numberLIST,num_const,sumrange[i][0],sumrange[i][1]))
            indicator = True
            break
   if indicator == False:
            print("List is invalid")
   

if __name__ == "__main__":
    main()