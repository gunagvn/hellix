#to print right angle triangle pattern
n = int(input("Enter number of rows: "))
#outer loop for no of rows
for i in range(1, n+1):
    #inner loop is for printing stars
    for j in range(1, i+1):
        print("*", end="")
    