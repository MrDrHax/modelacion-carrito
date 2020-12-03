import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if sys.version_info[0] >= 3 and sys.version_info[1] >= 8 or sys.version_info[0] > 3:
    print('python version meets minimum requirements')
else:
    print('python version 3.8+ is requiered. please install it at: https://www.python.org/ to proceed.')
    exit()

try:
    import streamlit, matplotlib, pyglet, numpy
    print('All software requirements are met, not runing any extra procceses.')
    doTheExit = True
except:
    print("Not all software requirements met!")
    doTheExit = False

if doTheExit:
    exit('sys completed!')

if not input('Would you like to continue with auto installation? (y/n) ') == 'y':
    print('exiting...')
    exit()

print('testing for streamlit')

try:
    import streamlit
    print('Streamlit is installed!')

except:
    print("Streamlit is not installed, installing...")
    install('streamlit')

print('testing for matplotlib')

try:
    import matplotlib
    print('matplotlib is installed!')

except:
    print("matplotlib is not installed, installing...")
    install('matplotlib')

print('testing for pyglet')

try:
    import pyglet
    print('pyglet is installed!')

except:
    print("pyglet is not installed, installing...")
    install('pyglet')

print('testing for numpy')

try:
    import numpy
    print('numpy is installed!')

except:
    print("numpy is not installed, installing...")
    install('numpy')