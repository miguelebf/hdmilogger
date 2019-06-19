###############################
#                             #
#  Author: Miguel Bustamante  #
#  Server WBU v 0.1           #
#                             #
###############################
import socket
import os
import sys
import subprocess

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=9999
host = socket.gethostname()
try:
	# Bindea el puerto
        server_socket.bind((host, port))
        # Cola de hasta 1 peticiones 
        server_socket.listen(1)
        # Espera por el cliente 
        print("[+] Waiting connection with HDMILogger...")
        # Acepta la coneccion 
        connection = server_socket.accept()[0].makefile('rb')
        print("[+]Connection has been established with HDMILogger")

	try:
		# Run a viewer with an appropriate command line. Uncomment the mplayer
		# version if you would prefer to use mplayer instead of VLC
		cmdline = ['vlc', '--demux', 'h264', '-']
		#cmdline = ['mplayer', '-fps', '25', '-cache', '1024', '-']
		player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
		while True:
		    # Repeatedly read 1k of data from the connection and write it to
		    # the media player's stdin
		    data = connection.read(1024)
		    if not data:
			break
		    player.stdin.write(data)
	finally:
		connection.close()
		server_socket.close()
		player.terminate()
except:
	print("Adios")
	

    
