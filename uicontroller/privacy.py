from __init__ import *


class privacy(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('privacy/privacy.html'), 200, headers)
