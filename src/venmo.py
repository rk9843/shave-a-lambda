# venmo.py handles collecting the recent payments to be used by tracker.py
from venmo_api import Client


class Transaction:
    def __init__(self, UID, sender, recipient, amount, note):
        self.UID = UID
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.note = note

    def __str__(self):
        return f"TRANSACTION {self.UID}:\n{self.sender} paid {self.recipient} ${self.amount}\n{self.note}\n"


def get_token():
    credentialsFile = open("./credentials/credentials.txt", "r")
    credentials = credentialsFile.read().split('\n')
    credentialsFile.close()

    access_token = Client.get_access_token(username=credentials[0],
                                            password=credentials[1])
    print("My token:", access_token)


def get_transactions(callback_limit=10):
    # print("HI")
    tokenFile = open("/home/ShaveALambda/mysite/credentials/token.txt", "r")
    access_token = tokenFile.read()
    tokenFile.close()
    # print(access_token)
    # Initialize api client using an access-token
    client = Client(access_token=access_token)

    # used to get user profile id
    # my_profile = client.user.get_my_profile()
    # print(my_profile)

    userFile = open("/home/ShaveALambda/mysite/credentials/user.txt", "r")
    userID = int(userFile.read())
    userFile.close()

    # print(userID)
    # print(type(userID))
    transactions_list = client.user.get_user_transactions(user_id=userID, limit=callback_limit)

    recent_transactions = {}
    for transaction in transactions_list:
        if transaction.payment_type == 'pay' and transaction.date_completed >= 1707783676 and transaction.target.username == '':
            # print(transaction)
            t = Transaction(transaction.id,
                            transaction.actor.username,
                            transaction.target.username,
                            transaction.amount,
                            transaction.note
                            )
            recent_transactions[t.UID] = t
    return(recent_transactions)

