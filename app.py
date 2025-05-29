from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)
EXCEL_FILE = 'user.xlsx'

# Check if the user credentials match any row in Excel
def check_credentials(username, password):
    if not os.path.exists(EXCEL_FILE):
        return False
    df = pd.read_excel(EXCEL_FILE)
    user_row = df[(df['username'] == username) & (df['password'] == password)]
    return not user_row.empty

# Check if username already exists in Excel
def user_exists(username):
    if not os.path.exists(EXCEL_FILE):
        return False
    df = pd.read_excel(EXCEL_FILE)
    return username in df['username'].values

# Append a new user to the Excel file
def add_user(username, password):
    new_user = pd.DataFrame([[username, password]], columns=['username', 'password'])

    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE)
        df = pd.concat([df, new_user], ignore_index=True)
    else:
        df = new_user

    df.to_excel(EXCEL_FILE, index=False)

# Home route - login page
@app.route('/')
def home():
    return render_template('login.html')

# Login form POST request
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if check_credentials(username, password):
        return render_template('success.html', user=username)
    else:
        return render_template('failure.html')

# Register new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if user_exists(username):
            return "<h3>Username already exists. Try another one.</h3><p><a href='/register'>Go back</a></p>"

        add_user(username, password)
        return render_template('register_success.html')

    return render_template('register.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
