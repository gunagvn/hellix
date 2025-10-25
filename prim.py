varr = [] #Creating a new empty list to append values
for i in range(10,101):
    if i%2 != 0 : #This is the condition to check Whether the number is prime or not
        varr.append(i) #This syntax helps to append the values to that empty new list
        
print("Prime numbers:",varr)       
     