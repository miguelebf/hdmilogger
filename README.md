# HDMILogger
![Supported Python versions](https://img.shields.io/badge/python-3.5-orange.svg)  ![Supported OS](https://img.shields.io/badge/Tested%20On-Ubuntu_18.04-yellow.svg)

# Cómo funciona?
 El dispositivo se conecta en uno de los extremos del cable hdmi y reenvia la senal por la salida hdmi y tambien al cliente a través de internet.
 
 ![](https://github.com/miguelebf/hdmilogger/blob/master/Imagenes/hdmilogger.PNG?raw=true)


# Hardware
Para este prototipo se uso una Raspberry Zero W, un modulo B102 HDMI to CSI-2 bridge y el modulo Pisugar.  

### Rapberry Zero W
<img src="https://github.com/miguelebf/hdmilogger/blob/master/Imagenes/raspberry.jpg?raw=true" width="300" height="200" /> 



### B102 HDMI to CSI-2 bridge
<img src="https://github.com/miguelebf/hdmilogger/blob/master/Imagenes/b102.jpg?raw=true" width="300" height="200" /> 

 # Software
 Hay dos scripts un cliente(Ubuntu) y servidor(Raspberry W Zero), el cliente espera por la conexión del servidor y recive como video en vivo la senal del HDMI.

## Instalación y Uso 

```sh
En la Raspberry (Raspbian)
# git clone https://github.com/miguelebf/hdmilogger.git
# cd hdmilogger
# sudo python3 install.py
```
```sh
En el Cliente (Ubuntu)
# git clone https://github.com/miguelebf/hdmilogger.git
# cd hdmilogger
# python3 client.py
```

## To-do

 - Mejorar la autonomia(optimizacion del uso de la bateria)
 - Comunicación por gsm/gprs
 - Desarrollar un dispositivo final

Licencia
----

MIT
