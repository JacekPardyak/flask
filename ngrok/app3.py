#!/usr/bin/env python
from flask import Flask, render_template, send_from_directory
import logging, ngrok
import os
import uuid
import rpy2.robjects as robjects
r = robjects.r

logging.basicConfig(level=logging.INFO)
listener = ngrok.werkzeug_develop()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/plots'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot')
def plot():
    # Generate a unique filename
    plot_filename = f'plot_{uuid.uuid4().hex}.png'
    plot_filepath = os.path.join(app.config['UPLOAD_FOLDER'], plot_filename)
    r_filepath = plot_filepath.replace("\\", "/")
    # R code to create and save the plot
    r_code = f'''
    library(ggplot2)
    ggplot(mpg, aes(displ, hwy, colour = class)) + 
      geom_point()
    ggsave("{r_filepath}", dpi = 60)
    '''
    # Execute the R code
    r(r_code)
    return render_template('plot.html', plot_image=plot_filename)

@app.route('/static/plots/<filename>')
def serve_plot(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)


# run with
# NGROK_AUTHTOKEN=2kINMGp8T4PcEzp86qqv5lHjWGg_7XaVCetGfBroeEaRvRk3Q python app.py
