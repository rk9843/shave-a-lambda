from flask import Flask, flash, render_template, request, redirect, url_for
import transactions, db, logging

app = Flask(__name__)


@app.route('/')
def index():
    balance_data = transactions.main()
    # balance_data = db.get_balance()

    # print(balance_data)
    # print(type(balance_data))
    balance_data.pop(-1)
    # print(balance_data)
    logging.info(balance_data)

    top_three = db.top_three()
    return render_template('index.html', balance_json=balance_data, top3_json = top_three)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name = request.form['name']
        team = request.form['team']
        amount = request.form['amount']
        db.update_money(name, amount, team)
        return redirect(url_for('admin'))
    else:
        return render_template('admin.html')


def setup():
    db.create_table()

def benis():
    db.show_table()
    a = db.top_three()
    print('a', a)
    db.get_balance()
