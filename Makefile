#
# Makefile for PhotoFilmStrip
#

DISPLAYNAME = PhotoFilmStrip
PY_SRC_ROOT_DIR = .
PY_PACKAGE_DIR = photofilmstrip

SHELL := bash

SCM_REV := $(shell if [[ -f ".git/config" ]]; then git rev-parse --short HEAD; else echo -n; fi)
LOC_OSTYPE := $(shell if [[ "$$OSTYPE" =~ ^linux.* ]]; then echo -n "lx"; else if [[ "$$OSTYPE" = darwin* ]]; then echo -n "mac"; else if [[ "$$OSTYPE" = msys* ]]; then echo -n "win"; else echo -n "error"; fi; fi; fi)

SPHINXOPTS =
SPHINXBUILD = sphinx-build
SPHINXSOURCEDIR = docs/help
SPHINXBUILDDIR = build/sphinx

all: clean compile test

# remove all generated files (except for 'res/images.py')
clean:
	@if [ ! -d "venv-$(LOC_OSTYPE)" ]; then \
		./y-venvo.sh || exit 1; \
	fi
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v clean

# generate 'res/images.py', the translation units from 'po/*.po' into 'build/mo/', the sphinx help files into 'build/sphinx/'
#   and copy the source code into 'build/lib/' + 'build/scripts-x.yz/'
compile:
	@if [ ! -d "venv-$(LOC_OSTYPE)" ]; then \
		./y-venvo.sh || exit 1; \
	fi
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v clean
	@if [ -z "$(SCM_REV)" ]; then \
		echo "Warning: Missing SCM_REV"; \
	else \
		echo SCM_REV="$(SCM_REV)"; \
		export SCM_REV="$(SCM_REV)"; \
	fi
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v build

# generate TAR ball with source code. also generates 'photofilmstrip.egg-info/*'.
#   will also do 'compile'
package-source:
	@if [ ! -d "venv-$(LOC_OSTYPE)" ]; then \
		./y-venvo.sh || exit 1; \
	fi
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v clean
	@if [ -z "$(SCM_REV)" ]; then \
		echo "Warning: Missing SCM_REV"; \
	else \
		echo SCM_REV="$(SCM_REV)"; \
		export SCM_REV="$(SCM_REV)"; \
	fi
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v sdist

# build compiled MS Windows executable, ready to be used as portable application that includes all dependencies.
#   will also do 'compile'
build-winport:
	@if [ ! -d "venv-$(LOC_OSTYPE)" ]; then \
		./y-venvo.sh || exit 1; \
	fi
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v clean
	@if [ -z "$(SCM_REV)" ]; then \
		echo "Warning: Missing SCM_REV"; \
	else \
		echo SCM_REV="$(SCM_REV)"; \
		export SCM_REV="$(SCM_REV)"; \
	fi
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v bdist_win

# generate ZIP file with compiled MS Windows executable, ready to be used as portable application that includes all dependencies.
#   will also do 'compile'
package-winport:
	@if [ ! -d "venv-$(LOC_OSTYPE)" ]; then \
		./y-venvo.sh || exit 1; \
	fi
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v clean
	@if [ -z "$(SCM_REV)" ]; then \
		echo "Warning: Missing SCM_REV"; \
	else \
		echo SCM_REV="$(SCM_REV)"; \
		export SCM_REV="$(SCM_REV)"; \
	fi
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v bdist_winportzip

# generate ZIP file with compiled portable Python code for Linux and MS Windows.
#   will also do 'compile'
package-interpreterportzip:
	@if [ ! -d "venv-$(LOC_OSTYPE)" ]; then \
		./y-venvo.sh || exit 1; \
	fi
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v clean
	@if [ -z "$(SCM_REV)" ]; then \
		echo "Warning: Missing SCM_REV"; \
	else \
		echo SCM_REV="$(SCM_REV)"; \
		export SCM_REV="$(SCM_REV)"; \
	fi
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v sdist_interpreterportzip

# run the unit tests
test:
	@if [ ! -d "venv-$(LOC_OSTYPE)" ]; then \
		./y-venvo.sh || exit 1; \
	fi
	venv-$(LOC_OSTYPE)/bin/pylint --rcfile=.pylintrc --disable=W,R,C "$(PY_SRC_ROOT_DIR)/$(PY_PACKAGE_DIR)"

# generate the sphinx help files (will also be done by 'compile')
generate-help:
	@if [ ! -d "venv-$(LOC_OSTYPE)" ]; then \
		./y-venvo.sh || exit 1; \
	fi
	@#@test -d "$(SPHINXBUILDDIR)" || mkdir -p "$(SPHINXBUILDDIR)"
	@#@venv-$(LOC_OSTYPE)/bin/$(SPHINXBUILD) -M html "$(SPHINXSOURCEDIR)" "$(SPHINXBUILDDIR)" $(SPHINXOPTS)
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v build_sphinx

# update translation units in 'po/*.po'
update-po:
	@if [ ! -d "venv-$(LOC_OSTYPE)" ]; then \
		./y-venvo.sh || exit 1; \
	fi
	pygettext3 -o "po/$(DISPLAYNAME).pot" -v "$(PY_SRC_ROOT_DIR)/$(PY_PACKAGE_DIR)"
	find po/ -name "*.po" -exec msgmerge --backup=none --update {} "po/$(DISPLAYNAME).pot" ';'

# output the current application version
versioninfo:
	@if [ ! -d "venv-$(LOC_OSTYPE)" ]; then \
		./y-venvo.sh || exit 1; \
	fi
	@venv-$(LOC_OSTYPE)/bin/python3 -c "from photofilmstrip import Constants; print(Constants.APP_VERSION)"
