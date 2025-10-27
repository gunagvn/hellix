with open("hi.txt",'r') as file :
    words = 0
    characters = 0
    lines = 0 
    
    for line in file :
        lines = lines + 1
        characters = characters + len(line)
        words = words + len(line.split())
        
    print("Number of lines:", lines)    
    print("Number of words:", words)
    print("Number of characters:", characters)
        
        