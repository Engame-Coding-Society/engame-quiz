import json
import time
from flask import Flask, jsonify, request

app = Flask(__name__)


scoreboard: list[dict] = [
    {"name": "Endergamer_hun", "score": 5, "date": 0.0},
    {"name": "Peter", "score": 3, "date": 0.0},
]


def error(cause: str):
    return jsonify(success=False, cause=cause)


def success(data=None, **kwargs):
    if len(kwargs) > 0:
        return jsonify(success=True, data=kwargs)
    return jsonify(success=True, data=data)


def get_player_score(name: str):
    for score in scoreboard:
        if score["name"] == name:
            return score
    return None


def remove_score(name: str):
    for score in scoreboard:
        if score["name"] == name:
            scoreboard.remove(score)


@app.route("/scores", methods=["GET"])
def get_scoreboard():
    return success(scoreboard)


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
    date: float = data.get("date") or time.time()

    prev = get_player_score(name)["score"]
    if prev >= score:
        return error(f"Score not higher than previous score of {prev}."), 409

    entry = {"name": name, "score": score, "date": date}
    remove_score(name)
    scoreboard.append(entry)
    return success(entry), 201


@app.route("/top", methods=["GET"])
def get_top():
    return jsonify(error("Not implemented yet")), 501


@app.route("/top/<int:top>", methods=["GET"])
def get_top_id(top: int):
    return jsonify(error("Not implemented yet")), 501
