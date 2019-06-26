# HDMILogger
![Supported Python versions](https://img.shields.io/badge/python-3.6-orange.svg)  ![Supported OS](https://img.shields.io/badge/Supported%20OS-Kali_Linux-yellow.svg)

# Cómo funciona?
 El dispositivo funciona como un rubber ducky de hak5 con la diferencia que se pueden enviar los Scripts por medio de internet.
 
 ![](https://github.com/miguelebf/hdmilogger/blob/master/Imagenes/hdmilogger.PNG?raw=true)


# Hardware
Para este prototipo se uso una Raspberry Zero W, un modulo B102 HDMI to CSI-2 bridge.  

### Rapberry Zero W
<img src="https://github.com/miguelebf/hdmilogger/blob/master/Imagenes/raspberry.jpg?raw=true" width="300" height="200" /> 



### B102 HDMI to CSI-2 bridge
<img src="https://github.com/miguelebf/hdmilogger/blob/master/Imagenes/b102.jpg?raw=true" width="300" height="200" /> 

 # Software
 Un programa escrito en python sirve como servidor socket, espera la conexión del dispistívo una vez conectado se puede modifcar, ver y enviar el script que se le enviará al dispositívo, el script que se enviara estara en la carpeta .../WBU/scritp.txt, el lenguaje que se usa es duckyscript  

## Instalación y Uso 
#### Hardware
- Conectar según el siguiente diagrama:
<img src="https://raw.githubusercontent.com/miguelebf/WBU/master/Imagenes/esquemaConexion.PNG" width="600" height="400" /> 
<img src="https://raw.githubusercontent.com/miguelebf/WBU/master/Imagenes/20180906_162647.jpg" width="600" height="400" /> 

- Subir los skechts al Arduino y al ESP(Nodemcu)

#### Software
```sh
# git clone https://github.com/miguelebf/WBU.git
# cd WBU
# python3 wbu.py
```

## To-do

 - Distribución del teclado (Keyboard Layouts) 
 - Comunicación por gsm/gprs
 - Desarrollar un dispositivo final

 ## Créditos

 - [WHID WiFi HID Injector](https://github.com/whid-injector/WHID) (funciones para convertir de Ducky Script a Arduino) 

Licencia
----

MIT
