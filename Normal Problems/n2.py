import re

def checkMatch(text):
    regex = "ab*" #Insert regex here
    if re.match(regex, text):
        return True
    return False


testStrings = ["a", "b", "abbbbbb", "ab"] #Insert test string here
for i in testStrings:
    print("Checking if string \"",i,"\" matches: ", checkMatch(i))