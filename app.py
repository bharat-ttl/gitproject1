import json

from flask import Flask, Response, jsonify
from search import search
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/<query>')
def search_route(query):
    try:
        resp = search(query)
        return jsonify(dict(resp))
    except Exception as e:
        return Response(str(e), status=500)


if __name__ == '__main__':
    app.run()
