# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2016-2019, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
# -----------------------------------------------------------------------------

"""
sounddevice:
https://github.com/spatialaudio/python-sounddevice/
"""

import os

from PyInstaller.compat import is_darwin, is_win
from PyInstaller.utils.hooks import get_package_paths

sfp = get_package_paths("sounddevice")

path = None
if is_win:
    path = os.path.join(sfp[0], "_sounddevice_data", "portaudio-binaries")
elif is_darwin:
    path = os.path.join(
        sfp[0], "_sounddevice_data", "portaudio-binaries", "libportaudio.dylib"
    )

if path is not None and os.path.exists(path):
    binaries = [(path,
                 os.path.join("_sounddevice_data", "portaudio-binaries"))]
