from flask import Flask, render_template, request
from helpers import acct_pwd
from operator import attrgetter

app: Flask = Flask(__name__)

account_list: list[acct_pwd] = []
    
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/encrypt-password', methods=["GET", "POST"])
def create_todo():
    if request.method == "POST":
        global account_list

        account: str = request.form['account']
        password: str = request.form['password']

        if account == '':
            return render_template("encrypt-password.html", acct_valid=False, pwd_valid=False)

        elif password == '':
            return render_template("encrypt-password.html", acct_valid=True, pwd_valid=False)
        new_acct: acct_pwd = acct_pwd(account, password)
        account_list.append(new_acct)
        account_list = sorted(account_list, key=attrgetter("lower_account"))

        return render_template("success.html", account=account, password=password)
    return render_template("encrypt-password.html", acct_valid=True, pwd_valid=True)

@app.route('/view-list')
def view_account_list():
    return render_template('view-list.html', account_list=account_list)

if __name__ == '__main__':
    app.run(debug=True)