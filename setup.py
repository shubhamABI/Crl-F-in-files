# -*- coding: utf-8 -*-
import sys
import os
from cx_Freeze import setup,Executable

os.environ['TCL_LIBRARY'] = "C:\\Users\\shubham\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\shubham\\Anaconda3\\tcl\\tk8.6"
setup(
        name="FindInFiles",
        version="1.1",
        description="hi",
        executables=[Executable("FindTheWord.py")]
        )


