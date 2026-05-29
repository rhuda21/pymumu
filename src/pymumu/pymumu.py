from .instance import InstanceMixin
from .control import ControlMixin
from .adb import AdbMixin
from .utils import UtilsMixin
from .shares import SharesMixin
from .exception import MuMuException

class PyMumu(InstanceMixin, AdbMixin, UtilsMixin, ControlMixin, SharesMixin):
    def __init__(self, path: str = None, index: int = 0):
        self.path = self._find_mumu()
        self.index = index
    def __repr__(self):
        return f"PyMumu(path='{self.path}', index={self.index})"