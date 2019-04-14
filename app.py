import logging
import os

from flask import (
    Flask,
    jsonify,
    request,
)


LOG_LEVEL = os.environ.get('FLASK_LOG_LEVEL', 'ERROR')

# NOTE: One option for logging, which I'd be inclined to do in production:
# Werkzeug already logs request-level information, including timestamp,
# method, path, and IP address.
logging.getLogger('werkzeug').setLevel(LOG_LEVEL)

app = Flask(__name__)
app.logger.setLevel(LOG_LEVEL)


def wants_json(request):
    """Return True if this is a GET request and asks for JSON."""
    return (
        request.method == 'GET'
        and request.headers.get('Accept') == 'application/json'
    )


@app.route('/', methods=['GET', 'POST'])
def hello():
    # NOTE: Another option for logging, which is more flexible, is to hop on
    # the logger for Flask (which is an instance of the standard Python
    # logger), and use that.
    app.logger.debug('%s %s', request.method, request.url)

    if wants_json(request):
        return jsonify(message='Good morning')
    return '<p>Hello, World</p>'
