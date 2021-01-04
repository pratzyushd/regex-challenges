import re

def checkMatch(text):
    regex = "^ab{3,3}$"
    #Requires ^ and $ chars at begin and end so that only if this is the exact
    #string, otherwise "abbbbbbbb" is a match
    if re.match(regex, text):
        return True
    return False


testStrings = ["abbb", "abb", "b","abbbbbbbbbb"]
for i in testStrings:
    print("Checking if string \"",i,"\" matches: ", checkMatch(i))