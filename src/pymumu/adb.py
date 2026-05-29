class AdbMixin:
    # ADB Connection
    def adb_connect(self, index=None):
        """Connect ADB to player"""
        idx = index if index is not None else self.index
        return self._run("adb", "-v", idx, "-c", "connect")

    def adb_disconnect(self, index=None):
        """Disconnect ADB from player"""
        idx = index if index is not None else self.index
        return self._run("adb", "-v", idx, "-c", "disconnect")

    def adb_cmd(self, command: str, index=None):
        """Run a raw ADB command"""
        idx = index if index is not None else self.index
        return self._run("adb", "-v", idx, "-c", command)

    # Shell
    def shell(self, command: str, index=None):
        """Run a shell command in player"""
        idx = index if index is not None else self.index
        return self._run("sh", "-v", idx, "-c", command)

    def input_text(self, text: str, index=None):
        """Input text into player"""
        idx = index if index is not None else self.index
        return self._run("sh", "-v", idx, "-c", f"input_text {text}")

    def getprop(self, prop: str, index=None):
        """Get an Android system property"""
        idx = index if index is not None else self.index
        return self._run("sh", "-v", idx, "-c", f"getprop {prop}")

    def setprop(self, prop: str, value: str, index=None):
        """Set an Android system property"""
        idx = index if index is not None else self.index
        return self._run("sh", "-v", idx, "-c", f"setprop {prop} {value}")
    
    # Key Events
    def key_back(self, index=None):
        """Press back button"""
        idx = index if index is not None else self.index
        return self._run("sh", "-v", idx, "-c", "go_back")

    def key_home(self, index=None):
        """Press home button"""
        idx = index if index is not None else self.index
        return self._run("sh", "-v", idx, "-c", "go_home")

    def key_task(self, index=None):
        """Press recent apps button"""
        idx = index if index is not None else self.index
        return self._run("sh", "-v", idx, "-c", "go_task")

    def key_enter(self, index=None):
        """Press enter key"""
        idx = index if index is not None else self.index
        return self._run("sh", "-v", idx, "-c", "key_enter")

    def key_delete(self, index=None):
        """Press delete key"""
        idx = index if index is not None else self.index
        return self._run("sh", "-v", idx, "-c", "key_delete")

    def key_space(self, index=None):
        """Press space key"""
        idx = index if index is not None else self.index
        return self._run("sh", "-v", idx, "-c", "key_space")

    def volume_up(self, index=None):
        """Press volume up"""
        idx = index if index is not None else self.index
        return self._run("sh", "-v", idx, "-c", "volume_up")

    def volume_down(self, index=None):
        """Press volume down"""
        idx = index if index is not None else self.index
        return self._run("sh", "-v", idx, "-c", "volume_down")

    def volume_mute(self, index=None):
        """Press volume mute"""
        idx = index if index is not None else self.index
        return self._run("sh", "-v", idx, "-c", "volume_mute")