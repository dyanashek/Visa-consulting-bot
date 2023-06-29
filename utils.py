import re

def get_name(text):
    '''Gets name from text.'''

    regex = r'(?<=Имя: ).+'
    name = re.search(regex, text)
    if name:
        name = name.group().rstrip(' ')
    
    return name