from flask import Blueprint, render_template
from interact_with_DB import interact_db
# kit blueprint definition
kit = Blueprint('kit', __name__, static_folder='static', static_url_path='/kit', template_folder='templates')


# Routes
@kit.route('/kit')
def kit_func():  # put application's code here
    query = 'select * from kit;'
    kit = interact_db(query=query, query_type='fetch')
    return render_template('kit.html', kit=kit)
