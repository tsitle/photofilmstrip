# -*- coding: utf-8 -*-
#
# PhotoFilmStrip - Creates movies out of your pictures.
#
# Copyright (C) 2011 Jens Goepfert
#

import base64
import glob
import stat
import sys
import os
import unittest
import zipfile
import logging
import shutil
from typing import List, Tuple, Final

from setuptools.command.build import build
from setuptools.command.sdist import sdist
from setuptools import setup
from setuptools import Command

try:
    from sphinx.application import Sphinx
except ImportError:
    Sphinx = None

try:
    from cx_Freeze.command.build_exe import build_exe as BuildExe
    from cx_Freeze import Executable
except ImportError:
    BuildExe = None
    Executable = None

from photofilmstrip import Constants

WORKDIR = os.path.dirname(os.path.abspath(sys.argv[0]))
MSGFMT = os.path.join(
        getattr(sys, "base_prefix", os.path.dirname(sys.executable)),
        "Tools",
        "i18n",
        "msgfmt.py"
    )
if os.path.isfile(MSGFMT):
    MSGFMT = [sys.executable, MSGFMT]
else:
    MSGFMT = ["msgfmt"]

tmpIs64Bit = (sys.maxsize > 2 ** 32)
if tmpIs64Bit:
    WIN_BIT_SUFFIX = "win64"
else:
    WIN_BIT_SUFFIX = "win32"

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

class PfsClean(Command):
    sub_commands = []
    user_options = []

    def _clean_project(self):
        paths_to_clean = [
                "build",
                "dist",
                "docs/help/_build",
                "photofilmstrip.egg-info",
                "photofilmstrip/_scmInfo.py",
            ]
        for path in paths_to_clean:
            if os.path.exists(path):
                if os.path.isdir(path):
                    gLogger.info(f"Removing path '{path}'")
                    shutil.rmtree(path)
                else:
                    gLogger.info(f"Removing file '{path}'")
                    os.remove(path)

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self._clean_project()

        for directory in (
                    os.path.join(WORKDIR, "build"),
                ):
            if os.path.exists(directory):
                try:
                    shutil.rmtree(directory)
                except FileNotFoundError:
                    pass

        for fname in (
                    os.path.join(WORKDIR, "version.info"),
                    os.path.join(WORKDIR, "MANIFEST"),
                ):
            if os.path.exists(fname):
                os.remove(fname)


class PfsScmInfo(Command):

    description = "generates _scmInfo.py in source folder"

    user_options = [
            ('scm-rev=', None, 'The SCM revision'),
        ]

    sub_commands = []

    def initialize_options(self):
        self.scm_rev = os.getenv("SCM_REV")

    def finalize_options(self):
        pass

    def run(self):
        if not self.scm_rev:
            # if not set in environment it hopefully was generated earlier
            # building deb with fakeroot has no SCM_REV var anymore
            try:
                import photofilmstrip._scmInfo
                self.scm_rev = photofilmstrip._scmInfo.SCM_REV  # pylint: disable=no-member, protected-access
            except ImportError:
                self.scm_rev = "src"

        if self.scm_rev != "src":
            fd = open(os.path.join("photofilmstrip", "_scmInfo.py"), "w")
            fd.write("SCM_REV = \"%s\"\n" % self.scm_rev)
            fd.close()


class PfsSdist(sdist):

    description = "create a distribution TAR ball of the source code"

    sub_commands = [
            ('scm_info', lambda x: True),
            ('build', lambda x: True),
        ] + sdist.sub_commands

    def run(self):
        outputFn1 = os.path.join("dist", f"photofilmstrip-{Constants.APP_VERSION_SUFFIX}.tar.gz")
        gLogger.info(f"Building source distribution TAR ball '{outputFn1}'...")
        sdist.run(self)
        #
        outputFn2 = os.path.join("dist", f"photofilmstrip-{Constants.APP_VERSION_SUFFIX}-source.tar.gz")
        gLogger.info(f"Renaming source distribution TAR ball to '{outputFn2}'")
        os.rename(outputFn1, outputFn2)


class PfsDocs(Command):

    description = "generates sphinx docs"

    user_options = [
            ('config-dir=', 'c', 'Location of the configuration directory'),
            ('project=', None, 'The documented project\'s name'),
            ('version=', None, 'The short X.Y version'),
            ('release=', None, 'The full version, including alpha/beta/rc tags'),
            ('builder=', 'b', 'The builder (or builders) to use.')
        ]
    sub_commands = []

    def initialize_options(self):
        self.config_dir = None
        self.project = ''
        self.version = ''
        self.release = ''
        self.builder = ['html']

    def finalize_options(self):
        pass

    def run(self):
        build = self.get_finalized_command('build')
        build_dir = os.path.join(os.path.abspath(build.build_base), 'sphinx')
        doctree_dir = os.path.join(build_dir, 'doctrees')
        self.mkpath(build_dir)
        self.mkpath(doctree_dir)
        confoverrides = {}
        if self.project:
            confoverrides['project'] = self.project
        if self.version:
            confoverrides['version'] = self.version
        if self.release:
            confoverrides['release'] = self.release

        for builder in self.builder:
            builder_target_dir = os.path.join(build_dir, builder)
            self.mkpath(builder_target_dir)

            app = Sphinx(
                    self.config_dir,
                    self.config_dir,
                    builder_target_dir,
                    doctree_dir,
                    builder,
                    confoverrides
                )
            app.build()

        self.distribution.data_files.extend([
                (os.path.join("share", "doc", "photofilmstrip"), glob.glob("docs/*.*")),
                (os.path.join("share", "doc", "photofilmstrip", "html"), glob.glob("build/sphinx/html/*.*")),
                (os.path.join("share", "doc", "photofilmstrip", "html", "_sources"), glob.glob("build/sphinx/html/_sources/*.*")),
                (os.path.join("share", "doc", "photofilmstrip", "html", "_static"), glob.glob("build/sphinx/html/_static/*.*"))
            ])


class PfsBuild(build):

    sub_commands = [
            ('scm_info', lambda x: True),
            ('build_sphinx', lambda x: True if Sphinx else False),
        ] + build.sub_commands

    user_options = [
            ('build-exe=', None, 'Location of the configuration directory'),
        ]

    def initialize_options(self):
        build.initialize_options(self)
        self.build_exe = None

    def finalize_options(self):
        build.finalize_options(self)
        self.build_exe = "build"

    def run(self):
        self._make_resources()
        self._make_locale()

        build.run(self)

    def _make_resources(self):
        try:
            from wx.tools.img2py import img2py
        except ImportError:
            gLogger.error("Cannot update image resources! Using images.py from source")
            return

        if sys.platform.startswith("linux") and os.getenv("DISPLAY") is None:
            gLogger.error("Cannot update image resources! img2py needs X")
            return

        imgDir = os.path.abspath(os.path.join("res", "icons"))
        if not os.path.exists(imgDir):
            return

        target = os.path.join("photofilmstrip", "res", "images.py")
        #target_mtime = os.path.getmtime(target)

        imgResources = (
                ("ICON", "photofilmstrip.svg"),

                ("PROJECT_NEW", "project_new.svg"),
                ("PROJECT_OPEN", "project_open.svg"),
                ("PROJECT_SAVE", "project_save.svg"),
                ("PROJECT_SAVE_D", "project_save_d.svg"),
                ("PROJECT_CLOSE", "project_close.svg"),
                ("PROJECT_CLOSE_D", "project_close_d.svg"),
                ("FOLDER_OPEN", "folder_open.svg"),

                ("MOTION_START_TO_END", "motion_start_to_end.svg"),
                ("MOTION_END_TO_START", "motion_end_to_start.svg"),
                ("MOTION_SWAP", "motion_swap.svg"),
                ("MOTION_MANUAL", "motion_manual.svg"),
                ("MOTION_RANDOM", "motion_random.svg"),
                ("MOTION_RANDOM_D", "motion_random_d.svg"),
                ("MOTION_CENTER", "motion_center.svg"),
                ("MOTION_CENTER_D", "motion_center_d.svg"),
                ("LOCK", "lock.svg"),
                ("UNLOCK", "unlock.svg"),

                ("MENU", "menu.svg"),
                ("ABORT", "abort.svg"),
                ("LIST_REMOVE", "list_remove.svg"),

                ("RENDER", "render.svg"),
                ("RENDER_D", "render_d.svg"),
                ("IMPORT_PICTURES", "import_pictures.svg"),
                ("IMPORT_PICTURES_D", "import_pictures_d.svg"),
                ("JOB_QUEUE", "job_queue.svg"),
                ("JOB_QUEUE_D", "job_queue_d.svg"),

                ("IMAGE_ROTATION_LEFT", "image_rotation_left.svg"),
                ("IMAGE_ROTATION_LEFT_D", "image_rotation_left_d.svg"),
                ("IMAGE_ROTATION_RIGHT", "image_rotation_right.svg"),
                ("IMAGE_ROTATION_RIGHT_D", "image_rotation_right_d.svg"),
                ("IMAGE_MOVING_LEFT", "image_moving_left.svg"),
                ("IMAGE_MOVING_LEFT_D", "image_moving_left_d.svg"),
                ("IMAGE_MOVING_RIGHT", "image_moving_right.svg"),
                ("IMAGE_MOVING_RIGHT_D", "image_moving_right_d.svg"),
                ("IMAGE_REMOVE", "image_remove.svg"),
                ("IMAGE_REMOVE_D", "image_remove_d.svg"),

                ("MUSIC", "music.svg"),
                ("MUSIC_DURATION", "music_duration.svg"),
                ("PLAY", "play.svg"),
                ("PLAY_PAUSE", "play_pause.svg"),
                ("PLAY_PAUSE_d", "play_pause_d.svg"),
                ("ARROW_UP", "arrow_up.svg"),
                ("ARROW_UP_D", "arrow_up_d.svg"),
                ("ARROW_DOWN", "arrow_down.svg"),
                ("ARROW_DOWN_D", "arrow_down_d.svg"),
                ("REMOVE", "remove.svg"),
                ("REMOVE_D", "remove_d.svg"),
                ("VIDEO_FORMAT", "video_format.svg"),

                ("ADD", "add.svg"),
                ("ALERT", "alert.svg"),
                ("PROPERTIES", "properties.svg"),
                ("EXIT", "exit.svg"),
                ("HELP", "help.svg"),
                ("ABOUT", "about.svg"),

                ("FILMSTRIP", "filmstrip.png"),
                ("DIA", "dia.svg"),
                ("DIA_S", "dia_s.svg"),
            )

        for idx, (imgName, imgFile) in enumerate(imgResources):
            file2py(
                    os.path.join(imgDir, imgFile),
                    target,
                    append=idx > 0,
                    resName=imgName
                )

    def _make_locale(self):
        for filename in os.listdir("po"):
            lang, ext = os.path.splitext(filename)
            if ext.lower() == ".po":
                moDir = os.path.join("build", "mo", lang, "LC_MESSAGES")
                moFile = os.path.join(moDir, "%s.mo" % Constants.APP_NAME)
                if not os.path.exists(moDir):
                    os.makedirs(moDir)

                self.spawn(MSGFMT + [
                            "-o",
                            moFile,
                            os.path.join("po", filename)
                        ]
                   )

                targetPath = os.path.join("share", "locale", lang, "LC_MESSAGES")
                self.distribution.data_files.append(
                        (targetPath, (moFile,))
                    )


class PfsTest(Command):

    description = "runs unit tests"

    user_options = []
    sub_commands = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        loader = unittest.TestLoader()
        suite = loader.discover("tests")
        runner = unittest.TextTestRunner()
        runner.run(suite)


class PfsWinPortableExe(Command):

    description = "create a portable executable for MS Windows (cx_freeze)"

    user_options = [
            ('target-dir=', 't', 'target directory'),
        ]
    sub_commands = [
            ('build', lambda x: True),
            ('build_exe', lambda x: True if BuildExe else False)
        ]

    def initialize_options(self):
        self.target_dir = os.path.join(
                "build",
                "dist_portable_win",
                f"photofilmstrip-{Constants.APP_VERSION_SUFFIX}-portable_{WIN_BIT_SUFFIX}"
            )

    def finalize_options(self):
        self.mkpath(self.target_dir)

    def run(self):
        localBuildExe = self.get_finalized_command('build_exe')
        localBuildExe.build_exe = self.target_dir
        #
        if Executable is None:
            raise Exception("missing cx_freeze.Executable")
        self.distribution.executables = [
                Executable(
                        os.path.join("photofilmstrip", "GUI.py"),
                        base="Win32GUI",
                        target_name=Constants.APP_NAME + ".exe",
                        icon=os.path.join("res", "icon", "photofilmstrip.ico")
                    )
            ]
        self.distribution.executables[0]._manifest = MANIFEST_TEMPLATE.encode("utf-8")
        self.distribution.executables.append(
                 Executable(
                        os.path.join("photofilmstrip", "CLI.py"),
                        target_name=Constants.APP_NAME + "-cli.exe",
                        icon=os.path.join("res", "icon", "photofilmstrip.ico")
                    )
            )
        # Run all sub-commands (at least those that need to be run)
        for cmdName in self.get_sub_commands():
            self.run_command(cmdName)
        # copy data files
        for targetDir, filelist in self.distribution.data_files:
            targetDir = os.path.join(self.target_dir, targetDir)
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            for f in filelist:
                self.copy_file(f, targetDir)
        # copy files from root directory
        otherFiles = [
                "COPYING",
                "LICENSE",
                "README-running.md"
            ]
        for f in otherFiles:
            self.copy_file(f, self.target_dir)
        #
        gLogger.info(f"Built portable executable at '{self.target_dir}'")


class PfsWinPortableZip(Command):

    description = "create a distribution ZIP file of the portable executable for MS Windows"

    user_options = []
    sub_commands = [
            ('bdist_win', lambda x: True),
       ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Run all sub-commands (at least those that need to be run)
        for cmdName in self.get_sub_commands():
            self.run_command(cmdName)
        #
        outputFn = os.path.join("dist", f"photofilmstrip-{Constants.APP_VERSION_SUFFIX}-portable_{WIN_BIT_SUFFIX}.zip")
        gLogger.info(f"Building portable zip '{outputFn}'...")
        create_zip_file(
                outputFn,
                "build/dist_portable_win",
                #virtualFolder="PhotoFilmStrip-%s" % ver,
                stripFolders=2
            )
        gLogger.info(f"Built portable zip '{outputFn}'")


class PfsInterpreterPortableZip(Command):

    description = "create a distribution ZIP file of the compiled portable Python code for Linux and MS Windows"

    user_options = [
            ("target-dir=", "t", "target directory"),
        ]
    sub_commands = [
            ("build", lambda x: True),
        ]

    def initialize_options(self):
        self.target_dir = os.path.join(
                "build",
                "dist_portable_interpreter",
                f"photofilmstrip-{Constants.APP_VERSION_SUFFIX}-portable_generic"
            )

    def finalize_options(self):
        self.mkpath(self.target_dir)

    def run(self):
        # run all sub-commands
        for cmdName in self.get_sub_commands():
            self.run_command(cmdName)
        # copy all data files (HTML docs, audio files, *.desktop, app icons, locale files and pixmaps) to 'build/.../share/'
        for dfTargetDir, dfFilelist in self.distribution.data_files:
            tmpBuildDfTargetDir = os.path.join(self.target_dir, dfTargetDir)
            if not os.path.exists(tmpBuildDfTargetDir):
                os.makedirs(tmpBuildDfTargetDir)
            for f in dfFilelist:
                self.copy_file(f, tmpBuildDfTargetDir)
        # copy files from root directory
        otherFiles = [
                "COPYING",
                "LICENSE",
                "README-running.md",
                "requirements.txt",
                "y-install_depso.sh",
                "y-venvo.sh"
            ]
        for f in otherFiles:
            self.copy_file(f, self.target_dir)
        # copy source code directory
        tmpBuildSourceDir = os.path.join("build", "lib", "photofilmstrip")
        tmpBuildTargetDir = os.path.join(self.target_dir, "app", "photofilmstrip")
        self.copy_tree(tmpBuildSourceDir, tmpBuildTargetDir)
        # generate scripts
        self.__write_run_bat(isCli=False)
        self.__write_run_bat(isCli=True)
        self.__write_run_sh(isCli=False)
        self.__write_run_sh(isCli=True)
        # change file perms of bash scripts
        for tmpFn in ["run-gui.sh", "run-cli.sh", "y-install_depso.sh", "y-venvo.sh"]:
            tmpScriptPath = os.path.join(self.target_dir, tmpFn)
            os.chmod(tmpScriptPath, stat.S_IRUSR | stat.S_IWUSR  | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
        # create ZIP file
        outputFn = os.path.join("dist", f"photofilmstrip-{Constants.APP_VERSION_SUFFIX}-portable_generic.zip")
        gLogger.info(f"Building portable zip '{outputFn}'...")
        create_zip_file(outputFn, self.target_dir, stripFolders=2)
        gLogger.info(f"Built portable zip '{outputFn}'")

    def __write_run_bat(self, isCli: bool):
        with open(os.path.join(self.target_dir, f"run-{"cli" if isCli else "gui"}.bat"), "w") as tmpScript:
            _LINEEND: Final = "\r\n"
            tmpScript.write("@echo off" + _LINEEND)
            tmpScript.write(_LINEEND)
            tmpScript.write("REM" + _LINEEND)
            tmpScript.write("REM by TS, Dec 2024" + _LINEEND)
            tmpScript.write("REM" + _LINEEND)
            tmpScript.write(_LINEEND)
            tmpScript.write("set VENV_PATH=venv-win" + _LINEEND)
            tmpScript.write(_LINEEND)
            tmpScript.write("if exist \"%VENV_PATH%\" goto runHaveVenv" + _LINEEND)
            tmpScript.write("echo Missing Python VENV in '%VENV_PATH%'." + _LINEEND)
            tmpScript.write("echo Executing '$ ./y-venvo.sh' in UCRT64 Terminal..." + _LINEEND)
            tmpScript.write("cd \"%~dp0\"" + _LINEEND)
            tmpScript.write("C:\\msys64\\ucrt64.exe \"./y-venvo.sh\"" + _LINEEND)
            tmpScript.write("echo Once the Python VENV has been created you can execute this script again" + _LINEEND)
            tmpScript.write("pause" + _LINEEND)
            tmpScript.write("goto runEnd" + _LINEEND)
            tmpScript.write(_LINEEND)
            tmpScript.write(":runHaveVenv" + _LINEEND)
            tmpScript.write(_LINEEND)
            tmpScript.write("echo Invoking PFS-" + ("CLI" if isCli else "GUI") + _LINEEND)
            tmpScript.write("cd app" + _LINEEND)
            tmpScript.write("\"..\\%VENV_PATH%\\bin\\python3.exe\" -c \"from photofilmstrip." + ("CLI" if isCli else "GUI") + " import main; main()\" %*" + _LINEEND)
            tmpScript.write("cd .." + _LINEEND)
            tmpScript.write(_LINEEND)
            tmpScript.write(":runEnd" + _LINEEND)

    def __write_run_sh(self, isCli: bool):
        with open(os.path.join(self.target_dir, f"run-{"cli" if isCli else "gui"}.sh"), "w") as tmpScript:
            _LINEEND: Final = "\n"
            tmpScript.write("#!/usr/bin/env bash" + _LINEEND)
            tmpScript.write(_LINEEND)
            tmpScript.write("#" + _LINEEND)
            tmpScript.write("# by TS, Dec 2024" + _LINEEND)
            tmpScript.write("#" + _LINEEND)
            tmpScript.write(_LINEEND)
            tmpScript.write("VAR_MYNAME=\"$(basename \"$0\")\"" + _LINEEND)
            tmpScript.write("VAR_MYDIR=\"$(dirname \"$0\")\"" + _LINEEND)
            tmpScript.write(_LINEEND)
            tmpScript.write("case \"${OSTYPE}\" in" + _LINEEND)
            tmpScript.write("\tlinux*)" + _LINEEND)
            tmpScript.write("\t\tVENV_PATH=\"venv-lx\"" + _LINEEND)
            tmpScript.write("\t\t;;" + _LINEEND)
            tmpScript.write("\tdarwin*)" + _LINEEND)
            tmpScript.write("\t\tVENV_PATH=\"venv-mac\"" + _LINEEND)
            tmpScript.write("\t\t;;" + _LINEEND)
            tmpScript.write("\tmsys*)" + _LINEEND)
            tmpScript.write("\t\tVENV_PATH=\"venv-win\"" + _LINEEND)
            tmpScript.write("\t\t;;" + _LINEEND)
            tmpScript.write("\t*)" + _LINEEND)
            tmpScript.write("\t\techo \"${VAR_MYNAME}: Error: Unknown OSTYPE '${OSTYPE}'\" >>/dev/stderr" + _LINEEND)
            tmpScript.write("\t\texit 1" + _LINEEND)
            tmpScript.write("\t\t;;" + _LINEEND)
            tmpScript.write("esac" + _LINEEND)
            tmpScript.write(_LINEEND)
            tmpScript.write("cd \"${VAR_MYDIR}\" || exit 1" + _LINEEND)
            tmpScript.write(_LINEEND)
            tmpScript.write("\"./y-venvo.sh\" || {" + _LINEEND)
            tmpScript.write("\techo \"${VAR_MYNAME}: Error: y-venvo failed\" >>/dev/stderr" + _LINEEND)
            tmpScript.write("\texit 1" + _LINEEND)
            tmpScript.write("}" + _LINEEND)
            tmpScript.write(_LINEEND)
            tmpScript.write("echo \"${VAR_MYNAME}: Invoking PFS-" + ("CLI" if isCli else "GUI") + "\" >>/dev/stderr" + _LINEEND)
            tmpScript.write("cd app || exit 1" + _LINEEND)
            tmpScript.write("\"../${VENV_PATH}/bin/python3\" -c \"from photofilmstrip." + ("CLI" if isCli else "GUI") + " import main; main()\" $@" + _LINEEND)


# ----------------------------------------------------------------------------------------------------------------------

def create_zip_file(zipFile: str, srcDir: str, stripFolders: int=0, virtualFolder: str=None):
    gLogger.info("zip %s to %s" % (srcDir, zipFile))
    if not os.path.isdir(os.path.dirname(zipFile)):
        os.makedirs(os.path.dirname(zipFile))

    zf = zipfile.ZipFile(zipFile, "w", zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(srcDir):
        fldr: str = dirpath
        if stripFolders > 0:
            fldrs: List[str] = os.path.normpath(fldr).split(os.sep)[stripFolders:]
            if fldrs:
                fldr = os.path.join(*fldrs)
            else:
                fldr = ""
        for fname in filenames:
            if virtualFolder is None:
                zipTarget = os.path.join(fldr, fname)
            else:
                zipTarget = os.path.join(virtualFolder, fldr, fname)
            gLogger.info("  deflate %s" % zipTarget)
            zf.write(os.path.join(dirpath, fname), zipTarget)
    zf.close()

def unzip_file(zipFile: str, targetDir: str, stripFolders: int=0):
    gLogger.info("unzip %s to %s" % (zipFile, targetDir))
    if not os.path.isdir(targetDir):
        os.makedirs(targetDir)

    zf = zipfile.ZipFile(zipFile, "r")
    for ele in zf.namelist():
        eleInfo = zf.getinfo(ele)
        if eleInfo.file_size == 0:
            continue

        gLogger.info("  inflate %s (%s)" % (ele, eleInfo.file_size))
        tmpEleSplit = os.path.split(ele)
        fldr: str = tmpEleSplit[0]
        fname: str = tmpEleSplit[1]

        if stripFolders > 0:
            fldrs: List[str] = os.path.normpath(fldr).split(os.sep)[stripFolders:]
            if fldrs:
                fldr: str = os.path.join(*fldrs)
            else:
                fldr = ""

        eleFldr: str = os.path.join(targetDir, fldr)
        if not os.path.isdir(eleFldr):
            os.makedirs(eleFldr)

        data = zf.read(ele)
        fd = open(os.path.join(eleFldr, fname), "wb")
        fd.write(data)
        fd.close()

def file2py(source, python_file, append, resName):
    lines = []
    with open(source, "rb") as fid:
        raw_data = fid.read()
        data = base64.b64encode(raw_data)
    while data:
        part = data[:72]
        data = data[72:]
        output = '    %s' % part
        if not data:
            output += ")"
        lines.append(output)
    data = "\n".join(lines)

    mode = "a" if append else "w"
    with open(python_file, mode) as out:
        if not append:
            out.write("# This file was generated by %s\n#\n" % os.path.basename(sys.argv[0]))
            out.write("catalog = {}\n")
            out.write("index = []\n\n")

        varName = resName
        out.write("%s = (\n%s\n" % (varName, data))
        out.write("index.append('%s')\n" % resName)
        out.write("catalog['%s'] = %s\n" % (resName, varName))
        out.write("\n")

    gLogger.info("Embedded %s using %s into %s" % (source, resName, python_file))

def __get_platform_scripts() -> List[str]:
    resArr = [
            os.path.join("scripts", "photofilmstrip.py"),
            os.path.join("scripts", "photofilmstrip-cli.py"),
            os.path.join("scripts", "photofilmstrip.bat"),
            os.path.join("scripts", "photofilmstrip-cli.bat")
        ]
    return resArr

def __get_platform_data() -> List[Tuple[str, List[str]]]:
    resArr = []
    if os.name == "nt":
        return resArr
    resArr.append(("share/applications", ["data/photofilmstrip.desktop"]))
    resArr.append(("share/pixmaps", ["data/photofilmstrip.xpm"]))

    for size in glob.glob(os.path.join("data/icons", "*")):
        for category in glob.glob(os.path.join(size, "*")):
            icons = []
            for icon in glob.glob(os.path.join(category, "*")):
                icons.append(icon)
            resArr.append(
                    (
                            "share/icons/hicolor/%s/%s" % \
                            (
                                    os.path.basename(size),
                                    os.path.basename(category)
                                ),
                            icons
                        )
                )
    return resArr

def __get_gstreamer_folders() -> List[Tuple[str, str]]:
    resArr = []
    if os.name != "nt":
        return resArr
    # add GStreamer related libraries
    msysPath = os.path.join("c:\\", "msys64", "ucrt64")
    if not os.path.exists(msysPath):
        raise Exception(f"MSYS2 path '{msysPath}' not found")
    for packageName in ("gstreamer-1.0", "girepository-1.0", "gst-validate-launcher"):
        oneFound = False
        for subFolder in ("etc", "share", "lib"):
            tmpSubFolderPathRel = os.path.join(subFolder, packageName)
            tmpSubFolderPathAbs = os.path.join(msysPath, tmpSubFolderPathRel)
            if os.path.exists(tmpSubFolderPathAbs):
                resArr.append((tmpSubFolderPathAbs, tmpSubFolderPathRel))
                oneFound = True
        if not oneFound:
            raise Exception(f"Package '{packageName}' not found")
    return resArr

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

MANIFEST_TEMPLATE = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
  <assemblyIdentity version="1.0.0.0" processorArchitecture="*" name="PhotoFilmStrip" type="win32"></assemblyIdentity>
  <description>PhotoFilmStrip</description>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity type="win32" name="Microsoft.Windows.Common-Controls" version="6.0.0.0" processorArchitecture="*" publicKeyToken="6595b64144ccf1df" language="*"/>
    </dependentAssembly>
  </dependency>
  <asmv3:application>
    <asmv3:windowsSettings xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">
      <ms_windowsSettings:dpiAware xmlns:ms_windowsSettings="http://schemas.microsoft.com/SMI/2005/WindowsSettings">true</ms_windowsSettings:dpiAware>
    </asmv3:windowsSettings>
  </asmv3:application>
</assembly>
"""

# Note that setup() will reset the logging level.
# In order to see gLogger.info() outputs run setup.py with the arg '-v'.
# gLogger.debug() won't work at all
gLogger = logging.getLogger(__name__)
logging.basicConfig(format="%(levelname)s:%(message)s", encoding="utf-8", level=logging.WARNING)

setup(
        cmdclass={
                "clean": PfsClean,
                "sdist": PfsSdist,
                "build": PfsBuild,
                "bdist_win": PfsWinPortableExe,
                "bdist_winportzip": PfsWinPortableZip,
                "sdist_interpreterportzip": PfsInterpreterPortableZip,
                "scm_info": PfsScmInfo,
                "build_sphinx": PfsDocs,
                "test": PfsTest,
                "build_exe": BuildExe,
            },
        verbose=False,
        options={
                "build_exe": {
                        #"bundle_files":1,
                        "optimize": 2,
                        "include_msvcr": False,
                        "packages": ["gi", "photofilmstrip"],
                        "includes": [
                                "gi",
                                "PIL.Image",
                                "PIL.BlpImagePlugin",
                                "PIL.BmpImagePlugin",
                                "PIL.BufrStubImagePlugin",
                                "PIL.CurImagePlugin",
                                "PIL.DcxImagePlugin",
                                "PIL.DdsImagePlugin",
                                "PIL.EpsImagePlugin",
                                "PIL.FitsImagePlugin",
                                "PIL.FliImagePlugin",
                                "PIL.FpxImagePlugin",
                                "PIL.FtexImagePlugin",
                                "PIL.GbrImagePlugin",
                                "PIL.GifImagePlugin",
                                "PIL.GribStubImagePlugin",
                                "PIL.Hdf5StubImagePlugin",
                                "PIL.IcnsImagePlugin",
                                "PIL.IcoImagePlugin",
                                "PIL.ImImagePlugin",
                                "PIL.ImtImagePlugin",
                                "PIL.IptcImagePlugin",
                                "PIL.JpegImagePlugin",
                                "PIL.Jpeg2KImagePlugin",
                                "PIL.McIdasImagePlugin",
                                "PIL.MicImagePlugin",
                                "PIL.MpegImagePlugin",
                                "PIL.MpoImagePlugin",
                                "PIL.MspImagePlugin",
                                "PIL.PalmImagePlugin",
                                "PIL.PcdImagePlugin",
                                "PIL.PcxImagePlugin",
                                "PIL.PdfImagePlugin",
                                "PIL.PixarImagePlugin",
                                "PIL.PngImagePlugin",
                                "PIL.PpmImagePlugin",
                                "PIL.PsdImagePlugin",
                                "PIL.QoiImagePlugin",
                                "PIL.SgiImagePlugin",
                                "PIL.SpiderImagePlugin",
                                "PIL.SunImagePlugin",
                                "PIL.TgaImagePlugin",
                                "PIL.TiffImagePlugin",
                                "PIL.WebPImagePlugin",
                                "PIL.WmfImagePlugin",
                                "PIL.XbmImagePlugin",
                                "PIL.XpmImagePlugin",
                                "PIL.XVThumbImagePlugin",
                            ],
                        "include_files": __get_gstreamer_folders(),
                        "excludes": [
                                "Tkconstants", "tkinter", "tcl",
                                "PIL._imagingtk", "PIL.ImageTk",
                                "_ssl", "numpy"
                            ]
                    },
                "sdist": {"formats": ["gztar"]},
                "build_sphinx": {
                        "project": Constants.APP_NAME,
                        "release": Constants.APP_VERSION_SUFFIX,
                        "config_dir": "docs/help",
                        "builder": ["html"]
                    }
            },
        data_files=[
                (os.path.join("share", "doc", "photofilmstrip"), glob.glob("docs/*.*")),
                (os.path.join("share", "photofilmstrip", "audio"), glob.glob("data/audio/*.mp3")),
            ] + __get_platform_data(),
        scripts=__get_platform_scripts(),

        name=Constants.APP_NAME.lower(),
        version=Constants.APP_VERSION_SUFFIX,
        license="GPLv2",
        description=Constants.APP_SLOGAN,
        long_description=Constants.APP_DESCRIPTION,
        author=Constants.DEVELOPERS[1],
        author_email="technisandk@gmail.com",
        url=Constants.APP_URL,

        packages=[
                "photofilmstrip",
                "photofilmstrip.action", "photofilmstrip.cli",
                "photofilmstrip.core", "photofilmstrip.core.renderer",
                "photofilmstrip.gui", "photofilmstrip.gui.ctrls",
                "photofilmstrip.gui.util",
                "photofilmstrip.lib", "photofilmstrip.lib.common",
                "photofilmstrip.lib.jobimpl",
                "photofilmstrip.res",
                "photofilmstrip.ux"
            ],
    )
