from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Define a route to render the initial HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Define a route to handle the form submission
@app.route('/colorize', methods=['POST'])
def colorize():
    # Get the uploaded file
    file = request.files['image']
    
    # Save the file to a temporary location
    file_path = 'temp_bw_image.jpg'
    file.save(file_path)
    
    # Call the Python script to colorize the image
    os.system('python demo.py --img_path temp_bw_image.jpg')
    
    # Render the result HTML page with the colorized image
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
