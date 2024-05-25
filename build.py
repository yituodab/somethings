import os
os.system('pyinstaller -F -i ico.ico Launcher.py -y')
Input = input('version?')
os.rename(r'dist\Launcher.exe', r'Launcher-v'+Input+'.exe')