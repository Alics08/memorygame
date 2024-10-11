from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Sample cards for the memory game
easy_cards = ['🐶', '🐱', '🐰', '🐻'] * 2  # 8 cards total (4 pairs)
medium_cards = ['🐶', '🐱', '🐰', '🐻', '🦁', '🐸', '🐵', '🐷'] * 2  # 16 cards total (8 pairs)
hard_cards = ['🐶', '🐱', '🐰', '🐻', '🦁', '🐸', '🐵', '🐷', '🦄', '🦓', '🦍', '🐢', '🐍', '🐳', '🐙', '🦑'] * 2  # 32 cards total (16 pairs)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/cards/<difficulty>')
def get_cards(difficulty):
    if difficulty == 'easy':
        cards = easy_cards
    elif difficulty == 'medium':
        cards = medium_cards
    else:  # difficulty == 'hard'
        cards = hard_cards

    random.shuffle(cards)  # Shuffle cards for each game
    return jsonify(cards)

@app.route('/api/check/<int:card1>/<int:card2>/<difficulty>')
def check(card1, card2, difficulty):
    if difficulty == 'easy':
        cards = easy_cards
    elif difficulty == 'medium':
        cards = medium_cards
    else:  # difficulty == 'hard'
        cards = hard_cards

    if cards[card1] == cards[card2]:
        return jsonify({'match': True})
    return jsonify({'match': False})

if __name__ == '__main__':
    app.run(debug=True)
