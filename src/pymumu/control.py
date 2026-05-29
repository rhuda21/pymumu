class ControlMixin:
    # App Control
    def app_install(self, apk_path: str, index=None):
        """Install an apk/apks/xapk"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "app", "install", "--apk", apk_path)

    def app_uninstall(self, package: str, index=None):
        """Uninstall an app by package id"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "app", "uninstall", "--package", package)

    def app_launch(self, package: str, index=None):
        """Launch an app by package id"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "app", "launch", "--package", package)

    def app_close(self, package: str, index=None):
        """Close an app by package id"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "app", "close", "--package", package)

    def app_info(self, package: str = None, index=None):
        """Get app info or list all installed apps"""
        idx = index if index is not None else self.index
        if package:
            return self._run("control", "-v", idx, "app", "info", "--package", package)
        return self._run("control", "-v", idx, "app", "info", "--installed")

    # Toolbar
    def tool_func(self, name: str, index=None):
        """Trigger a toolbar function.
        Options: rotate, go_home, go_back, top_most, fullscreen,
                 shake, screenshot, volume_up, volume_down, volume_mute
        """
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "tool", "func", "--name", name)

    def tool_tap(self, x: int, y: int, index=None):
        """Tap at position (x, y)"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", str(idx), "tool", "cmd", "--cmd", f"input tap {x} {y}")

    def tool_swipe(self, x1: int, y1: int, x2: int, y2: int, duration_ms: int = 100, index=None):
        """Swipe from (x1, y1) to (x2, y2)"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "tool", "cmd", "--cmd", f"input swipe {x1} {y1} {x2} {y2} {duration_ms}")

    def tool_long_press(self, x: int, y: int, duration_ms: int = 900, index=None):
        """Long press at position (x, y)"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "tool", "cmd", "--cmd", f"input swipe {x} {y} {x} {y} {duration_ms}")

    def tool_input_text(self, text: str, index=None):
        """Input text into player via toolbar"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "tool", "cmd", "--text", text)

    def tool_location(self, longitude: float, latitude: float, index=None):
        """Update GPS location. longitude: -180~180, latitude: -90~90"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "tool", "location", "--longitude", longitude, "--latitude", latitude)

    def tool_downcpu(self, cap: int, index=None):
        """Set CPU execution cap (1-100)"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "tool", "downcpu", "--cap", cap)

    def tool_gyro(self, x: float, y: float, z: float, index=None):
        """Change gravity sensing values"""
        idx = index if index is not None else self.index
        return self._run("control", "-v", idx, "tool", "gyro", "--gyro_x", x, "--gyro_y", y, "--gyro_z", z)

    # Simulation
    def set_simulation(self, key: str, value: str, index=None):
        """Change simulated properties.
        Keys: android_id, mac_address, imei
        Use '__null__' to clear value
        """
        idx = index if index is not None else self.index
        return self._run("simulation", "-v", idx, "--simu_key", key, "--simu_value", value)

    def set_android_id(self, value: str, index=None):
        """Simulate Android ID"""
        return self.set_simulation("android_id", value, index)

    def set_mac_address(self, value: str, index=None):
        """Simulate MAC address"""
        return self.set_simulation("mac_address", value, index)

    def set_imei(self, value: str, index=None):
        """Simulate IMEI"""
        return self.set_simulation("imei", value, index)

    # Settings
    def get_setting(self, key: str, index=None):
        """Get a player setting value"""
        idx = index if index is not None else self.index
        return self._run("setting", "-v", idx, "--key", key)

    def set_setting(self, key: str, value: str, index=None):
        """Set a player setting value. Use '__null__' to clear"""
        idx = index if index is not None else self.index
        return self._run("setting", "-v", idx, "--key", key, "--value", value)
    
    def enable_root(index=None):
        """Enable root permission for a player"""
        idx = index if index is not None else self.index
        return self._run("setting", "-v", idx, "--key", "root_permission", "--value", "true")

    def get_all_settings(self, index=None):
        """Get all settings for a player"""
        idx = index if index is not None else self.index
        return self._run("setting", "-v", idx, "--all")

    def set_settings_from_file(self, json_path: str, index=None):
        """Apply settings from a .json file"""
        idx = index if index is not None else self.index
        return self._run("setting", "-v", idx, "--path", json_path)