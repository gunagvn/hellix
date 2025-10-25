def fact_num(number):
#Creating a for loop
    for i in range(1,number):
        if (number % i == 0):
            print(i,end="")
            
number = int(input("Enter any number:"))            
#to print the statement        
print("Factor of a given number is") 
fact_num(number)
      
        
        