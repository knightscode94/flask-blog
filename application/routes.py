# import render_template function from the flask module
from flask import render_template
# import the app object from the ./application/__init__.py
from application import app
# define routes for / & /home, this function will be called when these are accessed

blogData = [
    {  
        "name": {"first":"Tobi", "last":"Jackson"},
        "title":"First Post",
        "content":"My first blog post about Flask"
    },
    {   
        "name": {"first":"Tobias", "last":"Jackson"},
        "title":"Second Post",
        "content":"This is even more blog data for Flask lectures"
    }
]

@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Home', posts=blogData)


@app.route('/about')
def about():
 return render_template('about.html', title='About')


@app.route('/login')
def login():
 return render_template('log_in.html', title='Login')


@app.route('/register')
def register():
 return render_template('register.html', title='Register')
