# import libraries
from __init__ import *


class about(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('about/about.html'), 200, headers)
