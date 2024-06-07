from flask import Flask
import os

from routes import e_commerce

app = Flask(__name__)
app.secret_key=os.environ["SECRET_KEY"]
app.register_blueprint(e_commerce)


if __name__ == "__main__":
    app.run(debug=True,port=8000)