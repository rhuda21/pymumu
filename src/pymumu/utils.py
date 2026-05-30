import winreg
import os
import subprocess
import json
from .exception import MuMuException, MuMuNotFoundError

class UtilsMixin:
    def _find_mumu(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\MuMuPlayerGlobal")
            display_icon, _ = winreg.QueryValueEx(key, "DisplayIcon")
            winreg.CloseKey(key)
            nx_main = os.path.dirname(display_icon)
            exe = os.path.join(nx_main, "MumuManager.exe")
            if os.path.exists(exe):
                return exe
        except FileNotFoundError:
            pass
        if os.path.exists(r"C:\Program Files\Netease\MuMuPlayer\nx_main\MumuManager.exe"):
            return r"C:\Program Files\Netease\MuMuPlayer\nx_main\MumuManager.exe"
        raise MuMuNotFoundError("MuMuPlayer not found")
    def _run(self,*args, allowErrors=False):
        cmd = [self.path, *[str(a) for a in args]]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            if not allowErrors:
                raise MuMuException(f"Command {' '.join(cmd)} failed: {result.stderr}")
        if not result.stdout or not result.stdout.strip():
            return result.stdout
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError:
            return result.stdout