#!/usr/bin/python3
"""
Flask App
"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_conn(self):
    """ close connection """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def get_state():
    """ get all states_list """
    state = storage.all('State').values()
    return render_template("7-states_list.html", state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
