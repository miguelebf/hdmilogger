import socket
import time
import picamera

# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)
port=8000
host='127.0.0.1'

while True:

    try:
        with picamera.PiCamera() as camera:
            if camera.start_preview(): 
                time.sleep(2)
                while True:
                    try:
                        #Conexcion 
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
        continue