import socket
import time
import picamera

# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)
client_socket = socket.socket()


client_socket.connect(('my_server', 8000))
connection = client_socket.makefile('wb')

while True:
    try:
        with picamera.PiCamera() as camera:
            if camera.start_preview(): 
                time.sleep(2)
            
            camera.start_recording(connection, format='h264')
            #camera.stop_recording()
    finally:
        connection.close()
        client_socket.close()