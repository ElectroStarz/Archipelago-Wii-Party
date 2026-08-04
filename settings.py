import os
import shutil
from pathlib import Path
from typing import Union, Sequence, Any

import Utils
from Utils import T
import settings

class WPSettings(settings.Group):
    settings_key = "wp_settings"

    class AutoOpenWP(settings.Bool):
        """Enabling this will automatically open Wii Party when opening the client."""

    class DolphinExePath(settings.UserFilePath):
        """A path to the Dolphin emulator executable."""
        is_exe = True

        def browse(self, filetypes=None, **kwargs):
            from Utils import open_filename, is_windows

            # Set up the file filter based on the operating system
            if not filetypes:
                # Windows uses .exe, macOS uses .app (or no extension for Linux binaries)
                valid_exts = [".exe"] if is_windows else ["", ".app"]
                filetypes = [("Dolphin Emulator", valid_exts)]

            # Open the file dialogue
            dialog_title = "Select Dolphin Executable"
            selected_path = open_filename(dialog_title, filetypes, self)

            if not selected_path:
                return None

            self.validate(selected_path)

            # Try to use a relative path if the executable is inside the base directory
            try:
                base_dir = self.__class__("").resolve()
                rel_path = os.path.relpath(selected_path, base_dir)

                if not rel_path.startswith(".."):
                    selected_path = rel_path
            except ValueError:
                pass  # Ignores errors on Windows if files are on different drives

            return self.__class__(selected_path)

    auto_open: AutoOpenWP | bool = False
    dolphin_exe_path: DolphinExePath | str = DolphinExePath("")