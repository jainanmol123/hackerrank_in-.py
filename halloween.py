
import sys

def howManyGames(p, d, m, s):
    if p>s:
        return(0)
    games=1
    s-=p
    while(s>=p):
        if((p-d)>m):
            p=p-d
        else:
            
            p = m
        
        games+=1
        s=s-p
    return(games)    
        
        
    # Return the number of games you can buy

if __name__ == "__main__":
    p, d, m, s = input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print(answer)
