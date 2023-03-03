import re
a = input()
matches = re.sub( "[ ,.]", ":" , a )
print(matches)