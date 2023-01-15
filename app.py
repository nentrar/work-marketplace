from flask import Flask
from flask import render_template
from marketplace import Marketplace

magic = Marketplace()
items = magic.read_all_data()

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           topic=items["1"]["Card"],
                           cat=items["1"]["Cat"],
                           image=items["1"]["Image"],
                           price=items["1"]["Price"])
