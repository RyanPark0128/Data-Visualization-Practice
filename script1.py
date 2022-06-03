# from flask import Flask, render_template

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template("home.html")


# @app.route('/about/')
# @app.route('/about/<topic>')
# def about(topic=None):
#     return render_template("about.html", topic=topic)


# @app.route("/me")
# def me_api():
#     return {
#         "username": "ryan",
#         "theme": "black",
#     }

from flask import Flask, flash, redirect, render_template, \
    request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(debug=True)
