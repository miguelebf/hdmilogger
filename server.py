import socket
import time
import picamera
import threading

port=8000
host='192.168.0.5'
camera=None
event=threading.Event()
connection=None
preview=False

def initPreview(camera):
    flag=True
    while flag:
        preview=False
        try:
            camera=picamera.PiCamera()
            camera.start_preview()
            print('Picamera Init')
            preview=True
            event.wait()
            flag=False 
        except Exception as e:
            preview=False
            event.set()
            print('Error Picamera ' + str(e))
            continue

def initConnection(connection):
    flag1=True
    while flag1:
        try:
            client_socket=socket.socket()
            client_socket.connect((host,port))
            connection=client_socket.makefile('wb')
            event.set()
            flag1=False
            return connection
        except Exception as e:
            print('Error connection ' + str(e))
            continue

def control():
    while True:
    
        try:
            picamera.PiCamera()
            event.set()
            preview=False
        except:
            continue
        
#Main Thread
while True:
    try:
        
        hilo1=threading.Thread(target=initPreview(camera))
        hiloControl=threading.Thread(target=control())
        hilo2=threading.Thread(target=initConnection(connection))
        hilo1.start()
        hiloControl.start()
        
        if preview:
            connect=hilo2.start()
            camera.start_recording(connect, format='h264')
    except Exception as e:
        print('Error hilo principal ' + str(e))
        continue