from flask import Flask
  
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return """
    <html>
  <head>
    <title>Tobi's flask</title>
    </head>
    <body>
        <h1>The Adventures of QA</h1>
        <div id="mainContent">
          <p>My QA has a lot of adventures. Yesterday we <a href="about">Made a Flask
</a>, and i made two!</p>
          <p>Here's not a picture of QA:</p>
        </div>
         <div id="sidebar">
             <h2>Buy our stuff!</h2>
             <p>Some of our products include <span class="product">SuperWidgets</span
>, <span class="product">MegaWidgets</span>, and <span class="product">WonderWidgets<
/span>.</p>
         </div>
     </body>
    </html> 
    """
@app.route('/')
@app.route('/about')
def about():
    return """
    <title>"Im about"</title>
    <body> "Guess who this about"</body>
    """
