class MuMuException(Exception):
    """Base exception for PyMumu"""
    pass

class MuMuNotFoundError(MuMuException):
    """Raised when MuMuPlayer installation is not found"""
    def __init__(self, msg="MuMuPlayer installation not found. Install it or pass path manually."):
        super().__init__(msg)

class EmulatorNotRunningError(MuMuException):
    """Raised when trying to control an emulator that isn't running"""
    def __init__(self, msg="Emulator is not running. Start it before sending commands."):
        super().__init__(msg)

class AdbCommandError(MuMuException):
    """Raised when an ADB command fails"""
    def __init__(self, command, error):
        super().__init__(f"ADB command '{command}' failed: {error}")

class InvalidInstanceError(MuMuException):
    """Raised when an invalid emulator index is used"""
    def __init__(self, index):
        super().__init__(f"Emulator instance with index {index} does not exist")