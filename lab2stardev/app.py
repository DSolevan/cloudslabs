from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_NAME = os.getenv('APP_NAME', 'default_app')

@app.route('/')
def hello():
    return jsonify({
        "message": f"Hello from {APP_NAME}",
        "app_name": APP_NAME
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "app_name": APP_NAME
    }), 200

@app.route('/version')
def version():
    return jsonify({
        "version": "1.0",
        "app_name": APP_NAME
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)