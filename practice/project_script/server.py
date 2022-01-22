import flask

import sum

app = flask.Flask(__name__)

@app.route('/')
def index():
	return 'Hello Web with sum 1 + 2 == {}'.format(sum.sum(1,2))

app.run(host='0.0.0.0', port=8888)
