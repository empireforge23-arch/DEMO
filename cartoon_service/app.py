# app.py
from flask import Flask, request, send_file
from PIL import Image, ImageOps
import io
import os

app = Flask(__name__)

def make_cartoon(image_bytes):
    """Convert image to cartoon-like effect (simplified)"""
    img = Image.open(io.BytesIO(image_bytes))
    # Convert to grayscale, then apply edge enhance, then posterize
    img = ImageOps.grayscale(img)
    img = img.resize((img.width // 2, img.height // 2), Image.Resampling.LANCZOS)
    img = img.resize((img.width * 2, img.height * 2), Image.Resampling.NEAREST)
    # Save to bytes
    output = io.BytesIO()
    img.save(output, format='PNG')
    output.seek(0)
    return output

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'image' not in request.files:
            return 'No image uploaded', 400
        file = request.files['image']
        if file.filename == '':
            return 'No selected file', 400
        cartoon = make_cartoon(file.read())
        return send_file(cartoon, mimetype='image/png')
    return '''
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="image">
        <input type="submit">
    </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 

