# Ubuntu 18 Desktop Customization Console

# Ubuntu Desktop python console to customize lightdm login screen, login sound, and desktop background

# Author: Gustavo Wydler Azuaga - 08/13/2021

# NOTE: Screensots from the GUI program are available to view in the Screenshots folder

-----------------------------------------------------------------------------------------------------------

 Installation: 

- Clone repo to your /home/$USER/ path
- Copy all the .png files to the /home/$USER/ path
- Install python3.6: sudo apt-get install python3.6
- Import the following libraries in the python code:
  
    - from typing import SupportsComplex
    - import easygui
    - from easygui import *
    - import time
    - import datetime
    - from datetime import datetime
    - import sys
    - import os
    
- Provide no password in the /etc/sudoers/:
    
    - Access the sudoers file:
    - sudo nano /etc/sudoers/
    - <your_user>  ALL=(ALL) NOPASSWD:ALL
    - Save and exit.
    
- Open the Ubuntu_Customization_console.destkop file, and replace the command:

    - Exec=gnome-terminal -- python3.6 /home/$USER/Ubuntu_wallpaper_sounds.py
    
    - with:
    
    - Exec=gnome-terminal -- python3.6 /home/<your_user_here>/Ubuntu_wallpaper_sounds.py
    
    - Save and exit.
    
- Provide access permissions to the Ubuntu_Customization_console.destkop file:

    - sudo chmod +rx Ubuntu_Customization_console.destkop
    
- Turn the python file into an Ubuntu app:

    - sudo cp /home/$USER/Ubuntu_Customization_console.destkop /usr/share/applications/
    
- Run the python console from the apps bar.    

    
 

