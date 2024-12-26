#
# Makefile for PhotoFilmStrip
#

DISPLAYNAME = PhotoFilmStrip
PY_SRC_ROOT_DIR = .
PY_PACKAGE_DIR = photofilmstrip

SHELL := bash

SCM_REV := $(shell git rev-parse --short HEAD)
LOC_OSTYPE := $(shell if [[ "$$OSTYPE" =~ ^linux.* ]]; then echo -n "lx"; else if [[ "$$OSTYPE" = darwin* ]]; then echo -n "mac"; else if [[ "$$OSTYPE" = msys* ]]; then echo -n "win"; else echo -n "error"; fi; fi; fi)

SPHINXOPTS =
SPHINXBUILD = sphinx-build
SPHINXSOURCEDIR = docs/help
SPHINXBUILDDIR = build/sphinx

all: clean compile test

# remove all generated files (except for 'res/images.py')
clean:
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v clean

# generate 'res/images.py', the translation units from 'po/*.po' into 'build/mo/', the sphinx help files into 'build/sphinx/'
#   and copy the source code into 'build/lib/' + 'build/scripts-x.yz/'
compile:
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v clean
	@if [ -z "$(SCM_REV)" ]; then \
		echo "Missing SCM_REV"; \
	else \
		echo SCM_REV="$(SCM_REV)"; \
		export SCM_REV="$(SCM_REV)"; \
		venv-$(LOC_OSTYPE)/bin/python3 setup.py -v build; \
	fi

# generate TAR ball with source code. also generates 'photofilmstrip.egg-info/*'.
#   will also do 'compile'
package-source:
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v clean
	@if [ -z "$(SCM_REV)" ]; then \
		echo "Missing SCM_REV"; \
	else \
		echo SCM_REV="$(SCM_REV)"; \
		export SCM_REV="$(SCM_REV)"; \
		venv-$(LOC_OSTYPE)/bin/python3 setup.py -v sdist; \
	fi

# build compiled MS Windows executable, ready to be used as portable application that includes all dependencies.
#   will also do 'compile'
build-winport:
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v clean
	@if [ -z "$(SCM_REV)" ]; then \
		echo "Missing SCM_REV"; \
	else \
		echo SCM_REV="$(SCM_REV)"; \
		export SCM_REV="$(SCM_REV)"; \
		venv-$(LOC_OSTYPE)/bin/python3 setup.py -v bdist_win; \
	fi

# generate ZIP file with compiled MS Windows executable, ready to be used as portable application that includes all dependencies.
#   will also do 'compile'
package-winport:
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v clean
	@if [ -z "$(SCM_REV)" ]; then \
		echo "Missing SCM_REV"; \
	else \
		echo SCM_REV="$(SCM_REV)"; \
		export SCM_REV="$(SCM_REV)"; \
		venv-$(LOC_OSTYPE)/bin/python3 setup.py -v bdist_winportzip; \
	fi

# run the unit tests
test:
	venv-$(LOC_OSTYPE)/bin/pylint --rcfile=.pylintrc --disable=W,R,C "$(PY_SRC_ROOT_DIR)/$(PY_PACKAGE_DIR)"

# generate the sphinx help files (will also be done by 'compile')
generate-help:
	@#@test -d "$(SPHINXBUILDDIR)" || mkdir -p "$(SPHINXBUILDDIR)"
	@#@venv-$(LOC_OSTYPE)/bin/$(SPHINXBUILD) -M html "$(SPHINXSOURCEDIR)" "$(SPHINXBUILDDIR)" $(SPHINXOPTS)
	venv-$(LOC_OSTYPE)/bin/python3 setup.py -v build_sphinx

# update translation units in 'po/*.po'
update-po:
	pygettext3 -o "po/$(DISPLAYNAME).pot" -v "$(PY_SRC_ROOT_DIR)/$(PY_PACKAGE_DIR)"
	find po/ -name "*.po" -exec msgmerge --backup=none --update {} "po/$(DISPLAYNAME).pot" ';'

# output the current application version
versioninfo:
	@venv-$(LOC_OSTYPE)/bin/python3 -c "from photofilmstrip import Constants; print(Constants.APP_VERSION)"
