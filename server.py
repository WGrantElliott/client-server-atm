"""William Elliott
   September 6, 2021
   This program is supposed to mimic the functionality of an ATM, this will keep track of the current dollar amount
"""

import socket

HOST = '127.0.0.1'
PORT = 65432
num = 0

"""initialize balance"""
balance = 100


def update_balance(update_command):
    global balance
    print(update_command, "request recieved")

    if update_command == 'deposit':
        """receive the deposit amount"""
        data = conn.recv(1024)
        deposit_amount = str(data, 'utf8')
        balance += int(deposit_amount)
        statement = 'New balance is: ' + str(balance)
    elif update_command == 'withdraw':
        """receive withdraw amount"""
        data = conn.recv(1024)
        deposit_amount = str(data, 'utf8')
        """Check to make sure the requested balance is less than or equal to current balance"""
        if int(deposit_amount) <= balance:
            balance -= int(deposit_amount)
            statement = 'New balance is: ' + str(balance)
        else:
            statement = 'That is an invalid amount. please enter an amount less than:' + str(balance)
    elif update_command == 'check balance':
        """Do not receive an additional input, just return current balance"""
        statement = 'Your current balance is ' + str(balance)
    return statement


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    conn, addr = s.accept()
    print('connected by', addr)
    with conn:
        while True:
            """withdraw,deposit, or check balance"""
            data = conn.recv(1024)
            if not data:
                break
            string = str(data, 'utf8')
            """update the balance and store the string returned"""
            return_statement = update_balance(string)
            print(return_statement)
            """Send the string back to the client"""
            return_statement = return_statement.encode()
            conn.sendall(return_statement)
