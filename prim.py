#To print the prime numbers between the given range
for i in range(10,101):
    if i > 1:
        for num in range(2, (int(i**0.5))+1):
            if i % num == 0 :
                break
            
        else:
            print(i)    
                    
            
                
     