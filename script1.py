from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
@app.route('/about/<topic>')
def about(topic=None):
    return render_template("about.html", topic=topic)


if __name__ == "__main__":
    app.run(debug=True)
