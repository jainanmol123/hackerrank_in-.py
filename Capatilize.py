# Complete the solve function below.
def solve(s):
    p=[]
    S=s.split()
    for i in S:
        p.append(i.capitalize())
    return(" ".join(p))    
        
print(solve("hello   world  lol"))
