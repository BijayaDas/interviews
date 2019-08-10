from flask import Flask, jsonify, request, Response, redirect, url_for, render_template
import util

# Creating Flask app
app = Flask(__name__, template_folder='../templates')


@app.route('/', methods=['GET'])
def index():
	step = util.get_data_with_id(1)
	return render_template("index.html", step=step)

@app.route('/get_next_step', methods=['GET'])
def get_next_step():
	step = util.get_data_with_id(request.args.get("next_id", 1))
	return jsonify(results=step)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
