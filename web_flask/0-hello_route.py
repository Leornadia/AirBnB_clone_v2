#!/usr/bin/python3
"""
This script starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
/: display “Hello HBNB!”
"""
from web_flask import app

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route to display 'Hello HBNB!'.
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

