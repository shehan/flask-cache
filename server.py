from datetime import datetime

from flask import *
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        now = datetime.now()
        headers = [('Set-Cookie', 'last_access=' + str(now) + ';path=/'), ('Set-Cookie', 'country=usa;Max-Age=60;path=/')]
        return {'message': 'C is for cookie that’s good enough for me'}, 200, headers


api.add_resource(HelloWorld, '/api/set-cookie')


@app.route('/set-cookie')
def set_cookie():
    response = make_response("<h1>cookie is set</h1>")
    response.set_cookie('userID', 'john')
    response.set_cookie('email', 'john@smith.com', max_age=(5 * 60))
    response.set_cookie('token', '1234ABCD', max_age=5)
    return response


@app.route('/get-cookie')
def get_cookie():
    name = request.cookies.get('userID')
    email = request.cookies.get('email')
    token = request.cookies.get('token')
    last_access = request.cookies.get('last_access')
    country = request.cookies.get('country')
    error_message = ''
    message = ''
    if name is None:
        error_message = error_message + '<br><h1>userID Cookie Not Set</h1>'
    if token is None:
        error_message = error_message + '<br><h1>token Cookie Not Set</h1>'
    if email is None:
        error_message = error_message + '<br><h1>email Cookie Not Set</h1>'
    if last_access is None:
        error_message = error_message + '<br><h1>last_access Cookie Not Set</h1>'
    if country is None:
        error_message = error_message + '<br><h1>country Cookie Not Set</h1>'

    if name is not None:
        message = message + '<h1>userID:' + name + '</h1>'
    if token is not None:
        message = message + '<br><h1>token:' + token + '</h1>'
    if email is not None:
        message = message + '<br><h1>email:' + email + '</h1>'
    if last_access is not None:
        message = message + '<br><h1>last_access:' + last_access + '</h1>'
    if country is not None:
        message = message + '<br><h1>country:' + country + '</h1>'

    return error_message + message


@app.route('/delete-cookie')
def delete_cookie():
    response = make_response("<h1>cookie is deleted</h1>")
    response.delete_cookie('userID')
    response.delete_cookie('email')
    response.delete_cookie('token')
    response.delete_cookie('last_access')
    response.delete_cookie('country')

    return response


if __name__ == '__main__':
    app.run(debug=True)
