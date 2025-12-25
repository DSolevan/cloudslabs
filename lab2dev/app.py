from flask import Flask, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/', methods=['GET'])
def hello():
    logger.info("Запрос на главную страницу")
    return jsonify({
        "status": "ok"
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/version', methods=['GET'])
def version():
    return jsonify({"version": "1.0.0"})

if __name__ == '__main__':
    logger.info("Запуск Flask приложения на порту 5000")
    app.run(host='0.0.0.0', port=5000, debug=False)


