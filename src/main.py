from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
    message = 'Hello world!'
    print(message)
    return message


if __name__ == "__main__":
    app.run()