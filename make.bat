@echo off

if %1!==! goto makeUsage

set VENV_PATH=venv-win

if exist "%VENV_PATH%" goto makeHaveVenv
echo Missing Python VENV in '%VENV_PATH%'.
echo Executing '$ ./y-venvo.sh' in UCRT64 Terminal...
cd "%~dp0"
C:\msys64\ucrt64.exe "./y-venvo.sh"
echo Once the Python VENV has been created you can execute this script again
pause
goto makeEnd

:makeHaveVenv

if not exist ".git\config" goto makeParseArgs
git rev-parse --short HEAD > scm_rev.txt
set /p SCM_REV=<scm_rev.txt
del scm_rev.txt

:makeParseArgs

if "%1"=="clean" goto makeClean
if "%1"=="compile" goto makeCompile
if "%1"=="build-winport" goto makeBuildWinPort
if "%1"=="package-winport" goto makePackageWinPort
if "%1"=="versioninfo" goto makeVersioninfo
goto makeUsage

:makeClean
"%VENV_PATH%\bin\python3.exe" setup.py -v clean
if %ERRORLEVEL% NEQ 0 goto makeError
goto makeEnd

:makeCompile
"%VENV_PATH%\bin\python3.exe" setup.py -v clean
if %ERRORLEVEL% NEQ 0 goto makeError
"%VENV_PATH%\bin\python3.exe" setup.py -v build
if %ERRORLEVEL% NEQ 0 goto makeError
goto makeEnd

:makeBuildWinPort
"%VENV_PATH%\bin\python3.exe" setup.py -v clean
if %ERRORLEVEL% NEQ 0 goto makeError
"%VENV_PATH%\bin\python3.exe" setup.py -v bdist_win
if %ERRORLEVEL% NEQ 0 goto makeError
goto makeEnd

:makePackageWinPort
"%VENV_PATH%\bin\python3.exe" setup.py -v clean
if %ERRORLEVEL% NEQ 0 goto makeError
"%VENV_PATH%\bin\python3.exe" setup.py -v bdist_winportzip
if %ERRORLEVEL% NEQ 0 goto makeError
goto makeEnd

:makeVersioninfo
"%VENV_PATH%\bin\python3.exe" -c "from photofilmstrip import Constants; print(Constants.APP_VERSION)"
if %ERRORLEVEL% NEQ 0 goto makeError
goto makeEnd

:makeUsage
echo usage:
echo   make.bat clean
echo   make.bat compile
echo   make.bat build-winport
echo   make.bat package-winport
echo   make.bat versioninfo

goto makeEnd

:makeError
echo Error!
exit /b 1

:makeEnd
