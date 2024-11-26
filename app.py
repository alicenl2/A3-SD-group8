import random
from flask import Flask, render_template, request
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost:5432/guessing_game_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define GameResult Model
class GameResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_choice = db.Column(db.String(4), nullable=False)  # 'Even' or 'Odd'
    app_choice = db.Column(db.String(4), nullable=False)   # 'Even' or 'Odd'
    result = db.Column(db.String(4), nullable=False)       # 'Win' or 'Lose'

    def repr(self):
        return f'<GameResult {self.id} - {self.result}>'

@app.route('/')
def home():
    options = ['Even', 'Odd']
    return render_template('home.html', options=options)

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form.get('choice')
    app_choice = random.choice(['Even', 'Odd'])
    result = 'Win' if user_choice == app_choice else 'Lose'
    return render_template('result.html', user_choice=user_choice, app_choice=app_choice, result=result)


if __name__ == '__main__':
    app.run(debug=True) 


