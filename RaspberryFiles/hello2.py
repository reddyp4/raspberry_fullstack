from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello2 World!"

@app.route("/example")
def example_route():
    return "This is an example route"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080
)
