from flask import Flask, request, render_template
import os
from get_info_database import get_info_by_id
from fstage1 import extract_id_from_image , extract_text_from_image
from save_into_database import save_info

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'save_images_files'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/registered')
def registered():
    return render_template('registered.html')

@app.route('/non_registered')
def non_registered():
    return render_template('non_registered.html')



# Registered 
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    file_path = os.path.abspath(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    print("file path" ,os.path.join(app.config['UPLOAD_FOLDER']))
    print("filename :",filename)
    print(file_path)
    
    # Extract information from the image output is student_id
    student_id = extract_id_from_image(file_path)
    
    # Retrieve student information from database
    student_info = get_info_by_id(int(student_id))

    # Check if student_info is None
    if student_info is None:
        return render_template('popup1.html', message='Error retrieving student information')
    
    # Render the display template with the student information
    return render_template('display.html', student_info = student_info)

# Non - Registered 
@app.route('/upload1', methods=['POST'])
def upload1():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    file_path = os.path.abspath(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    
    # Extract information from the image output is student_id
    student_info = extract_text_from_image(file_path)

    

    # Check if student_info is None , it means student id alredy present
    if save_info(student_info) == 0:

        return render_template('popup2.html', message='Error retrieving student information')
    
    else:
    # Render the display template with the student information
        return render_template('display2.html', student_info = student_info)

if __name__ == '__main__':
    app.run(debug=True)
