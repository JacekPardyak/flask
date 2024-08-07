# app.py
# run with python app.py
# app is here http://127.0.0.1:5000/
from flask import Flask, render_template_string, send_file, render_template, request
import pandas as pd
import io
import matplotlib.pyplot as plt

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [70000, 80000, 65000, 90000, 75000]
}

# Create a DataFrame
df = pd.DataFrame(data)
df_html = df.to_html(classes='table table-striped')
    
# HTML template
template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DataFrame Display</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <h1>DataFrame Display</h1>
            {{ df_html | safe }}
        </div>
    </body>
    </html>
    '''

# Generate the plot
plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['Salary'], color='blue')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Salary of Individuals')
img = io.BytesIO()
plt.savefig(img, format='png')
img.seek(0)

# Generate the plot in svg
fig, ax = plt.subplots()
df.plot(kind='bar', x='Name', y='Salary', ax=ax)
    
# Save the plot to a BytesIO object in SVG format
svg_output = io.BytesIO()
plt.savefig(svg_output, format='svg')
plt.close(fig)
svg_output.seek(0)
    
# Render the SVG in HTML
svg_data = svg_output.getvalue().decode()

svg_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SVG Plot Display</title>
    </head>
    <body>
        <div class="container">
            <h1>SVG Plot Display</h1>
            {{ svg_data|safe }}
        </div>
    </body>
    </html>
    '''


app = Flask(__name__)

@app.route('/')
def index():
    return 'index'
  
@app.route('/table')
def table():
    return render_template_string(template, df_html = df_html)

@app.route('/plot')
def plot():
    return send_file(img, mimetype='image/png')

@app.route('/svg')
def svg():
    return render_template_string(svg_template, svg_data=svg_data)

@app.route('/form')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Hello, {name}!'
  
if __name__ == "__main__":
    app.run(debug=True)
    
