from flask import Flask, request
app = Flask(__name__)


@app.route('/flask')
def hello_sample():
    return "Hello Flask!"


@app.route('/user/<user_id>')
def hello_person(user_id):
    return "Hello " + user_id


@app.route('/admin/<admin_id>')
def hello_admin(admin_id):
    return "Hello " + admin_id


if __name__ == '__main__':
    app.run()
