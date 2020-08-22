import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'some_secret'
messages = []


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    data = []

    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route('/about/<meal_strMeal>')
def about_meal(meal_strMeal):
    meal = {}

    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == meal_strMeal:
                meal = obj

    return render_template("meal.html", meal=meal)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message".format(
            request.form["name"]
        ))
    return render_template("contact.html", page_title="Contact")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Please try again'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

"""
def add_messages(username, message):
    """add messages to message list"""
    messages.append("{}:{}".format(username, message))


@app.route('/')
def msg():
    """Main page for instructions"""
    return "to send a message us/USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    """display chat message"""
    return "Welcome, {0}, {1}".format(username, messages)


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message an redirect to chat page"""
    add_messages(username, message)
    return redirect('/' + username)

"""
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
