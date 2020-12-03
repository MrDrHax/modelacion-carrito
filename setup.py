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
    import streamlit, pandas, matplotlib, mpl_toolkits, numpy
    print('All software requirements are met, not runing any extra procceses.')
    doTheExit = True
except:
    print("Not all software requirements met!")
    doTheExit = False

if doTheExit:
    exit()

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

print('testing for pandas')

try:
    import pandas
    print('pandas is installed!')

except:
    print("pandas is not installed, installing...")
    install('pandas')

print('testing for matplotlib')

try:
    import matplotlib
    print('matplotlib is installed!')

except:
    print("matplotlib is not installed, installing...")
    install('matplotlib')

print('testing for mpl_toolkits')

try:
    import mpl_toolkits
    print('mpl_toolkits is installed!')

except:
    print("mpl_toolkits is not installed, installing...")
    install('mpl_toolkits')

print('testing for numpy')

try:
    import numpy
    print('numpy is installed!')

except:
    print("numpy is not installed, installing...")
    install('numpy')