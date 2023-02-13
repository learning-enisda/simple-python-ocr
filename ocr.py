from flask import Flask, render_template, request
from PIL import Image
import pytesseract
import io

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST' and 'image' in request.files:
        image = request.files['image'].read()
        image = Image.open(io.BytesIO(image))
        result = pytesseract.image_to_string(image)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
