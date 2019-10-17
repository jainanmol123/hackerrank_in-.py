import re 
for i in range(int(input())):
    s=''.join(sorted(input()))
    if re.search(r'^[a-zA-Z0-9]{10}$',s)and re.search(r'[A-Z]{2,}',s)and re.search(r'\d{3,}',s) and not re.search(r'(.)\1',s):
        print("Valid")
    else:
        print("Invalid"
               
        
