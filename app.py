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
                           topic=items["001"]["Topic"],
                           type=items["001"]["Type"],
                           description=items["001"]["Description"],
                           image=items["001"]["Image"],
                           price=items["001"]["Price"])
