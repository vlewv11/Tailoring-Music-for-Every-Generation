from urllib import request
from flask import app, jsonify
from music import fetch_playlist


@app.route("/get-playlist", methods=["GET"])
async def get_playlist():
    if request.method == "GET":
        index = request.args.get("index", default=0, type=int)
        print("index:\n\n",index)
        initial = request.args.get("is_initial", default=True, type=bool)
        print("initia:\n\n",initial)
        data = await fetch_playlist(index, initial)
        return jsonify(data)
    else:
        return "Invalid request method"