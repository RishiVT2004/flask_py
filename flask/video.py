from flask import Flask,render_template,Response
import cv2

app=Flask(__name__)
web_camera=cv2.VideoCapture(0) # (0) -> default webcam 

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=web_camera.read() #generate 2 variable from gen_frame() [success is boolean in nature]
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            #encoding codes in terms of jpg
            # ret -> return , cv2.imencode encodes image to memory buffer...
            # omly buffer will be passed to frontend and display the frames 
            frame=buffer.tobytes()
            #return frame -> will only read once 

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        #yield helps to continously return frames along with content types 


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)
