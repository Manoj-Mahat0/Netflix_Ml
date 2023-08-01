from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace 'your_secret_key' with a strong secret key.

# Sample user data for demonstration purposes.
# In a real application, you would use a database to store and manage user information.
users = {
    'user1': {'password': 'pass123'},
    'user2': {'password': 'test456'}
}

@app.route('/')
def landing():
    if 'username' in session:
        return render_template('landing.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('landing'))
        else:
            return render_template('login.html', error='Invalid credentials. Please try again.')
    else:
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = {'password': password}
            session['username'] = username
            return redirect(url_for('landing'))
        else:
            return render_template('signup.html', error='Username already exists. Please choose a different username.')
    else:
        return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
