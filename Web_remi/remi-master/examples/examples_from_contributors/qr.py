#!/usr/bin/python3.7

import ssl
import remi.gui as gui
from remi import start, App
from PIL import Image
import io
import base64
from pyzbar.pyzbar import decode

class Camera(App):
    def __init__(self, *args, **kwargs):
        super(Camera, self).__init__(*args)

    def video_widgets(self):
        width = '300'
        height = '300'
        self.video = gui.Widget(_type='video')
        self.video.style['overflow'] = 'hidden'
        self.video.attributes['autoplay'] = 'true'
        self.video.attributes['width'] = width
        self.video.attributes['height'] = height

    def video_start(self, widget, callback_function):
        self.execute_javascript("""
            var params={};
            var frame = 0;
            document.video_stop = false;
	    const video = document.querySelector('video');
	    video.setAttribute("playsinline", true);
	    const canvas = document.createElement('canvas');
	    navigator.mediaDevices.getUserMedia({video: { facingMode: { ideal: "environment" } }, audio: false}).
	    then((stream) => {video.srcObject = stream});
	    const render = () => {
                if (document.video_stop) { return; }
                if (frame==90) {
                    canvas.width = video.videoWidth;
                    canvas.height = video.videoHeight;
	            canvas.getContext('2d').drawImage(video, 0, 0);
		    params['image']=canvas.toDataURL().split(',')[1];
		    remi.sendCallbackParam('%(id)s','%(callback_function)s',params);
                    frame = 0;
                }
                frame+=1;
		requestAnimationFrame(render);
            }
            requestAnimationFrame(render);
    """%{'id':str(id(self)), 'callback_function': str(callback_function)})

    def video_stop(self, widget):
        self.execute_javascript("""
            document.video_stop = true;
            const video = document.querySelector('video');
            video.srcObject.getTracks()[0].stop();
        """)

    def process_image(self, **kwargs):
        try:
            image = Image.open(io.BytesIO(base64.b64decode(kwargs['image'])))
        except Exception:
            return

        qr_code_list = decode(image)
        if len(qr_code_list)>0:
            qr_code_data = qr_code_list[0][0].decode('utf-8')
            self.qr_label.set_text(qr_code_data)
        return

    def main(self):
        self.video_widgets()
        screen = [self.video]
        start_button = gui.Button('Start Video')
        start_button.onclick.do(self.video_start, 'process_image')
        screen.append(start_button)
        stop_button = gui.Button('Stop Video')
        stop_button.onclick.do(self.video_stop)
        screen.append(stop_button)
        self.qr_label = gui.Label('No QR code detected')
        screen.append(self.qr_label)

        return gui.VBox(children=screen)

if __name__ == "__main__":
    start(Camera,
            certfile='./ssl_keys/fullchain.pem',
            keyfile='./ssl_keys/privkey.pem',
            ssl_version=ssl.PROTOCOL_TLSv1_2,
            address='0.0.0.0',
            port=2020,
            multiple_instance=True,
            enable_file_cache=True,
            start_browser=False,
            debug=False)
