import os,sys,subprocess
py_ver = subprocess.check_output('python -V',shell=True)
if '3.10' in str(py_ver):
    os.system('pkg upgrade python -y')
    os.system('python SAHIL.py')
else:pass
current_os=subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(current_os):
    if not os.path.isfile('sahil64'):
        os.system('curl -L https://github.com/LOLIX-01/GARAM-ANDY/blob/main/sahil64?raw=true > sahil64')
        os.system('chmod 777 sahil64')
        os.system('./sahil64')
    else:
        print(' device not spported ... ')
else:
    print('\n  Unknown device, aarch or os found, contact author.')
    os.sys.exit()
