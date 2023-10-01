#!/usr/bin/python3
'''Below is the code for the command handlers'''

class CommandHandlers:
    def __init__(self):
        self.DATA = {}
        self.STATS = {}

    def update_stats(self, command, success):
        """
        Update the STATS dict with info about if executing
        command was a success
        """
        if success:
            self.STATS[command]['success'] += 1
        else:
            self.STATS[command]['error'] += 1

    def handle_put(self, key, value):
        '''
        Return a tuple containing True and the message
        to send back to the client
        '''
        self.DATA[key] = value
        return (True, 'key[{}] set to [{}]'.format(key, value))

    def handle_get(self, key):
        '''
        Return a tuple containing True if the key exists and the message to send back to client
        '''
        if key not in self.DATA:
            return (False, 'ERROR: Key [{}] not found'.format(key))
        else:
            return (True, self.DATA[key])

    def handle_putlist(self, key, value):
        '''the return value inherits from handle_put'''
        return self.handle_put(key, value)

    def handle_getlist(self, key):
        return_value = exists, value = self.handle_get(key)
        if not exists:
            return return_value
        elif not isinstance(value, list):
            return (False, 'ERROR: Key [{}] contains non-list value ([{}]'.format(key, value))
        else:
            return return_value

    def handle_increment(self, key):
        '''
        Return a tuple containing True if the key's value could be incremented and the message to send back to the client
        '''
        return_value = exists, value = self.handle_get(key)

        if not exists:
            return return_value
        elif not isinstance(value, int):
            return (
                False, 'ERROR: key [{}] contains a non-int value([{}])'.format(key, value)
            )
        else:
            self.DATA[key] = value + 1
            return (True, 'key [{}] incremented'.format(key))

    def handle_append(self, key, value):
        return_value = exists, list_value = self.handle_get(key)

        if not exists:
            return return_value
        elif not isinstance(list_value, list):
            return (
                False, 'ERROR: Key [{}] contains non-list value ([{}])'.format(key, value)
            )
        else:
            self.DATA[key].append(value)
            return (True, 'Key [{}] had value [{}] appended'.format(key, value))

    def handle_delete(self, key):
        if key not in self.DATA:
            return (False, 'ERROR: Key [{}] not found and could not be deleted'.format(key))
        else:
            del self.DATA[key]

    def handle_stats(self):
        return (True, str(self.STATS))
