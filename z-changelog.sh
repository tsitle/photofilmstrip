#!/usr/bin/env bash

#
# by TS, Jan 2025
#

_printUsage() {
	{
		echo -e "\nUsage: $(basename "$0") <FROM_REV>"
		echo "Example: $(basename "$0") ffa6b3c3"
	} >>/dev/stderr
	exit 1
}

if [ $# -lt 1 ]; then
	echo "Missing argument <FROM_REV>" >>/dev/stderr
	_printUsage
fi
if [ $# -gt 1 ]; then
	echo "Too many arguments" >>/dev/stderr
	_printUsage
fi
OPT_FROM_REV="$1"

LCFG_OFN="CHANGELOG-temp.md"

echo -e "Generating '${LCFG_OFN}'...\n"
docker run \
	--mount src="$(pwd)",target=/home/git-changelog-command-line,type=bind \
	tomasbjerre/git-changelog-command-line:2.4.1 \
	-std \
	--from-revision "${OPT_FROM_REV}" \
	> "${LCFG_OFN}" || exit 1
echo "Done."
