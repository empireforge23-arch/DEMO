from PIL import Image
import io

app = Flask(__name__)

# --- Image processing function ---
def make_cartoon(image_bytes):
    img = Image.open(io.BytesIO(image_bytes))

    # Simple cartoon effect (grayscale + edge enhance)
    img = img.convert("L") # grayscale
    img = img.convert("RGB")

    output = io.BytesIO()
    img.save(output, format="PNG")
    output.seek(0)

    return output

# --- Home route (UI) ---
@app.route("/", methods=["GET"])
def home():
    return '''
    <h2>Upload an Image</h2>
    <form method="post" enctype="multipart/form-data" action="/upload">
        <input type="file" name="image" />
        <input type="submit" value="Upload" />
    </form>
    '''

# --- Upload route ---
@app.route("/upload", methods=["POST"])
def upload():
    if 'image' not in request.files:
        return 'No image uploaded', 400

    file = request.files['image']

    if file.filename == '':
        return 'No selected file', 400

    cartoon = make_cartoon(file.read())
    return send_file(cartoon, mimetype='image/png')

# --- Run app ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
