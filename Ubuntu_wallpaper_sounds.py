from typing import SupportsComplex
import easygui
from easygui import *
import time
import datetime
from datetime import datetime
import sys
import os

#openfile = easygui.fileopenbox(msg="This is the file opening window", title="File Open", default='*', filetypes=["*.jpg", "*.jpeg", "*.png", "*.bmp", "*.pbm", "*.pgm", "*.ppm", "*.sr", "*.ras", "*.jpe", "*.jp2", "*.tiff", "*.tif", multiple=True)

def mainprogram():

    msg = "      UBUNTU LINUX LOGIN SCREEN, DESKTOP AND SOUND CONSOLE\n\n      THIS CONSOLE ENABLES YOU TO CHANGE THE DEFAULT LOGIN SCREEN\n\n      SOUND, WALLPAPER, AND DESKTOP BACKGROUND WALLPAPER\n\n      CLICK OK, OR THE IMAGE TO PROCEED PLEASE..."
    title = "MAIN UBUNTU CUSTOMIZATION CONSOLE"
    ubuntu_penguin = "Ubuntu_linux_penguin.png"
    msgbox(msg=msg, title=title, image=ubuntu_penguin)

    def selection_panel():

        def exit_program_from_panel():

            warning = "warning2.png"
            msg = "Do you want to Quit the Program?"
            title = "Quit Program?"
            choices = ["Yes", "No"]
            choice = buttonbox(msg, title, choices, image=warning)
            if choice == "Yes":
                sys.exit(0)
            else:
                selection_panel()
                pass
    
        image = "ubuntu_18_image.png"
        title = "MAIN FILE FORMAT SELECTION PANEL"
        msg = "              SELECT THE DESIRED OPERATION USING THE BUTTONS BELOW\n\n\n"
        choices = [ "Ubuntu Login screen image", "Desktop background image", "Login screen sound or track", "EXIT PROGRAM"]
        choice = buttonbox(msg ,title, image=image, choices=choices)

        if choice == "Ubuntu Login screen image":

            try:

                openfile = easygui.fileopenbox(msg="Ubuntu Login screen image", title="File Open", default=None, filetypes=["*.png"], multiple=False)
                
                if ".png" in openfile:
                    print("Opened file: "+openfile+"\n")
                    msg = "   FILE OPENED IS: \n\n"+"   "+openfile+"\n\n   CLICK OK TO VIEW THE IMAGE YOU SELECTED TO PLACE IN THE LOGIN SCREEN\n\n"
                    title = "Ubuntu Login screen PNG image"
                    good = "good.png"
                    msgbox(msg=msg, title=title, image=good)
                    
                    msg = "   FILE OPENED IS A .PNG FILE FORMAT\n\n "
                    title = "Ubuntu Login screen PNG image file selector"
                    good = openfile
                    msgbox(msg=msg, title=title, image=openfile)
                    os.system('touch lightdm_login.sh')
                    with open('lightdm_login.sh', "a+") as f:
                        f.write('sudo -i << EOF\n')
                        f.write('xhost +SI:localuser:lightdm\n')
                        f.write('su lightdm -s /bin/bash\n')
                        f.write('gsettings set com.canonical.unity-greeter background '+openfile+'\n')
                        f.write('EOF\n')
                        f.write('echo "Exited root user"\n')
                    os.system('bash lightdm_login.sh')
                    time.sleep(1)
                    os.system('rm lightdm_login.sh')
                    selection_panel()

                else:
                    msg = "   ERROR: YOU MUST OPEN A VALID .PNG FORMAT FILE FOR THIS OPTION\n\n\n                              CLICK OK TO TRY AGAIN"
                    title = "ERROR, no valid file format opened"
                    redcross = "redcross.png"
                    msgbox(msg=msg, title=title, image=redcross)
                    mainprogram()

            except:
                selection_panel()

        if choice == "Desktop background image":
            
            try:

                openfile = easygui.fileopenbox(msg="Desktop background image", title="File Open", default=None, filetypes=["*.png"], multiple=False)
                
                if ".png" in openfile:
                    print("Opened file: "+openfile+"\n")
                    msg = "   FILE OPENED IS: \n\n"+"   "+openfile+"\n\n   CLICK OK TO VIEW THE IMAGE YOU SELECTED TO PLACE AS THE DESKTOP WALLPAPER\n\n"
                    title = "Ubuntu Login screen PNG image"
                    good = "good.png"
                    msgbox(msg=msg, title=title, image=good)

                    msg = "   FILE OPENED IS A .PNG FILE FORMAT\n\n "
                    title = "Desktop background image file selector"
                    good = openfile
                    msgbox(msg=msg, title=title, image=openfile)
                    os.system('gsettings set org.gnome.desktop.background picture-uri file://'+openfile)
                    selection_panel()

                else:
                    msg = "   ERROR: YOU MUST OPEN A VALID .PNG FORMAT FILE FOR THIS OPTION\n\n\n                              CLICK OK TO TRY AGAIN"
                    title = "ERROR, no valid file format opened"
                    redcross = "redcross.png"
                    msgbox(msg=msg, title=title, image=redcross)
                    mainprogram()
                    
            except:
                selection_panel()

        if choice == "Login screen sound or track":

            try:

                openfile = easygui.fileopenbox(msg="Login screen sound or track", title="File Open", default=None, filetypes=["*.ogg"], multiple=False)
                
                if ".ogg" in openfile:

                    print("Opened file: "+openfile+"\n")
                    msg = "FILE OPENED IS: \n\n"+"   "+openfile+"\n\n   THIS IS A VALID .OGG FILE. CLICK OK TO CHANGE THE SOUND FILE NOW, OR CLOSE THE WINDOW TO ABORT"
                    title = "OGG sound file or track selector"
                    good = "good.png"
                    msgbox(msg=msg, title=title, image=good)
                    sudocp="sudo cp " 
                    systemready=" system-ready.ogg"
                    os.system(sudocp+openfile+systemready)
                    os.system('sudo mv /usr/share/sounds/ubuntu/stereo/system-ready.ogg system-ready-old.ogg')
                    os.system('sudo mv system-ready.ogg /usr/share/sounds/ubuntu/stereo/')
                    selection_panel()

                else:
                    msg = "   ERROR: YOU MUST OPEN A VALID .OGG FORMAT FILE FOR THIS OPTION\n\n\n                              CLICK OK TO TRY AGAIN"
                    title = "ERROR, no valid file format opened"
                    redcross = "redcross.png"
                    msgbox(msg=msg, title=title, image=redcross)
                    selection_panel()

            except:
                selection_panel()

        if choice == "EXIT PROGRAM":
            exit_program_from_panel()

    selection_panel()

mainprogram()

