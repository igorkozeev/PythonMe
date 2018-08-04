import re

phoneNumRegex = re.compile(r'\d\d\d\-\d\d\d-\d\d\d\d')
#mo = phoneNumRegex.search('''Call me 415-555-1011 tomorrow, or 415-555-9999
#for my office line''')
#print(mo.group())

# Here is a way to print all matches in text

print(phoneNumRegex.findall('''Call me 415-555-1011 tomorrow, or 415-555-9999
for my office line'''))
