#!/usr/bin/python3
def search_replace(my_list, search, replace):

    '''
        A fnct that traverse through a list for an elmt that matches
        search & modify it with replace then returns a new list
        @elem: Elements
    '''

    if len(my_list) == 0:
        return my_list

    new_list = [elem if elem != search else replace for elem in my_list]
    return new_list
