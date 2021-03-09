from flask import Flask, request
app = Flask(__name__)


@app.route('/flask')
def hello_sample():
    return "Hello Flask!"


@app.route('/user/<user_id>')
def hello_person(user_id):
    return "Hello " + user_id


@app.toute('/test', methods=['GET', 'POST'])
def post_test():
    if request.method == 'GET':
        pass
    else:
        pass
    return '0'


if __name__ == '__main__':
    app.run()
