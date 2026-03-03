from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route('/user/<username>')

def profile(username):

    return render_template('profile.html', user=username)

@app.route('/')

def home():

    return render_template("login.html")

if __name__ == '__main__':

    app.run(debug=True)
usuarios = ['guilherme' 'heloisa']
senhas = [1, 2]
@app.route('/logar', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    session['username'] = username
    if username in usuarios and password in senhas:
        return redirect(url_for('profile'))