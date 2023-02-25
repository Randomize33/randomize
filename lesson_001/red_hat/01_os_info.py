# -*- coding: utf-8 -*-
import platform
import sys

#Сбор информации об ОС

import sys
import platform


info = 'OS info is \n{} \n\nPython version is {} {}'.format(
    platform.uname(), sys.version, platform.architecture()
)
print(info)

with open('os_info.txt','w') as ff:
    ff.write(info)