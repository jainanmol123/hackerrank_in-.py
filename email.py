import re 
for i in range(int(input())):
    name,email=input().split()
    if re.match(r'<[a-zA-Z](\w|-|_|\.)+@[a-zA-Z]+\.[a-zA-Z]{1,3}>',email):
        print(name,email)

