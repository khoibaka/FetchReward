

def compare(first, second):

    # Split the version string into list of integer 
    first_list = [int(i) for i in first.split('.')]
    second_list = [int(i) for i in second.split('.')]
    
    index = 0
    # Repeatedly comparing each number of each list from left to right.
    while index < len(first_list) and index < len(second_list):
        if first_list[index] < second_list[index]:
            return 'before'
        elif first_list[index] > second_list[index]:
            return 'after'
        else:
            index += 1

    # if length first list is longer than second list and what is left have something other than 0
    if len(first_list) > len(second_list) and contain_non_zero(first_list[index:]):
        return 'after'
    elif len(first_list) < len(second_list) and contain_non_zero(second_list[index:]):
        return 'before'
    else:
        return 'equal'

def contain_non_zero(array):
    for element in array:
        if element != 0:
            return True
    return False  

def is_software_version(s):
    for string in s.split('.'):
        if len(string) == 0 or not string.isdecimal():
            return False
    return True