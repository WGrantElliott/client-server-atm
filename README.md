# client-server-atm
This program is designed to work using the logic of an ATM. The user will enter a command into the terminal followed by an amount, these values then get sent to the server. The server keeps track of a balance which is initially 100. When the server receives a request, it will check to see if the balance needs to be updated or returned (in the case of ‘check balance’). If the command from the user is to withdraw money, the server checks to make sure the withdrawal request is less than or equal to the current balance. If it is not, the server returns a message letting the user know they have insufficient funds. When the user types ‘exit’, the client program is exited. The server side will stay running and can accept another connection. To stop running the server side type ctrl+c.

Steps to run:
    1. Run the server program first (python3 server.py)
    2. Run the client program       (python3 client.py)
    3. Enter your input commands, type exit to quit
