# tracker.py collects venmo data and updates the respective pools
# import matplotlib.pyplot as plt
import venmo, db


KEYWORDS = { 1 : ("1"),
          2 : ("2"),
          3 : ("3"),
          }

def get_transactions(last_N=25):
    recent_transactions = venmo.get_transactions(last_N)  # List of last N-1 transactions
    return(recent_transactions)

def validate_transactions(transactions):
    past_transactions = db.get_UUID()
    valid_transactions = {}
    for items in transactions:
        if int(items) not in past_transactions and int(transactions[items].UID) >= 3994820000000000000:
            valid_transactions[items] = transactions[items]
    return(valid_transactions)

def identify_teams(valid_transactions):
    balance = { 1 : 0,
            2 : 0,
            3 : 0,
            -1 : 0
           }
    for transaction in valid_transactions:
        team = -1
        note = valid_transactions[transaction].note.upper()
        if any(kw in note for kw in KEYWORDS[1]):
            team = 1
        elif any(kw in note for kw in KEYWORDS[2]):
            team = 2
        elif any(kw in note for kw in KEYWORDS[3]):
            team = 3
        # if not team == -1:
        balance[team] += round(valid_transactions[transaction].amount, 2)
    return balance


def main():
    recent_transactions = get_transactions(250)
    valid_transactions = validate_transactions(recent_transactions)
    db.update_table(valid_transactions)
    balance = identify_teams(valid_transactions)
    db.update_balance(balance)
    results = db.get_balance()
    return results

def debug():
    db.get_balance()

