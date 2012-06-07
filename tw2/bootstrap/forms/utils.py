'''
Created on 29.05.2012

@author: moschlar
'''


def replace_all(text, items):
    '''Replaces all old, new tuples from items in text

    items may be a dict of {old: new} pairs
    or a list of (old, new) tuples
    '''
    try:
        items = items.iteritems()
    except:
        pass
    for old, new in items:
        text = text.replace(old, new)
    return text