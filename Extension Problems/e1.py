import re

def checkMatch(text):
    regex = "^[a-zA-z0-9]+$"
    # ^ and $ characters show beginning and end of string, meaning that the
    # string must contain only one or more of the specified set within it
    if re.match(regex, text):
        return True
    return False


testStrings = ["abbasdfluasdfc", "123487", "ASDFB", "ASDVlkjahsdfaAJS123agD", "?", "abcd!"]
for i in testStrings:
    print("Checking if string \"",i,"\" matches: ", checkMatch(i))