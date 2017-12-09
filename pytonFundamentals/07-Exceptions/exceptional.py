'''A module for demonstrating exceptions'''

def convert(s):
    '''Convert to integer'''
    
    x = -1
    
    try:
        x = int(s)
        print("Conversion succeeded: x = ", x)
    except (ValueError, TypeError):
        print("Conversion failed")
    
    return x