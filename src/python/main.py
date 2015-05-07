#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

from search import Search
from serial_handler import SerialHandler
from gui import GUI
import sys

def is_windows():
        return sys.platform.startswith('win')

sh = SerialHandler(0.01, 0.01)
search = Search(sh)
GUI(sh, search, windows=is_windows())
