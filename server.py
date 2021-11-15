"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
  """Home page."""
    # <a href="localhost.5000/hello">Come say Hi!</a>
    # <button onclick="myFunction()">Click me</button>

  return """<!doctype html>
                <html>
                    <body>Hi! This is the home page. 
                      <a href="/hello">Come say Hi!</a>
                    </body>
                </html>"""
  # return redirect('/hello')

# <select name="pets" id="pet-select">
#     <option value="">--Please choose an option--</option>
#     <option value="dog">Dog</option>
#     <option value="cat">Cat</option>
#     <option value="hamster">Hamster</option>
#     <option value="parrot">Parrot</option>
#     <option value="spider">Spider</option>
#     <option value="goldfish">Goldfish</option>
# </select>
@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
          <select name="compliments">
            <option value="awesome">Awesome</option>
            <option value="terrific">Terrific</option>
            <option value="fantastic">Fantastic</option>
            <option value="neato">Neato</option>
          </select>
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliments")

    # compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
