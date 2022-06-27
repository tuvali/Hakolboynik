from flask import Blueprint, render_template

# policy blueprint definition
policy = Blueprint('policy', __name__, static_folder='static', static_url_path='/policy', template_folder='templates')


# Routes
@policy.route('/policy')
def index():
    return render_template('policy.html')
