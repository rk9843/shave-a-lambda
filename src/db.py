import sqlite3, logging

def create_table():
    try:
        connection = sqlite3.connect('/home/ShaveALambda/mysite/database.db')
        cursor = connection.cursor()
        logging.info("Successfully Connected to SQLite")

        with open('/home/ShaveALambda/mysite/create_table.sql', 'r') as create_table_script:
            create_table = create_table_script.read()

        cursor.executescript(create_table)
        logging.info("Table created successfully")
        cursor.close()
    except sqlite3.Error as error:
        logging.error("Error while creating a sqlite table{}".format(error))
    finally:
        if connection:
            connection.close()
            logging.info("sqlite connection is closed")


def update_table(valid_transactions):
    try:
        connection = sqlite3.connect('/home/ShaveALambda/mysite/database.db')
        cursor = connection.cursor()
        logging.info("Successfully Connected to SQLite")

        for transactions in valid_transactions:
            update_table_query = """INSERT INTO transactions (UUID, sender, recipient, amount, note)
                                    VALUES (?, ?, ?, ?, ?);"""

            transaction_data = (valid_transactions[transactions].UID,
                                valid_transactions[transactions].sender,
                                valid_transactions[transactions].recipient,
                                valid_transactions[transactions].amount,
                                valid_transactions[transactions].note)
            cursor.execute(update_table_query, transaction_data)

        connection.commit()
        logging.info("Records inserted successfully")
        cursor.close()
    except sqlite3.Error as error:
        logging.error("Error while inserting records{}".format(error))
    finally:
        if connection:
            connection.close()
            logging.info("sqlite connection is closed")


def show_table():
    try:
        connection = sqlite3.connect('/home/ShaveALambda/mysite/database.db')
        cursor = connection.cursor()
        logging.info("Successfully Connected to SQLite")

        show_table_query = """SELECT * FROM transactions"""
        cursor.execute(show_table_query)
        output = []
        for row in cursor:
            logging.info(row)
            output.append(row)

        connection.commit()
        logging.info("Record Obtained successfully")
        connection.close()
        return output
    except sqlite3.Error as error:
        logging.error("Error while obtaining records{}".format(error))
    finally:
        if connection:
            connection.close()
            logging.info("The SQLite connection is closed")


def get_UUID():
    try:
        connection = sqlite3.connect('/home/ShaveALambda/mysite/database.db')
        cursor = connection.cursor()
        logging.info("Successfully Connected to SQLite")

        get_UUID_query = """SELECT UUID FROM transactions;"""
        cursor.execute(get_UUID_query)
        rows = cursor.fetchall()
        result = [i[0] for i in rows]
        logging.info(result)

        connection.commit()
        logging.info("Record Obtained successfully")
        cursor.close()
        return result
    except sqlite3.Error as error:
        logging.error("Error while obtaining records{}".format(error))
        return None
    finally:
        if connection:
            connection.close()
            logging.info("sqlite connection is closed")

def update_balance(balance):
    try:
        connection = sqlite3.connect('/home/ShaveALambda/mysite/database.db')
        cursor = connection.cursor()
        logging.info("Successfully Connected to SQLite")

        for teams in balance:
            update_table_query = """UPDATE balance SET money_raised = money_raised + ? WHERE team_name IN (?);"""
            query_data = (round(float(balance[teams]), 2), teams)
            cursor.execute(update_table_query, query_data)

        connection.commit()
        logging.info("Records inserted successfully")
        cursor.close()
    except sqlite3.Error as error:
        logging.error("Error while inserting records{}".format(error))
    finally:
        if connection:
            connection.close()
            logging.info("sqlite connection is closed")

def get_balance():
    try:
        connection = sqlite3.connect('/home/ShaveALambda/mysite/database.db')
        cursor = connection.cursor()
        logging.info("Successfully Connected to SQLite")
        get_UUID_query = """SELECT * FROM balance;"""
        cursor.execute(get_UUID_query)
        rows = cursor.fetchall()

        result = {}
        for i in rows:
            result[i[1]] = i[2]
        print(result)
        connection.commit()
        logging.info("Record Obtained successfully")
        cursor.close()
        return result
    except sqlite3.Error as error:
        logging.error("Error while obtaining records{}".format(error))
        return None
    finally:
        if connection:
            connection.close()
            logging.info("sqlite connection is closed")



def top_three():
    try:
        connection = sqlite3.connect('/home/ShaveALambda/mysite/database.db')
        cursor = connection.cursor()
        logging.info("Successfully Connected to SQLite")
        # get_three_query = """SELECT * FROM transactions ORDER BY amount DESC LIMIT 3;"""

        get_three_query = """SELECT sender, SUM(amount) as total_amount FROM transactions GROUP BY sender ORDER BY total_amount DESC LIMIT 3;"""
        # get_three_query = """SELECT sender, SUM(amount) AS total_amount FROM transactions GROUP BY sender ORDER BY total_amount DESC LIMIT 3;"""
        cursor.execute(get_three_query)
        rows = cursor.fetchall()

        result = {}
        j = 1
        for i in rows:
            print(i)
            result[j] = (i[0], round(i[1],2))
            j += 1

        print(result)
        connection.commit()
        logging.info("Record Obtained successfully")
        cursor.close()
        return result
    except sqlite3.Error as error:
        logging.error("Error while obtaining records{}".format(error))
        return None
    finally:
        if connection:
            connection.close()
            logging.info("sqlite connection is closed")


def update_money(name, amount, team):
    try:
        connection = sqlite3.connect('/home/ShaveALambda/mysite/database.db')
        cursor = connection.cursor()
        logging.info("Successfully Connected to SQLite")

        query = """UPDATE balance SET money_raised = money_raised + ? WHERE team_name = ?;"""

        param = (amount, team)
        cursor.execute(query, param)

        connection.commit()

        logging.info("Records inserted successfully: {} donated {} to team {}.".format(name, amount, team))
        cursor.close()
    except sqlite3.Error as error:
        logging.error("Error while obtaining records{}".format(error))
        return None
    finally:
        if connection:
            connection.close()
            logging.info("sqlite connection is closed")

def debug():
    try:
        connection = sqlite3.connect('/home/ShaveALambda/mysite/database.db')
        cursor = connection.cursor()
        logging.info("Successfully Connected to SQLite")
        query = """SELECT * FROM balance;"""
        # query = """SELECT * FROM transactions;"""
        
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        connection.commit()
        logging.info("Record Obtained successfully")
        cursor.close()
        return result
    except sqlite3.Error as error:
        logging.error("Error while obtaining records{}".format(error))
        return None
    finally:
        if connection:
            connection.close()
            logging.info("sqlite connection is closed")


