from flask import Flask, render_template, Response
from camera import Video

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/style')
def style():
    return render_template('style.html')

@app.route('/gambar')
def gambar():
    return render_template('gambar.html')

@app.route('/about')
def about():
    return render_template('about.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\rm\n')

@app.route('/video')

def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(debug=True)