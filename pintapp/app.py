from flask import Flask, render_template
from flask.ext import restful
from logbook import Logger

app = Flask(__name__)
api = restful.Api(app)
log = Logger(__name__)

@app.route("/")
def index():
    render_template('index.html')


class RegisterUser(restful.Resource):
    def post(self):
        return {'token': 'a_pony_token'}

class ConfirmUser(restful.Resource):
    def post(self):
        return {'token': 'a_pony_token'}

class SendMessage(restful.Resource):
    def post(self):
        return {'token': 'a_pony_token'}


api.add_resource(RegisterUser, '/register')
api.add_resource(ConfirmUser, '/register/confirm')
api.add_resource(SendMessage, '/send')


if __name__ == '__main__':
    app.run(debug=True)
