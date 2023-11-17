import ctypes

# dfsr = disable file system redirection
# use this to fix some bugs using os.listdir or os.scandir
# look the link: https://stackoverflow.com/questions/19187812

class DFSR:
    'dfsr = disable file system redirection\n\nuse this to fix some bugs using os.listdir'
    _disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
    _revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
    def __enter__(self):
        self.old_value = ctypes.c_long()
        self.success = self._disable(ctypes.byref(self.old_value))
    def __exit__(self, *args):
        if self.success:
            self._revert(self.old_value)
