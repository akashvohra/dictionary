import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translator(w):
    
    if w in data:
        return data[w]
    elif w[0] in get_close_matches(w, data.keys())[0]:
        kol = get_close_matches(w, data.keys())[0]
        say = input(f"Do want to Say, {kol} Y/N :")
        if say == "Y" or say == "y":
            return data[kol]
        else:
            return f"{w} not found"
        

con = " "

while(True):
    outcome = input("Enter Here : ")
    print(translator(outcome.lower()))
    con = input("Do want to continue Y/N : ")
    if con == "N" or con == "n":
        break