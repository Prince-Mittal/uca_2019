from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    card1 = "20.png"
    card2 = "30.png"
    card3 = "40.png"
    card4 = "50.png"
    card5 = "A0.png"
    cards = [card1, card2, card3, card4, card5]
    card6 = "42.png"
    card7 = "A1.png"
    card8 = "93.png"
    card9 = "81.png"
    card10 = "71.png"
    cards2 = [card6, card7, card8, card9, card10]
    return render_template("index.html", user1_card=cards, user2_card=cards2)


if __name__ == '__main__':
    print(app.config)
    app.config['DEBUG'] = True
    app.run()