#Miguel Bustamante v0.1
##Imports
import os

#Functions
def modifyLine(file,find,replace):
	with open(file, "r") as f:
		lines = (line.rstrip() for line in f)
		altered_lines = [replace if line.split("=")[0]==find else line for line in lines]
	with open(file, "w") as f:
		f.write('\n'.join(altered_lines) + '\n')
		f.close()
 
#Modify  desktop-items-0.conf(Modify background to solid black colour)
modifyLine('/home/pi/.config/pcmanfm/LXDE-pi/desktop-items-0.conf','wallpaper_mode','wallpaper_mode=color')
modifyLine('/home/pi/.config/pcmanfm/LXDE-pi/desktop-items-0.conf','desktop_bg','desktop_bg=#000000000000')

#Reconfigure Pcmanfm
os.system('pcmanfm --reconfigure')
