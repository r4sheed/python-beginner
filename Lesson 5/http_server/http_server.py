"""
This script is a Flask web application that facilitates file uploads and downloads. It is designed to handle text and CSV files, providing a secure and user-friendly interface for users to upload their data. The application includes robust error handling to ensure that only permitted file types are accepted, and it employs a secret key for secure session management. The script also automatically creates the upload directory if it does not already exist, ensuring a smooth user experience.

Documentation was created by Phind-34B model.
"""

# Import necessary modules
import os
import secrets
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

# Get the current working directory
current_directory = os.getcwd()

# Define UPLOAD_FOLDER as a subdirectory within the current working directory
UPLOAD_FOLDER = os.path.join(current_directory, 'uploads')

# Check if the UPLOAD_FOLDER exists, if not, create it
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Define the allowed file extensions for uploads
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

# Create a Flask application instance
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16) # Generate a secret key
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if a file has an allowed extension
def allowed_file(file_name):
    """
    Checks if the given file name has an allowed extension.

    Args:
        file_name (str): The name of the file to check.

    Returns:
        bool: True if the file has an allowed extension, False otherwise.
    """
    return '.' in file_name and file_name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to serve uploaded files
@app.route('/uploads/<filename>')
def upload_files(filename):
    """
    Serves the uploaded file to the client.

    Args:
        filename (str): The name of the file to serve.

    Returns:
        Response: A Flask response object with the file's content.
    """
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Route to handle file uploads
@app.route('/', methods=['POST', 'GET'])
def upload_file():
    """
    Handles file uploads and downloads.

    If the request method is POST, the file is uploaded. If the request method is GET, the upload form is displayed.

    Args:
        None

    Returns:
        Response: A Flask response object with the appropriate content.
    """
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Error: No file part in the request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('Error: No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_files', filename=filename))
        else:
            flash('Error: File extension not allowed')
            return redirect(request.url)
    else:
        return render_template('upload.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)