"""William Elliott
   September 6, 2021
   This program is supposed to mimic the client interaction with an ATM, which allows the user to deposit, withdraw, check balance, or exit
"""

import socket
import time

HOST = '127.0.0.1'
PORT = 65432
input_command = ''


def update_statement(command):
    initial_statement = 'Input amount to ' + command + ' :'
    input_amount = input(initial_statement)
    """Make sure the input value is an int"""
    try:
        update_value = int(input_amount)
        """Make sure value is greater than zero"""
        if update_value < 0:
            print("Please enter a number greater than zero")
        else:
            """Send the command (withdraw or deposit)"""
            update = command.encode()
            s.sendall(update)
            """Allow time for the whole message to be transmitted"""
            time.sleep(.1)
            """Send the amount to deposit or withdraw"""
            input_amount = input_amount.encode()
            s.sendall(input_amount)
            """Receive string statement from server"""
            data = s.recv(1024)
            returned_statement = str(data, 'utf8')
            print(returned_statement)
    except ValueError:
        print("Please enter a number")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while input_command != 'exit':
        input_command = input('Input Command (deposit, withdraw, check balance, exit): ')
        input_command = input_command.lower()
        if (input_command == 'deposit') or (input_command == 'withdraw'):
            update_statement(input_command)
        elif input_command == 'check balance':
            """Send request to check balance"""
            input_command = input_command.encode()
            s.sendall(input_command)
            """Receive string statement from server"""
            data = s.recv(1024)
            returned_statement = str(data, 'utf8')
            print(returned_statement)
        elif input_command == 'exit':
            print("Goodbye")
        else:
            print("Please enter a valid input (deposit, withdraw, check balance, exit)")
