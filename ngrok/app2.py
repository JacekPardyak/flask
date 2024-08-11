#!/usr/bin/env python

import flask, logging, ngrok

logging.basicConfig(level=logging.INFO)
listener = ngrok.werkzeug_develop()

app = flask.Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)

# run with
# NGROK_AUTHTOKEN=2kINMGp8T4PcEzp86qqv5lHjWGg_7XaVCetGfBroeEaRvRk3Q python app.py
