from flask import Flask, request, jsonify, send_from_directory, render_template
import base64
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

# Ensure the "images" directory exists
IMAGE_DIR = "images"
global img_name
os.makedirs(IMAGE_DIR, exist_ok=True)


# Route to save the image
@app.route('/save_image', methods=['POST'])
def save_image():
    data = request.json
    image_data = data.get("image", "")
    img_name = data.get("name", "").lower().replace(" ","")+".png"

    if not image_data.startswith("data:image/png;base64,"):
        return jsonify({"message": "Invalid image format"}), 400

    # Remove base64 header
    image_data = image_data.replace("data:image/png;base64,", "")

    # Decode and save the image
    image_bytes = base64.b64decode(image_data)
    image_path = os.path.join(IMAGE_DIR, img_name)

    with open(image_path, "wb") as f:
        f.write(image_bytes)

    return jsonify({"message": "Image saved successfully!", "image_url": "/get_image"})

# Route to serve the saved image
@app.route('/get_image', methods=['GET'])
def get_image():
    return send_from_directory(IMAGE_DIR, img_name)


@app.route('/')  # Root URL will now load upload.html
def upload():
    return render_template('upload.html')  

@app.route('/data')
def data():
    return render_template('data.html')  

leaderboard = []

@app.route('/addPerson', methods=['POST'])
def add_person():
    person = request.json
    leaderboard.append(person)
    return jsonify({'status': 'success', 'person': person})

@app.route('/updateScore', methods=['POST'])
def update_score():
    updated_person = request.json
    for person in leaderboard:
        if person['name'] == updated_person['name']:
            person['questionsAnswered'] = updated_person['questionsAnswered']
            break
    return jsonify({'status': 'success', 'person': updated_person})

@app.route('/getLeaderboard', methods=['GET'])
def get_leaderboard():
    return jsonify({'leaderboard': leaderboard})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
