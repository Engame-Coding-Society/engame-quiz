import json
from firebase_functions import firestore_fn, https_fn, options
from firebase_admin import firestore, credentials, initialize_app
from flask import Flask, jsonify, request, Response
import os, sys

prefix = "server/" if not str(os.getcwd()).endswith('server') else ""
cred = credentials.Certificate(f".firebase.json")
initialize_app(cred)

options.set_global_options(max_instances=10)
db = firestore.client()

app = Flask(__name__)


def error(cause: str):
    return jsonify(success=False, cause=cause)


def success(data=None, **kwargs):
    if len(kwargs) > 0:
        return jsonify(success=True, data=kwargs)
    return jsonify(success=True, data=data)


def get_player_score(name: str):
    global db
    player_ref = db.collection("points_prod").document(name).get()
    if not player_ref.exists:
        return None
    else:
        return {"name": name, "score": player_ref.to_dict()["score"]}


CORS_HEADERS = [("Access-Control-Allow-Methods", "POST, GET, OPTIONS"),
                ("Access-Control-Allow-Headers", "Content-Type, Origin, Content-Length"),
                ("Access-Control-Allow-Origin", "*")]


@app.route("/scores", methods=["GET"])
def get_scoreboard():
    scores_stream = db.collection("points_prod").stream()
    scores = []
    for score in scores_stream:
        scores.append({"name": score.id, "score": score.to_dict()["score"]})
    return success(scores)


@app.route("/scores/<string:name>", methods=["GET"])
def get_player(name: str):
    score = get_player_score(name)
    if score is None:
        return error("User doesn't exist"), 404
    return success(score)


def is_valid(entry: dict) -> bool:
    keys = entry.keys()
    return ("name" in keys) and ("score" in keys)


@app.route("/scores", methods=["POST"])
def add_score():
    data = json.loads(request.data)
    if not is_valid(data):
        return error("Malformed request"), 400

    name: str = data.get("name")
    score: int = data.get("score")

    prev = get_player_score(name)
    if prev is not None and prev["score"] >= score:
        return error(f"Score not higher than previous score of {prev}."), 409

    db.collection("points_prod").document(name).set({"score": score})
    return success({"name": name, "score": score}), 201


def get_top_players(limit: int = 10) -> list:
    top_stream = db.collection("points_prod").order_by("score", direction=firestore.Query.DESCENDING).limit(limit).stream()
    return [{"name": p.id, "score": p.to_dict()["score"]} for p in top_stream]


@app.route("/scores/top", methods=["GET"])
def get_top():
    return success(get_top_players())


@app.route("/scores/top/top/<int:top>", methods=["GET"])
def get_top_id(top: int):
    return success(get_top_players(top))


@https_fn.on_request()
def handle_https_request(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        dispatched_request = app.full_dispatch_request()
        full_headers = []
        for header, value in dispatched_request.headers.items():
            full_headers.append((header, value))
        for header in CORS_HEADERS:
            full_headers.append(header)
        return Response(dispatched_request.response, dispatched_request.status, full_headers)
