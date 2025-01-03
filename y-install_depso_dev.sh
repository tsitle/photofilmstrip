#!/usr/bin/env bash

#
# by TS, Dec 2024
#

VAR_MYNAME="$(basename "$0")"

install_lx() {
	sudo apt-get install -y \
		git \
		libxt-dev \
		libgirepository1.0-dev \
		libcairo2-dev \
		gettext \
		|| exit 1
}

install_mac() {
	# We install only enough packages to use our IDE for development.
	# PhotoFilmStrip is not compatible with macOS.
	brew install \
		git \
		pkg-config \
		gettext \
		|| exit 1
	brew install \
		gobject-introspection \
		|| exit 1
}

install_win() {
	# update package database from server
	pacman -Sy || exit 1
	#
	pacman -S --noconfirm \
		git \
		|| exit 1
	pacman -S --noconfirm \
		base-devel \
		|| exit 1
	#pacman -S --noconfirm \
	#	mingw-w64-ucrt-x86_64-toolchain \
	#	|| exit 1
	pacman -S --noconfirm \
		gettext \
		|| exit 1
	# install cx_freeze
	pacman -S --noconfirm \
		mingw-w64-ucrt-x86_64-python-cx-freeze \
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
