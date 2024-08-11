import os
import uuid
import rpy2.robjects as robjects
r = robjects.r
r.source('r_code.R')

def run_r():
    r.source('r_code.R')
    return 1

run_r()

r_code = """
library(ggplot2)

ggplot(mpg, aes(displ, hwy, colour = class)) + 
  geom_point()
ggsave("plot2.png")
"""
r(r_code)

UPLOAD_FOLDER = 'static\plots'
def plot():
    # Generate a unique filename
    plot_filename = f'plot_{uuid.uuid4().hex}.png'
    plot_filepath = os.path.join(UPLOAD_FOLDER, plot_filename)
    r_filepath = plot_filepath.replace("\\", "/")
    print(r_filepath)
    # R code to create and save the plot
    r_code = f'''
    library(ggplot2)
    ggplot(mpg, aes(displ, hwy, colour = class)) + 
      geom_point()
    ggsave("{r_filepath}")
    '''
    # Execute the R code
    r(r_code)
    return r_filepath

plot()
