#!/usr/bin/env bash

#
# by TS, Dec 2024
#

VAR_MYNAME="$(basename "$0")"

install_lx() {
	sudo apt-get install -y \
		python3-venv \
		python3-wheel \
		python3-pip \
		python3-gi \
		pkg-config \
		|| exit 1
	sudo apt-get install -y \
		python3-wxgtk4.0 \
		|| exit 1
	sudo apt-get install -y \
		python3-gst-1.0 \
		python3-ges-1.0 \
		gir1.2-gstreamer-1.0 \
		gir1.2-gst-plugins-base-1.0 \
		gstreamer1.0-plugins-good \
		gstreamer1.0-plugins-ugly \
		gstreamer1.0-tools \
		gstreamer1.0-libav \
		|| exit 1
}

install_mac() {
	echo "${VAR_MYNAME}: PhotoFilmStrip is not compatible with macOS"
}

install_win() {
	# update package database from server
	pacman -Sy || exit 1
	#
	pacman -S --noconfirm \
		mingw-w64-ucrt-x86_64-gtk4 \
		mingw-w64-ucrt-x86_64-python \
		mingw-w64-ucrt-x86_64-python-pip \
		mingw-w64-ucrt-x86_64-python-gobject \
		mingw-w64-ucrt-x86_64-gobject-introspection \
		|| exit 1
	# for pillow:
	pacman -S --noconfirm \
		mingw-w64-ucrt-x86_64-zlib \
		mingw-w64-ucrt-x86_64-libjpeg-turbo \
		mingw-w64-ucrt-x86_64-libtiff \
		mingw-w64-ucrt-x86_64-libpng \
		mingw-w64-ucrt-x86_64-freetype \
		mingw-w64-ucrt-x86_64-libwebp \
		|| exit 1
	# for wxPython (install separately):
	pacman -S --noconfirm \
		mingw-w64-ucrt-x86_64-python-attrdict3 \
		|| exit 1
	# install wxPython itself
	pacman -S --noconfirm \
		mingw-w64-ucrt-x86_64-wxPython \
		|| exit 1
	# the current version of pycparser (2.22) doesn't work with cffi.
	#   so we need use an older version here
	python3 -m pip install pycparser==2.14 || exit 1
	# install cffi and ignore its dependencies
	#   (otherwise it would install the current version of pycparser)
	pacman -Sdd --noconfirm \
		mingw-w64-ucrt-x86_64-python-cffi \
		|| exit 1
	# Cairo renderer
	pacman -S --noconfirm \
		mingw-w64-ucrt-x86_64-python-cairo \
		|| exit 1
	# for SVG to BMP conversions (alternative for cairosvg):
	#pacman -S --noconfirm \
	#	mingw-w64-ucrt-x86_64-python-svglib \
	#	mingw-w64-ucrt-x86_64-python-rlpycairo \
	#	|| exit 1
	# Gstreamer stuff
	pacman -S --noconfirm \
		mingw-w64-ucrt-x86_64-gst-python \
		mingw-w64-ucrt-x86_64-gst-plugins-bad \
		mingw-w64-ucrt-x86_64-gst-plugins-base \
		mingw-w64-ucrt-x86_64-gst-plugins-good \
		mingw-w64-ucrt-x86_64-gst-plugins-ugly \
		mingw-w64-ucrt-x86_64-gst-libav \
		mingw-w64-ucrt-x86_64-gst-devtools \
		mingw-w64-ucrt-x86_64-gst-editing-services \
		|| exit 1
}

case "${OSTYPE}" in
	linux*)
		install_lx
		;;
	darwin*)
		install_mac
		;;
	msys*)
		install_win
		;;
	*)
		echo "${VAR_MYNAME}: Error: Unknown OSTYPE '${OSTYPE}'" >>/dev/stderr
		exit 1
		;;
esac

if [ -f "./y-installo_dev.sh" ]; then
	./y-installo_dev.sh || exit 1
fi

exit 0
