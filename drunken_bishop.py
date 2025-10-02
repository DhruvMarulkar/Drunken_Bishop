import time
import random

def drunken_bishop(word,width=17,height=9,delay=0.5):
    data = word.encode("utf-8")
    bits = "".join(f"{b:08b}"for b in data)
    moves = {
        "00":(-1,-1),
        "01":(1,-1),
        "10":(-1,1),
        "11":(1,1)     
    }
    grid = [[0 for _ in range(width)] for _ in range(height)]
    x,y = width //2 , height //2
    start_x,start_y =x,y
    
    symbols = [' ', '.', 'o', '+', '=', '*', 'B', '0', 'X', '@', '%', '&', '#', '/', '^']
    max_visits = len(symbols) - 1

    for i in range(0,len(bits),2):
        step = bits[i:i+2]
        if len(step)<2:
            break
        dx, dy = moves[step]
        
        dx += random.choice([-1, 0, 1])  
        dy += random.choice([-1, 0, 1])
        
        x = max(0,min(width-1,x+dx))
        y = max(0,min(height-1,y+dy))
        grid[y][x]+= 1
        
        print("\033c",end="")
        print(f"Step {i//2+1}/{len(bits)//2} ({step})")
        border = "+"+"-"*width+"+"
        print(border)
        
        for r in range(height):
            line = "|"
            for c in range(width):
                if(c,r) == (start_x,start_y):
                    line += "S"
                elif(c,r)==(x,y):
                    line += "E"
                else:
                    val = grid[r][c]
                    line += symbols[min(val, max_visits)]
            line += "|"
            print(line)
        print(border)
        time.sleep(delay)
        
    print("\033c", end="")
    print("Final Fingerprint:")
    border = "+" + "-" * width + "+"
    print(border)
    for r in range(height):
        line = "|"
        for c in range(width):
            if (c, r) == (start_x, start_y):
                line += "S"
            elif (c, r) == (x, y):
                line += "E"
            else:
                val = grid[r][c]
                line += symbols[min(val, max_visits)]
        line += "|"
        print(line)
    print(border)
    
user_word = input("Enter a word")
drunken_bishop(user_word)