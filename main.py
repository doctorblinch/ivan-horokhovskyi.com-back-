from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'app':'doctorblinch app'})

if __name__ == '__main__':
    app.run()
