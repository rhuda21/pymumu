class InstanceMixin:
    # Info
    def version(self):
        """Get MuMu Player version"""
        return self._run("version")

    def info(self, index=None,allowErrors=False):
        """Get info for an instance or all instances"""
        idx = index if index is not None else self.index
        return self._run("info", "-v", idx, allowErrors=allowErrors)

    # Lifecycle
    def start(self, index=None):
        """Launch an emulator instance"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "launch")

    def stop(self, index=None):
        """Shutdown an emulator instance"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "shutdown")

    def restart(self, index=None):
        """Restart an emulator instance"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "restart")

    # Window
    def show_window(self, index=None):
        """Show player window"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "show_window")

    def hide_window(self, index=None):
        """Hide player window"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "hide_window")

    def layout_window(self, x: int = None, y: int = None, width: int = None, height: int = None, index=None):
        """Set player window position and size"""
        idx = index if index is not None else self.index
        args = ["control", "-v", idx, "layout_window"]
        if x is not None: args += ["--pos_x", x]
        if y is not None: args += ["--pos_y", y]
        if width is not None: args += ["--size_w", width]
        if height is not None: args += ["--size_h", height]
        return self._run(*args)

    # Management
    def create(self, index=None, number: int = None, mini: bool = False):
        """Create a new emulator instance"""
        args = ["create"]
        if index is not None: args += ["-v", index]
        if number is not None: args += ["-n", number]
        if mini: args.append("--mini")
        return self._run(*args)

    def clone(self, index=None, number: int = None):
        """Clone an existing emulator instance"""
        idx = index if index is not None else self.index
        args = ["clone", "-v", idx]
        if number is not None: args += ["-n", number]
        return self._run(*args)

    def delete(self, index=None):
        """Delete an emulator instance"""
        idx = index if index is not None else self.index
        return self._run("delete", "-v", idx)

    def rename(self, name: str, index=None):
        """Rename an emulator instance"""
        idx = index if index is not None else self.index
        return self._run("rename", "-v", idx, "-n", name)

    # Import / Export
    def import_player(self, file_path: str, number: int = None):
        """Import a .mumudata file"""
        args = ["import", "--path", file_path]
        if number is not None: args += ["-n", number]
        return self._run(*args)

    def export_player(self, index=None, directory: str = None, name: str = None, zip: bool = False):
        """Export an instance as .mumudata file"""
        idx = index if index is not None else self.index
        args = ["export", "-v", idx]
        if directory: args += ["--dir", directory]
        if name: args += ["--name", name]
        if zip: args.append("--zip")
        return self._run(*args)

    # Shortcuts
    def shortcut_create(self, index=None):
        """Create desktop shortcut for player"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "shortcut", "create")
    
    def shortcut_delete(self, index=None):
        """Delete desktop shortcut for player"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "shortcut", "delete")

    # Driver
    def driver_install(self):
        """Install player drivers"""
        return self._run("driver", "install")

    def driver_uninstall(self):
        """Uninstall player drivers"""
        return self._run("driver", "uninstall")

    # Log
    def log_on(self):
        """Enable manager logging"""
        return self._run("log", "on")

    def log_off(self):
        """Disable manager logging"""
        return self._run("log", "off")

    # Sort
    def sort(self):
        """Layout and sort all player windows"""
        return self._run("sort")