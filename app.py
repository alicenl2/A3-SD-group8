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

    def _repr_(self):
        return f'<GameResult {self.id} - {self.result}>'



@app.route('/')
def home():
    options = ['Even', 'Odd']
    return render_template('home_html', options=options)


if __name__ == '__main__':
    app.run(debug=True)

