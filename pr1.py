#to find prime number in given range
def is_prime(start, end):
    for val in range(start, end):
        if val > 1:
            for i in range(2, val):
                if val % i == 0:
                    break   # not a prime number
            else:
                print(val)
                
start = int(input("Enter start num: "))
end = int(input("Enter end num: "))
is_prime(start, end)
                        
        