'''
This the "nester.py" module and it provides one function called print_lol() which prints lists that may or may not include nested lists.
'''
def print_lol(the_list):
    '''
    This is the Standard way to include a multiple-line comment in your code
    '''
    for each_item in the_list:
        if (isinstance(each_item, list)):
            print_lol(each_item)
        else:
            print(each_item)