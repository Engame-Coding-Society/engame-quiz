import requests

API_ROOT = "https://handle-https-request-uqetykzpsa-uc.a.run.app/"


def save_player(player_name, score):
    try:
        resp = requests.post(f"{API_ROOT}scores", json={"name": player_name, "score": score})
        if resp.status_code != 201:
            print(resp.text)
        return resp.json()
    except Exception as e:
        return {"success": False, "cause": "Internal Error"}


def get_top():
    try:
        resp = requests.get(f"{API_ROOT}scores/top")
        if resp.status_code != 200:
            print(resp.text)
        return resp.json()
    except Exception as e:
        return {"success": False, "cause": "Internal Error"}


def get_player_score(player_name):
    try:
        resp = requests.get(f"{API_ROOT}scores/{player_name}")
        if resp.status_code != 200:
            print(resp.text)
        return resp.json()
    except Exception as e:
        return {"success": False, "cause": "Internal Error"}
