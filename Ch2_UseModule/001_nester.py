'''
This the "nester.py" module and it provides one function called print_lol() which prints lists that may or may not include nested lists.
'''
def print_lol(listData):
    """
    This is the Standard way to include a multiple-line comment in your code
    """
    for item in listData:
        if (isinstance(item, list)):
            print_lol(item)
        else:
            print(item)

#look Nester Folder