from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)  
app.secret_key = 'keep it secret, keep it safe'

is_game_on = True
rand = None


@app.route('/')
def index():
    rand = random.randint(1,10)
    session['random'] = rand
    is_game_on = True
    return render_template("index.html", is_game_on = is_game_on)

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect("/game")

@app.route('/game')
def game():
    is_game_on = True
    guess = session['guess']
    if guess == session['random']:
        is_game_on = False
    return render_template("index.html", guess = guess, answer = session['random'], is_game_on = is_game_on)

@app.route('/again', methods=['POST'])
def again():
    is_game_on = True
    session.clear()
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)