import os, sys, platform

os.system('xdg-open https://facebook.com/iTx.MK.302')

bit = platform.architecture()[0]
if bit == '64bit':
        import MK

elif bit == '32bit':
    print ("Wait For 32 Bit ")
