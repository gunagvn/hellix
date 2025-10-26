n = int(input("Enter numbers:"))
val = 0

while n>0 :
        digit = n % 10
        val = (val*10)+digit
        n = n // 10
        
print("The reversed numbers:",val)    