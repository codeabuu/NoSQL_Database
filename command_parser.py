#!/usr/bin/python3

def parse_message(data):
    """Return a tuple containing the command, the key, and (optionally) the value cast to the appropriate type."""
    command, key, value, value_type = data.strip().slit(';')
    if value_type:
        if value_type == 'LIST':
            value = value.split(';')
        elif value_type == 'INT':
            value = int(value)
        else:
            value = str(value)
    else:
        value = None
    return command, key, value
