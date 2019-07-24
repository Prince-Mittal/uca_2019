from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    cards = ["20.png","30.png","40.png","50.png","60.png","70.png","80.png","90.png","T0.png","J0.png","Q0.png","K0.png","A0.png",
    "21.png","31.png","41.png","51.png","61.png","71.png","81.png","91.png","T1.png","J1.png","Q1.png","K1.png","A1.png","22.png","32.png",
    "42.png","52.png","62.png","72.png","82.png","92.png","T2.png","J2.png","Q2.png","K2.png","A2.png","33.png","33.png","43.png","53.png",
    "63.png","73.png","83.png","93.png","T3.png","J3.png","Q3.png","K3.png","A3.png"]
    user1_card = []
    user2_card = []
    random.shuffle(cards)
    for i in range(0,5):
        user1_card.append(cards[i])
    for i in range(5,10):
        user2_card.append(cards[i])
    return render_template("index.html", cards1=user1_card, cards2=user2_card)


if __name__ == '__main__':
    print(app.config)
    app.config['DEBUG'] = True
    app.run()