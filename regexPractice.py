import re
def regexFunc(pattern):
    pattern4Use = re.compile(pattern)

    result = re.search(pattern4Use,"string to search")

    print (result)

pattern = r"^s.*?"
regexFunc(pattern)
