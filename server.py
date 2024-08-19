import shutil
from flask import (
    Flask,
    jsonify,
    redirect,
    request,
    render_template,
    send_from_directory,
    session,
    url_for,
)
import os
from werkzeug.utils import secure_filename
from model import process_image, model_predict
from music import assign_age_range, fetch_playlist


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
MUSIC_FOLDER = "music"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MUSIC_FOLDER"] = MUSIC_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return render_template("upload.html")


# @app.route('/static/<path:path>')
# def send_static(path):
#     return send_from_directory('static', path)
prediction = 0
correct_age = 0


@app.route("/get-playlist", methods=["GET"])
async def get_playlist():
    if request.method == "GET":
        index = request.args.get("index", default=0, type=int)
        print(index,"\n\n")
        initial = request.args.get("is_initial", default='true', type=str)
        if initial == 'false':
            initial = False
        else:
            initial = True
        print(initial)
        data = await fetch_playlist(index, initial)
        print(data)
        return jsonify(data)
    else:
        return "Invalid request method"
    # data = await async_db_query(...)


@app.route("/music")
def get_music():
    try:
        index = assign_age_range(correct_age)
        # song_names = get_initial_playlist(index)
        # download_base(index, "./music/songs/")
        # song_covers = get_initial_playlist_song_cover(index)
        # songs = (song_names, song_covers)
        # rec_songs = get_recommendations(index)
        return render_template("music.html", index=index)
    except Exception as e:
        return f"Error: {e}", 500


@app.route("/music/<filename>")
def serve_music(filename):
    return send_from_directory(app.config["MUSIC_FOLDER"], filename)


@app.route("/upload", methods=["POST"])
def upload_file():
    global prediction
    if "photo" not in request.files:
        return "No file uploaded.", 400
    file = request.files["photo"]
    if file.filename == "":
        return "No file selected.", 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)
        try:
            image = process_image(file_path)
            try:
                prediction = model_predict(image)
                print("prediction: ", prediction)
                return "Success"
            except Exception as e:
                return str(e), 500
        except Exception as e:
            return str(e), 500


@app.route("/predict")
def predict():
    return render_template("predict.html", predicted_age=prediction)


@app.route("/confirm_age", methods=["POST"])
def confirm_age():
    global correct_age
    try:
        correct_age = request.form["correct_age"]
        try:
            files = os.listdir("uploads")
            first_image_path = os.path.join("uploads", files[0])
            DESTINATION_FOLDER = f"data/{correct_age}/"
            try:
                shutil.move(first_image_path, DESTINATION_FOLDER)
            except:
                os.remove(
                    os.path.join(DESTINATION_FOLDER, os.path.basename(first_image_path))
                )
                shutil.move(first_image_path, DESTINATION_FOLDER)
            return "Success"
        except Exception as e:
            return f"Error: {e}", 500
    except KeyError:
        return "Error: Missing form data.", 400
    except Exception as e:
        return f"Error: {e}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
