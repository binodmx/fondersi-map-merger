from cx_Freeze import setup, Executable 
import os


includes = ['numpy.core._methods', 'numpy.lib.format']
include_files = [r"C:\Users\Binod\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll",
                 r"C:\Users\Binod\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll"]

additional_mods = []

os.environ['TCL_LIBRARY'] = r'C:\Users\Binod\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Binod\AppData\Local\Programs\Python\Python36-32\tcl'

setup(name = "Fondersi" , 
      version = "1.1" , 
      description = "" ,
      author = "Binod",
      author_email = "binod.16@cse.mrt.ac.lk",
      options={"build_exe": {"includes": includes, "include_files": include_files}},
      executables = [Executable("fondersi_gui.py",base="Win32Gui")]) 
