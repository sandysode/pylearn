import json
data = json.load(open('data.json'))

def sandra(d):
    if sandra in data:
        d = d.lower
    return data[d]
write = input("Enter your name: ")
print(sandra(write))

