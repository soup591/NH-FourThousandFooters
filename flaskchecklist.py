""" 
We import the Flask class from the flask module, and the 
render_template function so we can use templates.
Additionally, we import "url_for" to find exact locations
of routes for us.
"""

from flask import Flask, render_template, url_for, flash, redirect
from mountain_dictionary import mountains
from forms import RegistrationForm, LoginForm

"""
Set variable "app" to an instance of the Flask class.
__name__ is a special variable in Python that just means 
the name of the module. It can be equal to "__main__".
Basically, this is so Python knows where to look for your
 templates, static files, etc. 
 """

app = Flask(__name__)

# Create a secret key to securely keep users logged in.
app.config['SECRET_KEY'] = '6d690f9e5a88923bc1ebeecced7d457f'

"""
Created a function to return various strings for difficulty depending 
the rating it was given in the dictionary.
"""

# We use the .route decorator to set destination for various 
# pages in Flask. Below, the "/" and "/home/" parameters are for the home page.
@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html", mountains=mountains)

# About page route decorator.
@app.route("/about/")
def about_info():
    return render_template("about.html")

@app.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success',)
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login/", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@tracker.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

# Basically, this if statement will run the debugger aka
# be able to dynamically update webpage if you are using python.
# If not, find out what you need to do to change this to work.
if __name__ == '__main__':
    app.run(debug=True)