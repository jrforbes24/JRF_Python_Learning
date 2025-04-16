#! python3
import re
import pyperclip

# Create a regex for phone number
phoneRegex = re.compile(r'''
# possible phone number formats 415-555-1234, 555-2356, (555) 415-1234, (800) 555-1234 ext 1234, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?  # area code (optional)
(\s|-)                        # first separator
\d\d\d                        # first 3 digits
-                             # second separator
\d\d\d\d                      # last 4 digits
((ext(\.)?\s|x)              # extension word part (optional) 
 (\d{2,5} ))? 
 )                            # extension number part (optional)                        
''', re.VERBOSE)

# Create a regex for emails
emailRegex = re.compile(r'''
# possible email format some.+_thing@somedomain.com                        
[a-zA-Z0-9_.+]+  # name part
@                # @ get it
[a-zA-Z0-9_.+]+  # domain name part
''',re.VERBOSE)

# Get the text of the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhoneNumbers = phoneRegex.findall(text)
extractedEmails = emailRegex.findall(text)

allPhoneNumbers = []
for phone in extractedPhoneNumbers:
    allPhoneNumbers.append(phone[0])
# print(extractedEmails)
# print(allPhoneNumbers)


#TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmails)
pyperclip.copy(results)