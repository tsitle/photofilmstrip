# PhotoFilmStrip - Compiling the Application

The current version of **PhotoFilmStrip** is compatible with Python 3.12.

## MS Windows

Because of the dependency to PyGObject it appears necessary to use MSYS2.  

### MSYS2 installation

- install [MSYS2](https://www.msys2.org/)
- add the following paths to your PATH in the System Environment Variables (in the MS Windows System Properties):  
	- `c:\msys64\ucrt64\bin`
	- `C:\msys64\usr\bin`
- open UCRT64 terminal (`C:\msys64\ucrt64.exe`)
- change directory to the **PhotoFilmStrip** repository  
	e.g. `$ cd /c/Users/<USERNAME>/Documents/photofilmstrip`
- run `$ ./y-install_depso.sh` - this will install all dependencies via *pacman*

See [PyGObject Getting Started](https://pygobject.gnome.org/getting_started.html#windows) for more information
on PyGObject and MSYS2.

### Some useful commands for *pacman*

```
Search for package:
$ pacman -Ss <SEARCH_TERM>

Show manually installed packages:
$ pacman -Qe

Remove package:
$ pacman -Rcns <PACKAGE>

Update package database from server:
$ pacman -Sy

Upgrade installed packages:
$ pacman -Suy
```

### Compiling the portable executable

To compile and package the portable executable for MS Windows, run

```
# this will create a ZIP file in 'dist/'
$ make package-winport
```

To only compile the portable executable for MS Windows, run

```
# this will create a subdirectory in 'build/dist_portable_win/'
$ make build-winport
```

## Debian Linux (and derivatives)

First run `$ ./y-install_depso.sh` to install all dependencies via *apt-get*.

Then run

```
# this will create a TAR ball in 'dist/'
$ make package-interpreterportzip
```

## macOS

**PhotoFilmStrip** is not supported on macOS.  
But you can install some of the Python packages in order to be able to
properly use an IDE for development.

## All OSes

First run `$ ./y-install_depso.sh` to install all dependencies.

Then create a source distribution ZIP file by running

```
# this will create a TAR ball in 'dist/'
$ make package-source
```
