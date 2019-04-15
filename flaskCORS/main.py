'''
Simple way to set up Flask CORS in your code
'''
from flask import Flask, jsonify
from flask_cors import cross_origin

try:
    from flask_cors import CORS  # The typical way to import flask-cors
except ImportError:
    # Path hack allows examples to be run without installation.
    import os
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)


app = Flask(__name__)
CORS(app, resources=r'/api/*')

# @app.route("/")
# def helloWorld():
#   return "Hello, cross-origin-world!"
# Above code is the simplest case with no resource specificity, or route specificity

# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
#
# @app.route("/api/v1/users")
# def list_users():
#   return "user example"
#The above code is an example of resource specific CORS.
#Here you can CORS options on a resource and origin level of granularity by passing a dictionary as the resources option, mapping paths to a set of options.

@app.route("/api/")
@cross_origin()
def helloWorld():
    return "Hello, cross-origin-world!"

'''
notice how the @cross_origin is under the route above. This is considered a route specific CORS using a decorator.
Basically it allows you to make only certain routes allow CORS.
'''

@app.route("/login")
@cross_origin(supports_credentials=True)
def login():
  return jsonify({'success': 'ok'})

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)
