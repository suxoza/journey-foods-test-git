from flask import Flask, Blueprint

app = Flask(__name__)
api = Blueprint("app", __name__, url_prefix = '/')
api2 = Blueprint("app2", __name__, url_prefix = '/app2')
 


@api.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World! changed here'

@api2.route('/')
def hello2():
    """Return a friendly HTTP greeting."""
    return 'Hello World 2!'


app.register_blueprint(api)
app.register_blueprint(api2)


if __name__ == "__main__":
    # Dev only: run "python main.py" and open http://localhost:8080
    app.run(host="localhost", port=8080, debug=True)

