from flask import Flask
from flask import render_template
from bazaar import Bazaar

magic = Bazaar()
items = magic.read_all_data()

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', bazaar_items=items)
