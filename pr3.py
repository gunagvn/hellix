str_fun = input("Enter the string:")
count = 0 #Initiating the count

#Creating a for loop to iterate over the given string
for i in str_fun:          
    if i == 'a' or i == 'e' or i =='i' or i == 'o' or i == 'u': #if yes then count will be incremented
        count += 1
        
if count == 0 :
    print("vowels are not found in that string")
    
else:
    print("Total number of vowels are:"+ str(count))            
        
    
        
        
    
    