from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import TextAreaField
import ShortURL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ask me do not as a farm okay'
domain = 'www.setgot.com'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:url>')
def goto_url(url):
    url = ShortURL.get_real_url(url)[0]
    return render_template('new-url.html', goto=url)


# Simple form handling using raw HTML forms
@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        title = request.form['title']
        url = request.form['url']

        if len(title) == 0 or len(url) == 0:
            error = "Please supply both title and url"
        else:
            return "https://" + domain + "/" + ShortURL.create_short_url(url, title)[1]
    return render_template('sign-up.html', message=error)


# Run the application
app.run(debug=False)