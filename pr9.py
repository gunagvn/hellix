# To find the given number is a palindrome
real_num = int(input("Enter the number:"))
temp = real_num  #The seperate variable to store modified real_num
palin = 0 #empty variable to store reversed numbers

#This condition helps to reverse a Given number
while real_num > 0 :
    digit = real_num % 10
    palin = (palin*10) + digit
    real_num = real_num // 10 
 
 #This if-else loops helps to compare the two variables   
if temp == palin :
    print("The given number is a palindrome")
else:
    print("Not a palindrome")
    
    