FBIQRServer
---
##How to use

Linux: Do 'sudo ./fbiqrserver <ciafolder> <port>' inside the project folder
Windows: Drag CIA folder over 'fbiqrserver.bat' (untested for now)

Then visit http://localhost in your favorite browser. You should see your QR codes.
 
Note: port defaults to 80 if not provided. 

##Customization

Just edit the files in the /preset folder if you wish to make things prettier.
Right now it just shows a bare-bones page with codes.

##Screenshot
![Following the latest trends in webdesign..](https://s30.postimg.org/wgslgb335/Screenshot_from_2017_01_16_14_58_17.png)

##Concerns

* Superuser is needed to open sockets. Windows will probably also throw a warning somewhere.
* Some files will be made in the folder you provide as the CIA folder. These are removed if you terminate the program normally (CTRL+C)

##Planned

* Actual Windows support
* Generate mixed QR-codes from subfolder

##Credits

[Davidshimjs](https://github.com/davidshimjs) - [QRcodejs](https://davidshimjs.github.io/qrcodejs/)
