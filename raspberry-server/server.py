import socket
import time
import picamera
import threading

# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)
port=8000
host='192.168.0.5'

def start_view(camera):
    camera.start_preview():
    time.sleep(0)

while True:
    try:
        with picamera.PiCamera() as camera:
            hiloPreview = threading.Thread(target=start_preview(camera))
            hiloPreview.start()
            while True:
                try:
                    client_socket = socket.socket()
                    client_socket.connect((host, port))
                    connection = client_socket.makefile('wb')
                    camera.start_recording(connection, format='h264')
                except:
                    camera.stop_recording()
                    connection.close()
                    client_socket.close()
                    continue
    except:
        hiloPreview.stop()
        continue