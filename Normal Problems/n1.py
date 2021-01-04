import re

def checkMatch(text):
    regex = "ab+"
    if re.match(regex, text):
        return True
    return False


testStrings = ["a", "ab", "b", "abbbb"]
for i in testStrings:
    print("Checking if string \"",i,"\" matches: ", checkMatch(i))