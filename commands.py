#!/usr/bin/python3
""""importing socket module for network socket operations"""
import socket

"""Define constants for the host and port to be used"""
HOST = "localhost"
PORT ='50505'

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

COMMAND_HANDLERS = {
        'PUT': handle_put,
        'GET': handle_get,
        'GETLIST': handle_getlist,
        'PUTLIST': handle_putlist,
        'INCREMENT': handle_increment,
        'APPEND': handle_append,
        'DELETE': handle_delete,
        'STATS': handle_stats,
        }
DATA = {}

def main():
    SOCKET.bind((HOST, PORT))
    SOCKET.listen(1)

    while 1:
        connection, address = SOCKET.accept()
        print ("New connection from [{}]".format(address))
        data = connection.recv(4096).decode()
        command, key, value = parse_msg(data)

        if command == 'STATS':
            response = handle_stats()
        elif command in (
                'GET',
                'GETLIST',
                'INCREMENT',
                'DELETE',
                ):
            response = COMMAND_HANDLERS[command](key)
        elif command in (
                'PUT',
                'PUTLIST',
                'APPEND',
                ):
            response = COMMAND_HANDLERS[command](key, value)
        else:
            response = (FALSE, 'Unknown command [{}]'.format(command))
        update_stats(command, response[0])
        connection.sendall('{};{}'.format(response[0], response[1]))

if __name__ == "__main__":
    main()
