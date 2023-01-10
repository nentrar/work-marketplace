from flask import Flask
from flask import render_template
from marketplace import marketplace

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           topic=marketplace[1]["Topic"],
                           type=marketplace[1]["Type"],
                           description=marketplace[1]["Description"],
                           image=marketplace[1]["Image"],
                           price=marketplace[1]["Price"])
