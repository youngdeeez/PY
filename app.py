from flask import Flask
from prometheus_client import Counter, generate_latest, REGISTRY
from prometheus_client.exposition import CONTENT_TYPE_LATEST

app = Flask(__name__)

# Создаем метрики
REQUEST_COUNT = Counter('request_count', 'App Request Count', ['method', 'endpoint'])

@app.route('/')
def hello_world():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    return 'Hello, World!'

@app.route('/metrics')
def metrics():
    REQUEST_COUNT.labels(method='GET', endpoint='/metrics').inc()
    return generate_latest(REGISTRY), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)