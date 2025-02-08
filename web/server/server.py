from flask import Flask, request, jsonify, send_from_directory, render_template
import base64
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

# Ensure the "images" directory exists
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)

# Serve the main webpage
@app.route('/')
def home():
    return render_template("index.html")  # This will load templates/index.html

# Route to save the image
@app.route('/save_image', methods=['POST'])
def save_image():
    data = request.json
    image_data = data.get("image", "")

    if not image_data.startswith("data:image/png;base64,"):
        return jsonify({"message": "Invalid image format"}), 400

    # Remove base64 header
    image_data = image_data.replace("data:image/png;base64,", "")

    # Decode and save the image
    image_bytes = base64.b64decode(image_data)
    image_path = os.path.join(IMAGE_DIR, "snapshot.png")

    with open(image_path, "wb") as f:
        f.write(image_bytes)

    return jsonify({"message": "Image saved successfully!", "image_url": "/get_image"})

# Route to serve the saved image
@app.route('/get_image', methods=['GET'])
def get_image():
    return send_from_directory(IMAGE_DIR, "snapshot.png")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
