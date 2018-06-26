"""A madlib game that compliments its users."""

from random import sample, randint, choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

MADLIBS = ['madlib.html', 'madlib_2.html', 'madlib_3.html']

@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet', methods=["POST"])
def greet_person():
    """Greet user with compliment."""

    player = request.form.get("person")

    random_nums = randint(1, len(AWESOMENESS))

    nice_things = sample(AWESOMENESS, random_nums)

    return render_template("compliment.html",
                           person=player,
                           compliments=nice_things)


@app.route('/game')
def show_madlib_form():
    """yes or no from user"""
    user = request.args.get("answer-game")

    if user == 'yes':
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    name = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adj = request.args.get("adj")
    num = request.args.get("num")
    verb = request.args.get("verb")
    clothes = request.args.getlist("clothes")

    madlib = choice(MADLIBS)

    return render_template(madlib, color=color, noun=noun, person=name,
                           adjective=adj, num=num, verb=verb, clothes=clothes)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
