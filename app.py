from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    options = ['Even', 'Odd']
    return render_template('home_html', options=options)


if __name__ == '__main__':
    app.run(debug=True)

