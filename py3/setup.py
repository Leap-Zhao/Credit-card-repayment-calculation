#coding=utf-8
from distutils.core import setup
import py2exe

# setup(console=['gui.py'])  #这样写的时候运行会出现dos窗口，要把console改为windows

setup(windows=['kun.py'])
# setup(console=[{"script":"main_pyqt5.py"}])
# setup(windows=[{"script":"main_pyqt5.py"}], options={"py2exe":{"includes":["sip"]}})