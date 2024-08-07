from flask import Flask, render_template, request, redirect, url_for
import os
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/img'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_file', methods=["POST"])
def upload_file():
    if 'image_upload' not in request.files:
        return redirect(request.url)
    
    file = request.files['image_upload']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        unique_id = uuid.uuid4().hex
        filename = f'img_{unique_id}.png'
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        return render_template('image.html', img_show=filename)

    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
