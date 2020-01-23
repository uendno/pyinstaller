#-----------------------------------------------------------------------------
# Copyright (c) 2013-2020, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtCore import QTimer

app = QApplication([])
view = QWebView()
view.show()
# Exit Qt when the main loop becomes idle.
QTimer.singleShot(0, app.exit)
# Run the main loop, displaying the WebKit widget.
app.exec_()
