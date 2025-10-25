a = input("Enter first person's name:")
b = input("Enter second person's name:")
c = input("Enter third person's name:")
d = input("Enter four person's name:")
e = input("Enter five person's name:")
vow_list = []
vow_col = "aeiou"
if a[0] in vow_col:
    vow_list.append(a)   
if b[0] in vow_col:
    vow_list.append(b)    
if c[0] in vow_col:
    vow_list.append(c)   
if d[0] in vow_col:
    vow_list.append(d)    
if e[0] in vow_col:
    vow_list.append(e)
                        
print("The needed names are:",vow_list)    

''' The logic is we have to get 5 input names from user and have to store only the names starts with 
vowels in a new list'''

'''So i'm getting the 5 input names from user and created one new empty list'''

'''Then we have to create one variable to store the vowel words, then we will 