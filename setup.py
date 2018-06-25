from distutils.core import setup
from cx_Freeze import *
import sys
setup(
    name='CurrencyDetector',
    version='1.0',
    packages=[''],
    url='',
    license='ibrahim',
    author='IBRAHIM',
    author_email='ibrahimkhan7777@gmail.com',
    description='Currency Detection software',
    executables=[Executable(script="gui.py",base="Win32GUI")])