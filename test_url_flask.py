from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import TextAreaField
import ShortURL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'our very hard to guess secretfir'

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

        print(title)
        return "https://newfamily.me/" + ShortURL.create_short_url(url)[1]

        # Validate form data
        if len(title) == 0 or len(url) == 0:
            # Form data failed validation; try again
            error = "Please supply both title and url"
        else:
            # Form data is valid; move along
            return redirect(url_for('thank_you'), keys=title)

    # Render the sign-up page
    return render_template('sign-up.html', message=error)



# Run the application
app.run(debug=False)