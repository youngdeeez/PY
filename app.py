from flask import Flask
app = Flask(__name__)
#test11
@app.route('/')
def hello_devops():
    return '<h1>Hello, DevOps!</h1><p>This is my first automated deployment.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)