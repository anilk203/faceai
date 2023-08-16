from flask import Flask, request, render_template
from flask import render_template, jsonify
from werkzeug.utils import secure_filename
import os
import requests
from pathlib import Path
from decimal import Decimal
from db import MySQLDatasource
import uuid
from datetime import datetime
import json
app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

 
@app.route('/')
def index():
    return render_template('index.html', title='Home')


def __register():
       facename = request.form.get("face_name")
       file = request.files['file']
       if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join("/", filename))
             
            
       face_file = open("/" + filename, "rb").read() 
       file=os.stat("/" + filename)
       file_size = (file.st_size / (1024))
      

       data = requests.post("http://faceai:5000/v1/vision/face/register", files={"image":face_file}, data={"userid":filename}).json()
       
       
       user_id = str(uuid.uuid4())
       registration_id = str(uuid.uuid4())
       
       
       file_size = round(Decimal(file_size),4) 
       mysql = MySQLDatasource()
       # check if exists based on user_name, l_file_name, l_file_size_in_kb
       existing_user_id = mysql.user_exists(facename, filename, file_size)
       
       if existing_user_id==None:
           user_id = user_id = str(uuid.uuid4())
           
           data['registration_id'] = registration_id
           data['user_id'] = user_id
           data['user_name'] = facename
           data['l_file_name'] = filename
           data['l_file_path'] = os.path.abspath(filename)
           data['l_file_size_in_kb']  = file_size
           
           mysql.save(data)
           
           additional_params = {
               'registration_id': registration_id,
               "user_id": user_id,
               "date": datetime.now()
           } 
           mysql.save_params(user_id, additional_params)
        
       else:
            user_id = existing_user_id['user_id']
           
        
           
       response_data = {'facename': facename, 'status': 'success', 'user_id': user_id}
       
       return response_data    
   
   
@app.route('/api/register', methods=["POST"])
def api_register():
       return __register()

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
       response_data = __register()
       return render_template('register.html', title='Register', response_data=response_data)
    
    return render_template('register.html', title='Register')

@app.route('/api/recognize', methods=["POST"])
def __recognize():
       file = request.files['file']
       if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join("/recognize/", filename))
            
       face_file = open("/recognize/" + filename, "rb").read() 
        
       res = requests.post("http://faceai:5000/v1/vision/face/recognize", files={"image":face_file}).json()        
       recongize_id = str(uuid.uuid4())
       additional_params = {
           "face_file": filename,
           "recongize_id": recongize_id,
       } 
       
       
    # handle exception
       mysql = MySQLDatasource()
       additional_params['success']=res['success']
       predictions = res['predictions']
       for p in predictions:
           for key,value in p.items():
               additional_params[key]=value
           mysql.save_recognize_params(recongize_id, filename, additional_params) 
       
       return res   
    
@app.route('/recognize', methods=["GET", "POST"])
def recognize():
    if request.method == "POST":
       res = __recognize()
       return render_template('recognize.html', data=res) 
    
    return render_template('recognize.html', title='Recognize')


@app.route('/registry')
def registry():
    
    mysql = MySQLDatasource()
    registrations = mysql.get_registrations()
    
    return render_template('registry.html', title='Registry', data = registrations)

    
if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['DEBUG'] = True
    app.run(debug=True, host='0.0.0.0', threaded=True, port=5000)

