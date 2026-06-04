from flask import Flask, render_template, jsonify
import config

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    with config.data_lock:
        data = dict(config.latest_data)
    return render_template('index.html', data=data)

@app.route('/api/data')
def get_data():
    with config.data_lock:
        return jsonify(config.latest_data)

def start_web_server():
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)