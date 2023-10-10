#!/usr/bin/python3
"""importing socket module for network socket operations"""
import socket
from command_parser import parse_message
from commands_h import CommandHandlers

"""Define constants for the host and port to be used"""
HOST = ""
PORT = 50505 # Changed to an integer

'''Create a socket object using IPv4 and TCP protocol'''
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

'''Define a dictionary 'STATS' to keep track of various statistics for different operations'''
STATS = {
    'PUT': {'success': 0, 'error': 0},
    'GET': {'success': 0, 'error': 0},
    'GETLIST': {'success': 0, 'error': 0},
    'PUTLIST': {'success': 0, 'error': 0},
    'INCREMENT': {'success': 0, 'error': 0},
    'APPEND': {'success': 0, 'error': 0},
    'DELETE': {'success': 0, 'error': 0},
    'STATS': {'success': 0, 'error': 0},
}

# Define COMMAND_HANDLERS after importing CommandHandlers class
COMMAND_HANDLERS = {
    'PUT': CommandHandlers.handle_put,
    'GET': CommandHandlers.handle_get,
    'GETLIST': CommandHandlers.handle_getlist,
    'PUTLIST': CommandHandlers.handle_putlist,
    'INCREMENT': CommandHandlers.handle_increment,
    'APPEND': CommandHandlers.handle_append,
    'DELETE': CommandHandlers.handle_delete,
    'STATS': CommandHandlers.handle_stats,
}
DATA = {}


def main():
    SOCKET.bind((HOST, PORT))
    SOCKET.listen(1)

    while 1:
        connection, address = SOCKET.accept()
        print("New connection from [{}]".format(address))
        data = connection.recv(4096).decode()
        command, key, value = parse_message(data)  # Changed 'parse_msg' to 'parse_message'

        if command == 'STATS':
            response = CommandHandlers.handle_stats()
        elif command in ('GET', 'GETLIST', 'INCREMENT', 'DELETE'):
            response = COMMAND_HANDLERS[command](key)
        elif command in ('PUT', 'PUTLIST', 'APPEND'):
            response = COMMAND_HANDLERS[command](key, value)
        else:
            response = (False, 'Unknown command [{}]'.format(command))
        CommandHandlers.update_stats(command, response[0])  # Changed 'update_stats' to 'CommandHandlers.update_stats'
        connection.sendall('{};{}'.format(response[0], response[1]))

if __name__ == "__main__":
    main()
