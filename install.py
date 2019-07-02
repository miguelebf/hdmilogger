#Miguel Bustamante v0.1
##Imports
from subprocess import call


#Functions
def modifyLine(file,find,replace):
	with open(file, "r") as f:
		lines = (line.rstrip() for line in f)
		altered_lines = [replace if line.split("=")[0]==find else line for line in lines]
	with open(file, "w") as f:
		f.write('\n'.join(altered_lines) + '\n')
		f.close()
 
#Modify  desktop-items-0.conf
modifyLine('/home/pi/.config/pcmanfm/LXDE-pi/desktop-items-0.conf','wallpaper_mode','wallpaper_mode=color')
