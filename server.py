from flask import Flask
import random

app = Flask(__name__)
correct_number = random.randint(0,9)
print(correct_number)
def html_h1(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        h1 = "<h1>{}</h1>".format(result)
        return h1
    new_function.__name__ = func.__name__
    return new_function

@app.route('/')
@html_h1
def start():
    return 'Guess a number between 0 and 9 <br> \
        <img src="https://media.giphy.com/media/Xblm7GRyDiCM53EQkG/giphy.gif"</img>'

@app.route('/<int:number>')
@html_h1
def guessing(number):
    if number == correct_number:
        return f'This was the correct {number}<br>\
            <img src="https://media.giphy.com/media/IwAZ6dvvvaTtdI8SD5/giphy.gif"</img>'
    elif number < correct_number:
        return f'Guess again <br> \
            <img src="https://media.giphy.com/media/pNCpaSVwEAQMpkoR1f/giphy.gif"</img>'
    else:
        return f'Guess again <br> \
            <img src="https://media.giphy.com/media/mhxZiXPbpF8QmtJe7Q/giphy.gif"</img>'

if __name__ == '__main__':
    app.run(debug=True)
