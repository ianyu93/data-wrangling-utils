import re
from IPython.display import Markdown, display
from unidecode import unidecode 
from ftfy import fix_text

def normalize_text(text):
    '''
    Normalize text through NFKC and unicode
    '''
    text = unidecode(fix_text(text, normalization='NFKC'))
    text = re.sub('<.*?>','',text)
    return text.replace('\\','')

def printmd(string):
    '''
    Prints string in Markdown
    '''
    display(Markdown(string))

def replace_all(text, dict):
    '''
    Given a text and replacement dictionary, performs multiple str.replace()

    Arguments:
    ==========
    text: str, text to perform str.replace()
    dic: dict, where each key is the replacement and each value is a list of strings to be replaced
    '''
    for key, value in dict.items():
        for v in value:
            text = text.replace(v, key)
    return text

def flatten(t):
    '''
    Flatten a nested list
    '''
    return [item for sublist in t for item in sublist]

def break_nest(x):
    '''
    Braek nested list or tuple into a flat list
    '''
    while all(isinstance(y, (list, tuple)) for y in x):
        x = flatten(x)
    return x

def find_columns(df, pat, normalize=False):
    '''
    Match pandas DataFrame column and value counts based on RegEx
    '''
    for col in df.columns:
        if re.search(pat, col):
            print(col)
            print(df[col].fillna('n/a').value_counts(normalize=normalize))
            print('\b')
        else:
            continue

