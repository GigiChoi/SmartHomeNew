
from flask import Flask
from flask import send_file
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './output/'
ALLOWED_EXTENSIONS = {'mp4', 'text'}

  
# Flask Constructor
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
  
# decorator to associate 
# a function with the url
@app.route("/LightsOn/")
def returnLightsOn():

   try:
      return send_file('./Expert Gestures/H-LightOn.mp4', attachment_filename='H-LightOn.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route("/LightsOff/")
def returnLightsOff():

   try:
      return send_file('./Expert Gestures/H-LightOff.mp4', attachment_filename='H-LightOff.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route("/FanOn/")
def returnFanOn():

   try:
      return send_file('./Expert Gestures/H-FanOn.mp4', attachment_filename='H-FanOn.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route("/FanOff/")
def returnFanOff():

   try:
      return send_file('./Expert Gestures/H-FanOff.mp4', attachment_filename='H-FanOff.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route("/FanUp/")
def returnFanUp():

   try:
      return send_file('./Expert Gestures/H-IncreaseFanSpeed.mp4', attachment_filename='H-IncreaseFanSpeed.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route("/FanDown/")
def returnFanDown():

   try:
      return send_file('./Expert Gestures/H-DecreaseFanSpeed.mp4', attachment_filename='H-DecreaseFanSpeed.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route("/SetThermo/")
def returnSetThermo():

   try:
      return send_file('./Expert Gestures/H-SetThermo.mp4', attachment_filename='H-SetThermo.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route("/Num0/")
def returnNum0():

   try:
      return send_file('./Expert Gestures/H-0.mp4', attachment_filename='H-0.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route("/Num1/")
def returnNum1():

   try:
      return send_file('./Expert Gestures/H-1.mp4', attachment_filename='H-1.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route("/Num2/")
def returnNum2():

   try:
      return send_file('./Expert Gestures/H-2.mp4', attachment_filename='H-2.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route("/Num3/")
def returnNum3():

   try:
      return send_file('./Expert Gestures/H-3.mp4', attachment_filename='H-3.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route("/Num4/")
def returnNum4():

   try:
      return send_file('./Expert Gestures/H-4.mp4', attachment_filename='H-4.mp4')

   except Exception as e:
      return str("Download Failure")
   
@app.route("/Num5/")
def returnNum5():

   try:
      return send_file('./Expert Gestures/H-5.mp4', attachment_filename='H-5.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route("/Num6/")
def returnNum6():

   try:
      return send_file('./Expert Gestures/H-6.mp4', attachment_filename='H-6.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route("/Num7/")
def returnNum7():

   try:
      return send_file('./Expert Gestures/H-7.mp4', attachment_filename='H-7.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route("/Num8/")
def returnNum8():

   try:
      return send_file('./Expert Gestures/H-8.mp4', attachment_filename='H-8.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route("/Num9/")
def returnNum9():

   try:
      return send_file('./Expert Gestures/H-9.mp4', attachment_filename='H-9.mp4')

   except Exception as e:
      return str("Download Failure")

@app.route('/', methods = ['GET', 'POST'])
def handle_request():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=45457)