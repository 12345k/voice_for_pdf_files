from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
import main

app = Flask(__name__)

path= os.getcwd()+"/pdf_files"
os.makedirs(path, exist_ok=True)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['file']
      
      f.save(os.path.join(path,secure_filename(f.filename)))

      result=main.get_started(os.path.join(path,f.filename))

      message="PDF is uplaoded"
      return render_template('index.html',message=message,output=result)
    else:
      return render_template('index.html')

      # return 'file uploaded successfully'

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 