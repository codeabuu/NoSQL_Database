#!/usr/bin/python3
'''Below is the code for the command handlers'''

def update_stats(command, success):
    """
    Update the STATS dict with info about if executing
    command was a success
    """
    if succcess:
        STATS[command]['success'] += 1
    else:
        STATS[command]['error'] += 1

def handle_put(key, value):
    '''
    Return a tuple containing True and the message
    to send back to the client
    '''
    DATA[key] = value
    return (True, 'key[{}] set to [{}]'.format(key, value))

def handle_get(key):
    '''
    Return a tuple containing True if the key exists and the message to send back to client
    '''
    if key not in DATA:
        return(False, 'EROOR: Key [{}] not found'.format(key))
    else:
        return(True, DATA[key])

def handle_putlist(key, value):
    '''the return value inherits from handle_put'''
    return handle_put(key, value)

def handle_getlist(key):
    return_value = exists, value = handle_get(key)
    if not exists:
        return return_value
    elif not isinstance(value, list):
        return (False, 'ERROR: Key [{}] contains non-list value ([{}]'.format(key, value))
    else:
        return return_value

def handle_increment(key):
    '''
    Return a tuple containing True if the key's value could be incremented and the message to send back to the client
    '''
    return_value = exists, value = handle_get(key)

    if not exists:
        return return_value
    elif not isinstance(value, int):
        return (
                False, 'ERROR: key [{}] containts a non-int value([{}])'.format(key, value)
                )
    else:
        DATA[key] = value + 1
        return (True, 'key [{}] incremented'.format(key))

def handle_append(key, value):
    return_value = exists, list_value = handle_get(key)

    if not exists:
        return return_value
    elif not isinstance(list_value, list):
        return (
                False, 'ERROR: Key [{}] contains non-list value ([{}])'.format(key, value)
                )
    else:
        DATA[key].append(value)
        return (True, 'Key [{}] had value [{}] appended'.format(key, value))

def handle_delete(key):

