from flask import render_template, Blueprint
from bazaar import magic

market = magic.Bazaar()
items = market.read_all_data()

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html', bazaar_items=items)

# @main.route('/')
# def index():
#     return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('profile.html')
