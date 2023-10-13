import json
sandra = json.load(open('data.json'))

def skylar(s):
     if s in sandra:
         s = s.lower
         return sandra[s]

write = input("Enter your value: ")
print(skylar(write))

