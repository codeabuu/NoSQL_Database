#!/usr/bin/python3
import socket

# Define the server's address and port
SERVER_HOST = "localhost"
SERVER_PORT = 50505

def send_request(command, key, value=None):
    # Create a socket object using IPv4 and TCP protocol
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Construct the message in the format: "command;key;value"
    message = f"{command};{key}"
    if value is not None:
        message += f";{value}"

    # Send the message to the server
    client_socket.sendall(message.encode())

    # Receive the server's response
    response = client_socket.recv(4096).decode()

    # Close the client socket
    client_socket.close()

    return response

if __name__ == "__main__":
    while True:
        print("Choose an operation:")
        print("1. PUT")
        print("2. GET")
        print("3. INCREMENT")
        print("4. DELETE")
        print("5. GETLIST")
        print("6. PUTLIST")
        print("7. APPEND")
        print("8. STATS")
        print("9. Exit")

        choice = input("Enter the operation number: ")

        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            response = send_request("PUT", key, value)
            print(response)

        elif choice == '2':
            key = input("Enter key: ")
            response = send_request("GET", key)
            print(response)

        elif choice == '3':
            key = input("Enter key: ")
            response = send_request("INCREMENT", key)
            print(response)

        elif choice == '4':
            key = input("Enter key: ")
            response = send_request("DELETE", key)
            print(response)

        elif choice == '5':
            key = input("Enter key: ")
            response = send_request("GETLIST", key)
            print(response)

        elif choice == '6':
            key = input("Enter key: ")
            value = input("Enter value (semicolon-separated list): ")
            response = send_request("PUTLIST", key, value)
            print(response)

        elif choice == '7':
            key = input("Enter key: ")
            value = input("Enter value to append: ")
            response = send_request("APPEND", key, value)
            print(response)

        elif choice == '8':
            response = send_request("STATS", "")
            print(response)

        elif choice == '9':
            print("Exiting the client.")
            break

        else:
            print("Invalid choice. Please choose a valid operation.")

