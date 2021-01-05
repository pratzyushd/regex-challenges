import re

def checkMatch(text):
    regex = "\AHello"
    #\A means match if at the beginning
    if re.match(regex, text):
        return True
    return False


testStrings = ["Hello World", "Hi World", "Hello DC", "Bonjour"]
for i in testStrings:
    print("Checking if string \"",i,"\" matches: ", checkMatch(i))