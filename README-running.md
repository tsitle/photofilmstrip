# PhotoFilmStrip - Running the Application

**PhotoFilmStrip** creates movies out of your pictures in just 3 steps.  
Simply select a couple of images, maybe add some music and then render the video.  
You can also edit the image transitions, add effects to the images and change the
time each image is displayed.

The source code for this application can be found at the [PhotoFilmStrip GitHub Repository](https://github.com/tsitle/photofilmstrip/).

## MS Windows

Take the `photofilmstrip-x.y.z-portable_win64.zip` file, extract it and run `PhotoFilmStrip.exe`.  
If you want to render videos from existing projects on the command line use `PhotoFilmStrip-cli.exe`.

You could also use the `photofilmstrip-x.y.z-portable_generic.zip` distribution file.  
But in that case you'll have to install MSYS2 and all the dependencies before using the application.  
See [README-compiling.md](https://github.com/tsitle/photofilmstrip/blob/master/README-compiling.md) for instructions on how to do that.  
Once the dependencies are installed you can start the application by executing `> run-gui.bat`
(or `$ ./run-gui.sh` from a UCRT64 terminal).  
If you want to render videos from existing projects on the command line use `> run-cli.bat`
(or `$ ./run-cli.sh` from a UCRT64 terminal).

## Debian Linux (and derivatives)

Take the `photofilmstrip-x.y.z-portable_generic.zip` file and extract it.  
Then run `$ ./y-install_depso.sh` to install the dependencies.

Start the application by executing `$ ./run-gui.sh`.  
If you want to render videos from existing projects on the command line use `$ ./run-cli.sh`.

## macOS

**PhotoFilmStrip** is not supported on macOS.  
