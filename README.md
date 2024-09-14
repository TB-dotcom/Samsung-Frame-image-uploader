This is a simple script for Windows that takes an image file as a command line parameter and sends it to a Samsung Frame in Art mode.  
Usage: pictotv.bat image.jpg  

Configuration:   
  -adjust the TV's IP address in pictotv.py (it's hardcoded)  
  -adjust the path in pictotv.bat  
  
Requirements:  
  -python  
  -samsungtvws library installed  
  
Conditions:  
  -TV needs to be on (can be in Art mode)  
  -not all TV's will work  

The samsungtvws library can be found in several repositories, and may differ a bit -most importantly- in relation to the TV's firmware version.  
  https://github.com/NickWaterton/samsung-tv-ws-api - I used this one and it works with my TV's FW 1640   
  https://github.com/xchwarze/samsung-tv-ws-api - seems to work with newer FW only  
  https://github.com/thypon/samsung-tv-ws-api - with a tweek for older FW   

If it does not work, it might be the problem with the upload service in the API - this can be tested in a Python console using the API commands directly, the upload command actually.   
Uninstalling/installing other repositories may help. All allowed me to connect and e.g. get info on current image, but only one handled uploads correctly.    
  
A nice enhancement is to have a chosen image being uploaded to the Frame from the RMB context menu in File Explorer. In short, you can achieve this by adding a new entry in the Windows Registry:  
  -run regedit  
  -find \HKEY_CLASSES_ROOT\SystemFileAssociations\image\shell  
  -under it add a new key SendToFrame (or any other name of your choice) with a value "Send to Frame" (or any other you want to be displated in the menu)  
  -under the above key add a sub-key named "command" with a value "C:\Users\...\pictotv.bat" "%1" adjusting the path   
  The option will appear in the RMB context menu, although under More options  
