from flask import Flask, render_template, send_from_directory
import os
import uuid
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/plots'
app.config['R_SCRIPT_PATH'] = 'scripts/plot_script.R'

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/plot')
def plot():
    # Generate a unique filename for the plot
    plot_filename = f'plot_{uuid.uuid4().hex}.svg'
    plot_filepath = os.path.join(app.config['UPLOAD_FOLDER'], plot_filename)

    # Run the R script with the output file path as an argument
    subprocess.run(['Rscript', app.config['R_SCRIPT_PATH'], plot_filepath], check=True)

    return render_template('plot2.html', plot_image=plot_filename)

@app.route('/static/plots/<filename>')
def serve_plot(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
    
