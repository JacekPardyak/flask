from flask import Flask, render_template, send_from_directory
import os
import uuid
import rpy2.robjects as robjects
r = robjects.r

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/plots'
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

@app.route('/run_r')
def run_r():
    #r.source('r_code.R')
    return render_template('run_r.html')

if __name__ == '__main__':
    app.run(debug=True)
