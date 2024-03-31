import re

def increment_string(string):
    # Regular expression to match the number at the end of the string
    match = re.search(r'(\d*)$', string)
    
    if match:
        # If a number is found, increment it by 1
        num = str(int(match.group(1)) + 1)
        # Format the string with the incremented number
        return string[:match.start()] + num
    else:
        # If no number is found, append '1' to the string
        return string + '1'




print(increment_string("foo12"))
print(increment_string("foo6"))
print(increment_string("foo2"))