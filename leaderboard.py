from requests import request
import json

API_ROOT = "https://handle-https-request-uqetykzpsa-uc.a.run.app/"


def save_player(player_name, score):
    try:
        resp = request("post", f"{API_ROOT}scores", data=json.dumps({"name": player_name, "score": score}),
                       headers={"Content-Type": "application/json"})
        if resp.status_code != 201:
            print(resp.text)
        return resp.json()
    except Exception as e:
        print(json.dumps(e))
        return {"success": False, "cause": "Internal Error"}


def get_top():
    try:
        resp = request("get", f"{API_ROOT}scores/top", data=None, headers=None)
        if resp.status_code != 200:
            print(resp.text)
        return resp.json()
    except Exception as e:
        return {"success": False, "cause": "Internal Error"}


def get_player_score(player_name):
    try:
        resp = request("get",f"{API_ROOT}scores/{player_name}")
        if resp.status_code != 200:
            print(resp.text)
        return resp.json()
    except Exception as e:
        return {"success": False, "cause": "Internal Error"}
