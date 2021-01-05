import re

def checkMatch(text):
    regex = "^a.*b$"
    #^a means a at beginning, .* means any number of any char in middle, b$
    #means b at end
    if re.search(regex, text):
        return True
    return False


testStrings = ["asdvasdfvd", "aSDFb", "absdfEadasv", "asdiu1234fhcasdb"]
for i in testStrings:
    print("Checking if string \"",i,"\" matches: ", checkMatch(i))