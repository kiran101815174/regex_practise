import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''


sentence = 'Start a sentence and then bring it to an end 832 476 876.'

#pattern = re.compile(r'M(r|s|rs)\.?\s+[a-zA-Z]\w*')
#pattern2=re.compile(r'(832|476)')
#pattern3=re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
pattern4=re.compile(r'(http|https)://(www\.)?[a-zA-Z0-9]+\.[a-zA-Z0-9]+')
matches = pattern4.finditer(urls)


for match in matches:
    print(match)
