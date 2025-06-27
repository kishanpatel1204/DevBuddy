from flask import Flask
from routes.github_webhook import webhook

app = Flask(__name__)
app.register_blueprint(webhook)


if __name__ == '__main__':
    app.run(port=5000)
    