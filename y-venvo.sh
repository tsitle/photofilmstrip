#!/usr/bin/env bash

#
# by TS, Dec 2024
#

VAR_MYNAME="$(basename "$0")"

case "${OSTYPE}" in
	linux*)
		VENV_PATH="venv-lx"
		;;
	darwin*)
		VENV_PATH="venv-mac"
		;;
	msys*)
		VENV_PATH="venv-win"
		;;
	*)
		echo "${VAR_MYNAME}: Error: Unknown OSTYPE '${OSTYPE}'" >>/dev/stderr
		exit 1
		;;
esac

if [ -d "${VENV_PATH}" ]; then
	exit 0
fi

case "${OSTYPE}" in
	msys*|linux*)
		# create virtualenv - it is important to use the system-site-packages here. Otherwise Python would try
		#   to build the packages and that would fail miserably
		echo "${VAR_MYNAME}: ---------------------------"
		echo -e "${VAR_MYNAME}: Creating VENV in '${VENV_PATH}'...\n"
		python3 -m venv --system-site-packages "${VENV_PATH}" || exit 1
		;;
	*)
		# create virtualenv - without system-site-packages
		echo "${VAR_MYNAME}: ---------------------------"
		echo -e "${VAR_MYNAME}: Creating VENV in '${VENV_PATH}'...\n"
		python3 -m venv "${VENV_PATH}" || exit 1
		;;
esac

case "${OSTYPE}" in
	msys*)
		echo -e "\n${VAR_MYNAME}: ---------------------------"
		echo -e "${VAR_MYNAME}: Upgrading PIP...\n"
		"${VENV_PATH}/bin/python3.exe" -m pip install --upgrade pip || exit 1

		# it should not be necessary to build any packages at all. but leaving the code here just in case
		#echo -e "\n${VAR_MYNAME}: ---------------------------"
		#echo -e "${VAR_MYNAME}: Setting CFLAGS, LDFLAGS, CMAKE_C_COMPILER and CMAKE_CXX_COMPILER\n"
		#export CFLAGS=-I/ucrt64/include
		#export LDFLAGS=-L/ucrt64/lib
		#export CMAKE_C_COMPILER=/ucrt64/bin/gcc
		#export CMAKE_CXX_COMPILER=/ucrt64/bin/g++
		#TMP_CFLAGSDIR="$(echo -n "$CFLAGS" | cut -c3-)"
		#if [ ! -d "${TMP_CFLAGSDIR}" ]; then
		#	echo "${VAR_MYNAME}: CFLAGS dir '${TMP_CFLAGSDIR}' not found!" >>/dev/stderr
		#	exit 1
		#fi
		;;
esac

echo -e "\n${VAR_MYNAME}: ---------------------------"
echo -e "${VAR_MYNAME}: Installing requirements from 'requirements.txt'...\n"
"${VENV_PATH}/bin/python3" -m pip install -r requirements.txt || exit 1

if [ -f "requirements_dev.txt" ]; then
	echo -e "\n${VAR_MYNAME}: ---------------------------"
	echo -e "${VAR_MYNAME}: Installing requirements from 'requirements_dev.txt'...\n"
	"${VENV_PATH}/bin/python3" -m pip install -r requirements_dev.txt || exit 1
fi

case "${OSTYPE}" in
	msys*)
		echo -e "\n${VAR_MYNAME}: ---------------------------"
		echo "${VAR_MYNAME}: Modifying local cairosvg package"
		TMP_PYTHON_VER="$(${VENV_PATH}/bin/python3 --version | cut -f2 -d\  | cut -f1-2 -d.)"
		TMP_CAIRO_PATH="${VENV_PATH}/lib/python${TMP_PYTHON_VER}/site-packages/cairosvg/__init__.py"
		if [ ! -f "${TMP_CAIRO_PATH}" ]; then
			echo "${VAR_MYNAME}: Could not find '${TMP_CAIRO_PATH}'. Aborting." >>/dev/stderr
			exit 1
		fi
		TMP_CAIRO_VERS="${VENV_PATH}/lib/python${TMP_PYTHON_VER}/site-packages/cairosvg/VERSION"
		if [ ! -f "${TMP_CAIRO_VERS}" ]; then
			echo "${VAR_MYNAME}: Could not find '${TMP_CAIRO_VERS}'. Aborting." >>/dev/stderr
			exit 1
		fi
		TMP_CAIRO_VERS="$(tr -d "[:space:]" < "${TMP_CAIRO_VERS}" | tr -d "[:cntrl:]")"
		sed -i -e "s;^VERSION = __version__ = (ROOT / 'VERSION').read_text().strip()$;VERSION = __version__ = \"${TMP_CAIRO_VERS}\"  # VERSION = __version__ = (ROOT / 'VERSION').read_text().strip();g" "${TMP_CAIRO_PATH}" || exit 1
		;;
esac

echo -e "\n${VAR_MYNAME}: ---------------------------"
echo -e "${VAR_MYNAME}: Done.\n"

exit 0
