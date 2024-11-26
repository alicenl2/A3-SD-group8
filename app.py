import logging
from logging.handlers import RotatingFileHandler

# Configure Logging
if not app.debug:
    # File Handler: Logs to a file with rotation to avoid large files
    file_handler = RotatingFileHandler('guessing_game.log', maxBytes=100000, backupCount=3)
    file_handler.setLevel(logging.INFO)

    # Console Handler: Logs to the console for immediate feedback
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Formatter: Defines the format of the logs
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the app logger
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)


@app.route('/play', methods=['POST'])
def play():
    try:
        user_choice = request.form.get('choice')

        # Validate input
        if user_choice not in ['Even', 'Odd']:
            app.logger.warning('Invalid choice submitted by user.')
            return "Invalid choice!", 400

        # Game logic
        app_choice = random.choice(['Even', 'Odd'])
        result = 'Win' if user_choice == app_choice else 'Lose'

        # Save result to database
        new_game = GameResult(user_choice=user_choice, app_choice=app_choice, result=result)
        db.session.add(new_game)
        db.session.commit()

        # Log the successful game
        app.logger.info(f'Game played: User({user_choice}) - App({app_choice}) - Result({result})')

        return render_template('result.html', user_choice=user_choice, app_choice=app_choice, result=result)

    except Exception as e:
        # Log the error
        app.logger.error(f'Error during game play: {e}')
        return "An error occurred during the game.", 500




@app.route('/results')
def results():
    try:
        games = GameResult.query.order_by(GameResult.id.desc()).limit(10).all()
        return render_template('results.html', games=games)
    except Exception as e:
        app.logger.error(f'Error fetching results: {e}')
        return "An error occurred while fetching the results.", 500

